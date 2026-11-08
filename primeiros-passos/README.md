# Primeiros passos

[Voltar ao início](../README.md)

O básico para seguir qualquer guia daqui, mesmo sem nunca ter programado. Informações conferidas na documentação
oficial em 08/11/2026.

## 1. O que é o Claude Code

É o assistente de IA da Anthropic que trabalha no seu computador: ele lê arquivos, roda comandos e monta coisas
para você. Você conversa com ele em português.

Para usar, você precisa de uma assinatura do Claude (Pro, Max, Ultra, Team ou Enterprise) ou de uma conta no
Claude Console. Planos e preços: https://claude.com/pricing

## 2. Instale o Claude Code

**Jeito mais fácil, sem terminal:** baixe o aplicativo do Claude para computador e use o Claude Code dentro dele.

https://claude.com/download

**Pelo terminal:** abra o terminal (veja o passo 3), cole o comando do seu sistema e aperte Enter.

No Mac:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

No Windows, no PowerShell:

```powershell
irm https://claude.ai/install.ps1 | iex
```

A instalação não mostra progresso enquanto baixa. Quando terminar, feche o terminal, abra outro e digite `claude`
para começar. Na primeira vez, ele pede para você entrar na sua conta do Claude.

Deu erro? A página oficial de instalação explica cada caso: https://code.claude.com/docs/en/setup

## 3. O que é o terminal e como abrir

É uma janela onde você digita comandos em vez de clicar.

- **Mac:** aperte Command + Espaço, digite `Terminal` e aperte Enter.
- **Windows:** clique no menu Iniciar, digite `PowerShell` e abra.

Guia oficial do terminal, com imagens: https://code.claude.com/docs/en/terminal-guide

## 4. Como copiar e usar um comando dos guias

- Todo comando fica num bloco cinza. Passe o mouse em cima e clique no botão de copiar, no canto do bloco.
- Comando que começa com `/` você digita dentro do Claude Code, na conversa com ele.
- Os outros você cola no terminal e aperta Enter. Ou cole na conversa e peça para o Claude rodar.
- Depois de instalar uma skill ou um plugin, abra uma conversa nova para ele começar a valer.

## 5. Quando o guia pede Node ou uv

São programas que alguns comandos usam para instalar coisas.

- **Node:** baixe a versão LTS em https://nodejs.org. Comandos que começam com `npx` precisam dele.
- **uv:** instruções em https://docs.astral.sh/uv/. Só um guia pede.

Na dúvida, peça para o Claude: "Confere se eu tenho o Node instalado e, se não tiver, me ajuda a instalar."

## 6. Palavras que aparecem nos guias

| Palavra | O que quer dizer |
|---|---|
| Repositório | Uma pasta de arquivos guardada no GitHub, como esta. |
| Skill | Um arquivo de instruções. Instalou, o Claude passa a trabalhar daquele jeito. |
| Plugin | Um pacote que junta skills e comandos para instalar de uma vez. |
| MCP | Uma ponte que liga o Claude a outro serviço, como a sua conta da Cloudflare. |
| Comando | Uma linha de texto que você cola no terminal para o computador fazer algo. |
| Terminal | A janela onde você cola os comandos. |

## Antes de instalar qualquer coisa

- Leia o que a skill ou o plugin faz. Ele passa a influenciar o que o seu agente faz.
- Nunca cole senha, chave ou token num comando que você não entende.
- Se ficar em dúvida, pergunte para o Claude o que o comando faz antes de rodar.
