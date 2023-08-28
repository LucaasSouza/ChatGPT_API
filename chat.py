import openai
from tkinter import *
import pyttsx3

engine = pyttsx3.init() # Instância do módulo de conversão de texto para áudio
engine.setProperty("rate", 150) # Configuração da velocidade da voz
engine.setProperty("volume", 1.0) # Configuração do volume da voz

def falar_resposta(txt): # Função responsável por iniciar a voz da resposta do Chat GPT
    engine.say(txt)
    engine.runAndWait()

class Application: # Classe que monta a telinha do TKinter
    def __init__(self, master = None):
        self.frame = Frame(master, padx = 20, pady = 10)
        self.frame.pack()

        self.label = Label(self.frame, text = 'Insira uma mensagem aqui:')
        self.label.pack()

        self.input = Entry(self.frame, width = 59)
        self.input.bind('<KeyPress>', self.keyDown)
        self.input.focus_set()
        self.input.pack()

        self.frameBtn = Frame(master, padx = 20, pady = 5)
        self.frameBtn.pack()

        self.button = Button(self.frameBtn, text = 'Clique aqui para enviar a mensagem', command = self.Chat, width = 50)
        self.button.pack()

    def keyDown(self, event):
        if event.keysym == 'Return': # Verifica se a tecla do evento de keydown foi o Enter/Return. Se sim, chama a função que faz a requisição do ChatGPT
            self.Chat()
    
    def Chat(self):
        pergunta = self.input.get() # Pego o conteúdo digitado no input

        if pergunta.upper() == 'FECHAR': 
            print('Até mais!')
            return root.destroy()
        else:
            try:
                openai.api_key = 'OPENAI_API_KEY'
                request = openai.Completion.create(
                    model = "text-davinci-003",
                    prompt = pergunta,
                    max_tokens = 50,
                    temperature = 0
                )

                falar_resposta(request.choices[0].text.strip())
                self.input.delete(0, 'end')
            except:
                print('ERRO! A conversa foi encerrada.')
                return root.destroy()

root = Tk()
root.title('Conversa com o Chat GPT')
Application(root)
root.mainloop()