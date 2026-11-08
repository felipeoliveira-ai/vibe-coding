# Skills que eu uso

[Voltar ao início](../README.md) · Primeira vez? [Comece pelo Claude Code](../claude-code/)

Skill é um arquivo de instruções para o Claude. Instalou, ele passa a trabalhar daquele jeito. Estas são as que eu
uso no dia a dia, com o comando para instalar cada uma.

**Como instalar:** copie o comando, cole na conversa do Claude Code e escreva "instala isto para mim". Ele roda e te
avisa. Comando que começa com `/` você digita direto na conversa. Depois de instalar, abra uma conversa nova.

Antes de instalar qualquer skill, leia o que ela faz. Ela passa a influenciar o que o seu agente faz.

## Para trabalhar melhor

### Superpowers

Faz o Claude perguntar, montar um plano e testar antes de dizer que terminou. É a primeira que eu instalo.

```text
/plugin install superpowers@claude-plugins-official
```

No terminal: `claude plugin install superpowers@claude-plugins-official`

Repositório: https://github.com/obra/superpowers

### Ponytail

Faz o Claude olhar o que já existe antes de escrever e escrever só o código necessário.

```text
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

No terminal: `claude plugin marketplace add DietrichGebert/ponytail && claude plugin install ponytail@ponytail`

Repositório: https://github.com/DietrichGebert/ponytail

### Caveman

Faz o Claude responder curto e direto, sem enrolação, mantendo os comandos e os detalhes técnicos. Menos texto para
você ler. O criador diz que corta cerca de 65% dos tokens.

```text
/plugin marketplace add JuliusBrussee/caveman
/plugin install caveman@caveman
```

No terminal: `claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman`

Para desligar numa conversa, escreva "normal mode".

Repositório: https://github.com/JuliusBrussee/caveman

### Graphify

Desenha um mapa do seu projeto, para você ver como tudo se liga. Precisa do uv
([como instalar](../claude-code/#5-quando-o-guia-pede-node-ou-uv)).

```bash
uv tool install graphifyy
graphify install
```

Repositório: https://github.com/Graphify-Labs/graphify

## Para vídeo e animação

### HyperFrames

O Claude monta vídeos no seu computador: legenda, gráficos, efeitos e animação. É com ela que eu edito os meus
Reels. Instala um pacote de skills de vídeo. Precisa do Node.

```bash
npx skills add heygen-com/hyperframes
```

Repositório: https://github.com/heygen-com/hyperframes

### Motion Design

Ensina ao Claude os princípios de animação: tempo, suavidade e a ordem em que as coisas se mexem. Precisa do Node.

```bash
npx skills add LottieFiles/motion-design-skill
```

Repositório: https://github.com/LottieFiles/motion-design-skill

## Para sites e segurança

### Frontend Design, da Anthropic

Faz o Claude caprichar no visual de sites e telas: ele escolhe uma direção, as fontes e as cores, em vez do visual
padrão de IA. É a skill oficial da Anthropic. Precisa do Node.

```bash
npx skills add anthropics/skills --skill frontend-design
```

Repositório: https://github.com/anthropics/skills

### Impeccable

Ajuda a tirar a cara de site feito por IA. Precisa do Node.

```bash
npx impeccable install
```

Repositório: https://github.com/pbakaus/impeccable

### Security Audit, da Cloudflare

Procura falha de segurança no seu código. Use só em código seu. É pesada: detalhes no
[guia das 5 skills](../5-skills-claude/). Precisa do Node.

```bash
npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit --global
```

Repositório: https://github.com/cloudflare/security-audit-skill

## Feita por mim

### Medir MCP

Mede quanto cada MCP pesa na memória do seu agente. Guia completo: [medir-mcp](../medir-mcp/). Precisa do Node.

```bash
npx skills add felipeoliveira-ai/vibe-coding --skill medir-mcp
```
