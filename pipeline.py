import whisper
import ollama

# INDIQUE O SEU ARQUIVO AQUI (Substitua pelo caminho do seu áudio)
ARQUIVO_AUDIO = "audio.mp3"

# ==========================================
# PASSO 1: Transcrição com Whisper
# ==========================================
print("[*] Transcrevendo o áudio...")
# Carrega o modelo (pode alterar para "tiny", "base", "small" ou "large")
modelo_whisper = whisper.load_model("base")
# Transcreve o arquivo de áudio selecionado
resultado = modelo_whisper.transcribe(ARQUIVO_AUDIO, fp16=False)
texto_transcrito = resultado['text']


# ==========================================
# PASSO 2: Extração de Pontos-Chave com Ollama
# ==========================================
print("[*] Extraindo pontos-chave...")
# Cria a instrução para a IA
prompt = f"""
Com base na transcrição abaixo, faça um breve resumo e liste os pontos-chave em tópicos:
Transcrição: {texto_transcrito}
"""

# Envia o texto transcrito para o modelo local processar: "Llama 3.2:1b (de 1 bilhão de parâmetros)"
resposta = ollama.generate(model="llama3.2:1b", prompt=prompt)


# ==========================================
# PASSO 3: Exibição do Resultado
# ==========================================
print("\n=== ANÁLISE DO TEXTO ===")
print(resposta['response'])
