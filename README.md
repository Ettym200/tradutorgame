# 🎮 Game Translator

Tradução simultânea de legendas e textos de jogos usando IA, direto na sua tela.

![Python](https://img.shields.io/badge/Python-3.8+-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Branch](https://img.shields.io/badge/Linux-branch%20linux--support-orange)

> ⚠️ **Usuários Linux:** use a branch [`linux-support`](https://github.com/Ettym200/tradutorgame/tree/linux-support) — ela contém suporte a hotkeys via `pynput` e o script `iniciar.sh`.

---

## O que é?

Game Translator é um app desktop que captura uma região da sua tela e traduz o texto automaticamente usando IA. Ideal para jogar games com legendas em inglês ou outro idioma sem precisar pausar ou sair do jogo.

A tradução aparece num overlay flutuante e transparente diretamente sobre o jogo, podendo ser movido e redimensionado livremente.

---

## Funcionalidades

- **Tradução em tempo real** ou **sob demanda** (uma vez)
- **Overlay arrastável e redimensionável** sobre qualquer jogo
- **Seleção visual da região** — define exatamente onde monitorar
- **Suporte a múltiplos provedores de IA:**
  - OpenRouter (recomendado, tem plano grátis)
  - Groq (grátis e rápido)
  - OpenAI (GPT-4o-mini)
  - Anthropic (Claude)
  - Custom (qualquer API compatível com OpenAI)
- **Atalhos de teclado globais** — funcionam mesmo com o jogo em foco
- **Detecção inteligente de mudança** — só chama a IA quando o texto muda, economizando tokens

---

## Como instalar

### Windows

1. Instale o [Python 3.8+](https://www.python.org/downloads/) — marque **"Add Python to PATH"**
2. Clone ou baixe este repositório
3. Execute `instalar.bat` — instala todas as dependências automaticamente
4. Execute `iniciar.bat` para abrir o app

> O app pedirá permissão de administrador automaticamente — necessário para os atalhos de teclado funcionarem dentro do jogo.

### Linux

> ⚠️ Use a branch **`linux-support`** — a branch `master` é apenas para Windows.

1. Instale o Python 3.8+ pelo seu gerenciador de pacotes:
```bash
# Ubuntu/Debian
sudo apt install python3 python3-pip

# Arch
sudo pacman -S python python-pip
```
2. Clone a branch correta:
```bash
git clone -b linux-support https://github.com/Ettym200/tradutorgame
cd tradutorgame
pip install -r requirements.txt
```
3. Execute o app:
```bash
bash iniciar.sh
```

> **Wayland vs X11:** funciona melhor no X11. No Wayland os atalhos globais podem ter limitações. Se não funcionarem, rode com `sudo`.

---

## Como usar

### 1. Configure a API

Escolha um provedor e obtenha sua API Key:

| Provedor | Plano grátis | Link |
|---|---|---|
| OpenRouter | ✅ Sim | [openrouter.ai](https://openrouter.ai) |
| Groq | ✅ Sim | [console.groq.com](https://console.groq.com) |
| OpenAI | ❌ Pago | [platform.openai.com](https://platform.openai.com) |
| Anthropic | ❌ Pago | [console.anthropic.com](https://console.anthropic.com) |

Cole a chave no campo **API Key** do app.

### 2. Selecione a região

- Abra o jogo e deixe o texto/legenda aparecer
- Clique em **Selecionar região** ou pressione `F9`
- Arraste para delimitar a área onde ficam as legendas

### 3. Traduza

**Modo "Traduzir uma vez"** — pressione `F10` ou clique no botão. Ideal para ler descrições de itens, missões, etc.

**Modo "Contínuo"** — monitora a região automaticamente e traduz quando o texto muda. Ideal para diálogos e cutscenes.

---

## Atalhos de teclado

| Tecla | Ação |
|---|---|
| `F9` | Abrir seletor de região |
| `F10` | Traduzir agora / Iniciar-Parar |
| `F11` | Mostrar / ocultar tradução |

> Os atalhos só funcionam com o jogo em foco se o app estiver rodando como **administrador**.

---

## Overlay

A janela de tradução flutua sobre o jogo:

- **Mover** — arraste pela barra vermelha no topo
- **Redimensionar** — arraste o canto inferior direito
- **Ocultar** — clique no ✕ ou pressione `F11`

---

## Compilar em .exe

Para distribuir sem expor o código fonte:

```
compilar.bat
```

O executável gerado fica em `dist/GameTranslator.exe`.

---

## Apoie o projeto

Se o app te ajudou, considere apoiar via Pix dentro do próprio app clicando em **❤ Apoiar via Pix**.

---

## Licença

MIT — use, modifique e distribua à vontade.
