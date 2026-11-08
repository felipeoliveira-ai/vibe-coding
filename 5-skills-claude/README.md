# 5 skills para o Claude Code

Do Reel: https://www.instagram.com/reel/DfdS4-ZjsrB/ · [Voltar ao início](../README.md) · Primeira vez? [Primeiros passos](../primeiros-passos/)

Manual em português para instalar cada uma, na ordem do vídeo. Precisa do [Claude Code](https://code.claude.com/docs) instalado.

Skill é um arquivo de instruções: instalou, o Claude passa a trabalhar daquele jeito.

Comando que começa com `/` roda dentro do Claude Code. Os outros rodam no terminal, ou peça para o Claude rodar.
Depois de instalar, abra uma sessão nova para a skill valer.

Antes de instalar qualquer skill, leia o que ela faz. Ela passa a ter influência sobre o que o seu agente faz.

## 1. Superpowers

Faz a IA perguntar, montar um plano e testar antes de dizer que terminou.

```text
/plugin install superpowers@claude-plugins-official
```

Repositório: https://github.com/obra/superpowers

## 2. Impeccable

Ajuda a tirar a cara de site feito por IA. Precisa do Node.

```bash
npx impeccable install
```

Abra uma sessão nova e rode uma vez em cada projeto:

```text
/impeccable init
```

Depois, para dar o acabamento numa tela: `/impeccable polish a página de preços`. Para uma crítica: `/impeccable critique a página de preços`.

Repositório: https://github.com/pbakaus/impeccable

## 3. Security Audit, da Cloudflare

Procura falha de segurança no seu código. Precisa do Node.

```bash
npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit --global
```

Use só em código seu ou que você tem autorização para testar. Ela é pesada: no nosso teste, a rodada rápida num app de 24 arquivos levou cerca de 1h30 e 3 milhões de tokens e achou as duas falhas que a gente já conhecia. Sem um ambiente isolado, os achados saem como "precisa verificar", e cada um pede conferência.

Repositório: https://github.com/cloudflare/security-audit-skill

## 4. Graphify

Desenha um mapa do seu projeto, para você ver como tudo se liga. Precisa do [uv](https://docs.astral.sh/uv/).

```bash
uv tool install graphifyy
graphify install
```

Depois, dentro do projeto:

```text
/graphify .
```

O `graphify install` acrescenta uma seção ao seu `CLAUDE.md`. No nosso teste, o mapa de um projeto com 267 arquivos de código saiu em 4,9 s, com 2.608 pontos e 5.925 conexões. Ele foi útil para enxergar o projeto, mas a busca comum achou mais arquivos ao procurar quem usa uma tabela. Use como mapa, não como substituto da busca.

Repositório: https://github.com/Graphify-Labs/graphify

## 5. Ponytail

Faz a IA olhar o que já existe antes de escrever, e escrever só o código necessário, sem cortar validação, tratamento de erro, segurança nem acessibilidade.

```text
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

Para revisar uma mudança: `/ponytail-review`. Para mudar a intensidade: `/ponytail lite`, `/ponytail full` ou `/ponytail ultra`.

No teste do criador, um campo de data caiu de 335 linhas de código para 10, porque o projeto já tinha um componente pronto. Os números são do criador; no nosso teste, com um pedido simples numa pasta vazia, deu empate.

Repositório: https://github.com/DietrichGebert/ponytail
