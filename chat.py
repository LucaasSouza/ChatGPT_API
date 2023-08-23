import openai
from tkinter import *

class Application:
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
        if event.keysym == 'Return':
            self.Chat()

    def Chat(self):
        pergunta = self.input.get()

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

                self.input.delete(0, 'end')
                return print(f'Pergunta: {pergunta}\nResposta: {request.choices[0].text.strip()}')
            except:
                print('ERRO! A conversa foi encerrada.')
                return root.destroy()

root = Tk()
root.title('Conversa com o Chat GPT')
Application(root)
root.mainloop()