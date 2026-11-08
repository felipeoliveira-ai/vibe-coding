---
name: medir-mcp
description: "Mede quantos tokens as definições de ferramentas de um servidor MCP ocupam. Use quando a pessoa perguntar quanto um MCP pesa, quanto contexto ele ocupa ou se vale a pena manter um MCP ligado, ou quiser comparar um servidor com e sem Code Mode."
---

# Medir MCP

Mede o peso de um servidor MCP (HTTP) e explica o resultado em português simples.

1. Pergunte a URL do servidor, se a pessoa não tiver dado. Para comparar com e sem Code Mode na Cloudflare, use
   `https://mcp.cloudflare.com/mcp` e `https://mcp.cloudflare.com/mcp?codemode=false`.
2. Rode, a partir da pasta desta skill:
   ```bash
   python3 medir_mcp.py URL [URL ...]
   ```
3. Se o servidor pedir login (HTTP 401 ou 403), peça que a pessoa defina a variável `MCP_TOKEN` no próprio terminal com
   um token **só de leitura**. Nunca peça para colar o token na conversa e nunca imprima o valor.
4. Explique o número: é o espaço que as descrições ocupariam se o agente carregasse todas de uma vez. O Claude Code
   costuma carregar sob demanda; `/context` mostra o que está ocupando o contexto agora.

O script só faz `initialize` e `tools/list`. Ele não chama ferramenta nenhuma e não altera nada na conta.
