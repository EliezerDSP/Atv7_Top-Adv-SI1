# Pipeline de Transcrição de Áudio e Extração de Pontos-Chave

Este projeto implementa um pipeline automatizado em Python que recebe um arquivo de áudio (como `.mp3` ou `.wav`), realiza a transcrição completa do conteúdo utilizando o **OpenAI Whisper**, e em seguida processa o texto gerado com o **Ollama (Llama 3.2:1b)** para extrair um resumo e os principais pontos-chave.

## Tecnologias Utilizadas

* **Python 3.10+**
* **OpenAI Whisper:** Para transcrição de áudio local de alta precisão.
* **Ollama (Modelo `llama3.2:1b`):** Para processamento de linguagem natural (NLP) e extração inteligente de tópicos em ambiente estritamente local.
* **FFmpeg:** Requisito de sistema necessário para o Whisper processar arquivos de mídia.

---

## Instalação e Configuração

### 1. Pré-requisitos do Sistema

O Whisper exige que a ferramenta de sistema `ffmpeg` esteja instalada na sua máquina.

* **Linux (Ubuntu/Debian):**
    ```bash
    sudo apt update && sudo apt install ffmpeg -y
    ```
* **macOS (via Homebrew):**
    ```bash
    brew install ffmpeg
    ```
* **Windows:** Baixe pelo site oficial ou use o Chocolatey/Scoop:
    ```bash
    choco install ffmpeg
    ```

### 2. Configuração do Ollama

Certifique-se de que o Ollama está instalado e rodando em segundo plano. Em seguida, baixe o modelo abaixo (recomendável para dispositivos com menor capacidade computacional), ou use qualquer outro modelo de linguagem de sua preferência:

```bash
ollama pull llama3.2:1b
