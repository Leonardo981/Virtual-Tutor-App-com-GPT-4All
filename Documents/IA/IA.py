from tkinter import *
from gpt4all import GPT4All

class VirtualTutorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tutor Virtual de Educação")

        self.history = []  

        self.create_widgets()
        self.load_model()

    def create_widgets(self):
        self.text_label = Label(self.master, text="Digite sua pergunta ao tutor online:")
        self.text_label.pack()

        self.text_entry = Entry(self.master, width=50)
        self.text_entry.pack()

        self.ask_button = Button(self.master, text="Perguntar", command=self.answer_question)
        self.ask_button.pack()

        self.result_label = Label(self.master, text="", wraplength=400)
        self.result_label.pack()

        self.history_label = Label(self.master, text="Histórico de Perguntas e Respostas:")
        self.history_label.pack()

        self.history_text = Text(self.master, state='disabled', width=50, height=10, wrap='word')
        self.history_text.pack()

        self.clear_button = Button(self.master, text="Limpar Histórico", command=self.clear_history)
        self.clear_button.pack()

    def load_model(self):
        MODEL_NAME = "mistral-7b-openorca.gguf2.Q4_0.gguf"
        MODELS_FOLDER = "C:/Users/ADS/AppData/Local/nomic.ai/GPT4All/"
        try:
            self.model = GPT4All(model_name=MODEL_NAME, model_path=MODELS_FOLDER, allow_download=False)
            print("Modelo carregado com sucesso")
        except Exception as e:
            print(f"Erro ao carregar o modelo: {e}")
            self.model = None

    def answer_question(self):
        print("Pergunta recebida")
        input_text = self.text_entry.get()

        if not self.model:
            self.result_label.config(text="Erro: modelo não carregado")
            return

        
        self.result_label.config(text="")

        answer = self.get_answer_from_model(input_text)
        print("Resposta gerada:", answer)

        
        self.update_history(input_text, answer)
        self.text_entry.delete(0, END)

    def get_answer_from_model(self, input_text):
        SYSTEM_TEMPLATE = '''
        sistema
        Você é MistralOrca, um grande modelo de linguagem treinado pela Alignment Lab AI.
        Seu objetivo é responder a perguntas educacionais de forma clara e concisa.
        As respostas não podem exceder a 250 caracteres.
        Dê todas as respostas em português.
        A resposta deve ser clara e detalhada, mas não deve exceder quatro linhas de texto.
        '''
        PROMPT_TEMPLATE = f'''
        usuário
        {input_text}
        assistente
        '''
        
        prompt = SYSTEM_TEMPLATE + PROMPT_TEMPLATE
        try:
            response = self.model.generate(prompt)
            print("Resposta concluída com sucesso")
            print("Resposta bruta:", response)

            formatted_response = self.format_response(response.strip())
            return formatted_response
        except Exception as e:
            print(f"Erro ao gerar resposta: {e}")
            return "Erro ao responder a pergunta"

    def format_response(self, response):
        if len(response) > 250:
            response = response[:250] + '...'
        lines = response.split('\n')
        if len(lines) > 4:
            return '\n'.join(lines[:4])
        return response

    def update_history(self, question, answer):
        self.history.append((question, answer))
        self.history_text.config(state='normal')
        self.history_text.insert(END, f"Pergunta: {question}\nResposta: {answer}\n\n")
        self.history_text.config(state='disabled')
        self.history_text.see(END)

    def clear_history(self):
        self.history_text.config(state='normal')
        self.history_text.delete(1.0, END)
        self.history_text.config(state='disabled')
        self.history = []  

def main():
    root = Tk()
    app = VirtualTutorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
