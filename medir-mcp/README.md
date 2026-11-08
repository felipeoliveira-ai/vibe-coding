# Medir MCP

Do Reel: https://www.instagram.com/reel/DfVB9xfhrBF/ · [Voltar ao início](../README.md)

Quanto cada MCP ocupa na memória do seu agente de IA? E como ligar o servidor da Cloudflare do jeito que gasta menos.

Teste feito em 03/11/2026, numa conta real da Cloudflare, com o script deste repositório:

| Servidor da Cloudflare | Ferramentas | Tokens só de descrição |
|---|---|---|
| Sem Code Mode (`?codemode=false`) | 3.762 | 910.477 |
| Com Code Mode | 4 | 2.471 |

Os números mudam com o tempo e dependem da forma de medir. Rode na sua máquina para ver os seus.

## 1. Ligar o servidor da Cloudflare no Claude Code

No terminal (ou peça para o Claude rodar):

```bash
claude mcp add --transport http --scope user cloudflare-api https://mcp.cloudflare.com/mcp
```

Depois abra `/mcp` no Claude Code, escolha `cloudflare-api` e autorize.

**Atenção:** na tela da Cloudflare, marque só permissões de leitura. Esse servidor executa qualquer chamada que a
permissão deixar, inclusive mudar o DNS dos seus sites no ar.

## 2. Medir os seus MCPs

Instale a skill (no terminal, ou peça para o Claude rodar):

```bash
npx skills add felipeoliveira-ai/vibe-coding --skill medir-mcp
```

E peça no Claude Code: "mede quanto o MCP tal ocupa". Sem a skill, baixe este repositório e rode de dentro da pasta dele (no Windows, use `python` no lugar de `python3`):

```bash
python3 skills/medir-mcp/medir_mcp.py "https://mcp.context7.com/mcp"
```

Para comparar com e sem Code Mode na Cloudflare, passe as duas URLs entre aspas (`"https://mcp.cloudflare.com/mcp"` e
`"https://mcp.cloudflare.com/mcp?codemode=false"`). Esse servidor pede login: defina `MCP_TOKEN` no terminal com um token **só de leitura**. O script só faz `initialize` e
`tools/list`: não chama nenhuma ferramenta e não altera nada na sua conta.

## 3. Ver o que está ocupando o contexto agora

Digite `/context` numa conversa do Claude Code. Isso mostra a ocupação do contexto atual, não o gasto total da sessão.

## Para ler mais

- [Cloudflare: Code Mode](https://blog.cloudflare.com/code-mode/)
- [Cloudflare: o servidor MCP com Code Mode](https://blog.cloudflare.com/code-mode-mcp/)
- [Código do servidor da Cloudflare](https://github.com/cloudflare/mcp)
- [Anthropic: execução de código com MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)
- [Goose: Code Mode](https://goose-docs.ai/docs/guides/managing-tools/code-mode/)

---

Mais testes de IA na prática em [@felipeoliveira.ai](https://www.instagram.com/felipeoliveira.ai/).
