import speech_recognition as sr
import openai
import pyttsx3

engine = pyttsx3.init() # Instância do módulo de conversão de texto para áudio
engine.setProperty("rate", 150) # Configuração da velocidade da voz
engine.setProperty("volume", 1.0) # Configuração do volume da voz

def resposta_voz(txt): # Função responsável por iniciar a voz da resposta do Chat GPT
    engine.say(txt)
    engine.runAndWait()

def enviar_chatGPT(pergunta): # Envia a pergunta para o Chat GPT
    try:
        openai.api_key = 'OPENAI_API_KEY'
        request = openai.Completion.create(
            model = "text-davinci-003",
            prompt = pergunta,
            max_tokens = 50,
            temperature = 0
        )

        resposta_voz(request.choices[0].text.strip())
    except:
        return print('ERRO! A conversa foi encerrada.')

def reconhecer_fala():
    microfone = sr.Recognizer() # Habilita o microfone

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source) # Reducao de ruido disponivel na speech_recognition
        print("Diga alguma coisa: ")
        audio = microfone.listen(source) # Guarda o audio falado na variavel 'audio', o audio é finalizado nas pausas grandes

        try:
            frase = microfone.recognize_google(audio_data = audio, language = 'pt-BR') #audio sera interpretado na lingua portuguesa
            enviar_chatGPT(frase)
        except:
            return print("Não entendi o que você disse!")

reconhecer_fala()