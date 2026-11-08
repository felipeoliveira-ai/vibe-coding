#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mede quantos tokens as definições de ferramentas de um servidor MCP (HTTP) ocupam.

Só faz initialize e tools/list: não chama nenhuma ferramenta e não altera nada na sua conta.

Uso:
  python3 medir_mcp.py URL [URL ...]
  MCP_TOKEN=seu_token python3 medir_mcp.py URL   (se o servidor pedir token)

O token vem só da variável MCP_TOKEN e nunca é impresso. Com o pacote tiktoken instalado, a contagem é exata
(cl100k_base); sem ele, é uma estimativa de caracteres / 4.
"""
import json, os, sys, urllib.error, urllib.request


def contar_tokens(texto):
    try:
        import tiktoken
        return len(tiktoken.get_encoding("cl100k_base").encode(texto)), "tiktoken"
    except Exception:
        return round(len(texto) / 4), "estimativa"


class Sessao:
    def __init__(self, url):
        self.url, self.sid, self.n = url, None, 0
        self.token = os.environ.get("MCP_TOKEN", "")

    def _post(self, corpo):
        h = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream",
             "User-Agent": "medir-mcp/1.0"}
        if self.token:
            h["Authorization"] = f"Bearer {self.token}"
        if self.sid:
            h["Mcp-Session-Id"] = self.sid
        req = urllib.request.Request(self.url, data=json.dumps(corpo).encode(), headers=h, method="POST")
        with urllib.request.urlopen(req, timeout=180) as r:
            self.sid = r.headers.get("Mcp-Session-Id") or self.sid
            return r.read().decode("utf-8", "ignore"), r.headers.get("Content-Type", "")

    def pedir(self, metodo, params=None):
        self.n += 1
        txt, tipo = self._post({"jsonrpc": "2.0", "id": self.n, "method": metodo, "params": params or {}})
        if "event-stream" in tipo:
            for linha in txt.splitlines():
                if linha.startswith("data:"):
                    d = json.loads(linha[5:].strip())
                    if d.get("id") == self.n:
                        return d
            raise RuntimeError("resposta sem o id esperado")
        return json.loads(txt)

    def listar(self):
        self.pedir("initialize", {"protocolVersion": "2025-06-18", "capabilities": {},
                                  "clientInfo": {"name": "medir-mcp", "version": "1.0"}})
        self._post({"jsonrpc": "2.0", "method": "notifications/initialized"})
        ferramentas, cursor = [], None
        while True:
            d = self.pedir("tools/list", {"cursor": cursor} if cursor else {})
            if "error" in d:
                raise RuntimeError(d["error"].get("message", "erro do servidor"))
            ferramentas += d["result"]["tools"]
            cursor = d["result"].get("nextCursor")
            if not cursor:
                return ferramentas


def main():
    urls = sys.argv[1:]
    if not urls or urls[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    falhou = 0
    for url in urls:
        try:
            ferramentas = Sessao(url).listar()
        except urllib.error.HTTPError as e:
            falhou = 1
            dica = " O servidor pede login: defina MCP_TOKEN com um token de leitura." if e.code in (401, 403) else ""
            print(f"{url}\n  erro HTTP {e.code}.{dica}")
            continue
        except (urllib.error.URLError, RuntimeError, ValueError) as e:
            falhou = 1
            print(f"{url}\n  erro: {e}")
            continue
        tokens, metodo = contar_tokens(json.dumps(ferramentas, ensure_ascii=False))
        print(f"{url}\n  {len(ferramentas)} ferramentas, {tokens:,} tokens de definição ({metodo})".replace(",", "."))
    return falhou


if __name__ == "__main__":
    sys.exit(main())
