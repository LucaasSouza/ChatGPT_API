import speech_recognition as sr
import openai

def reconhecer_fala():
    microfone = sr.Recognizer() # Habilita o microfone

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source) # Reducao de ruido disponivel na speech_recognition
        print("Diga alguma coisa: ")
        audio = microfone.listen(source) # Guarda o audio falado na variavel 'audio', o audio é finalizado nas pausas grandes

        try:
            frase = microfone.recognize_google(audio_data = audio, language = 'pt-BR') #audio sera interpretado na lingua portuguesa

            try:
                openai.api_key = 'OPENAI_API_KEY'
                request = openai.Completion.create(
                    model = "text-davinci-003",
                    prompt = frase,
                    max_tokens = 50,
                    temperature = 0
                )

                return print(f'Pergunta: {frase}\nResposta: {request.choices[0].text.strip()}')
            except:
                print('ERRO! A conversa foi encerrada.')
        except:
            print("Não entendi o que você disse!")

reconhecer_fala()