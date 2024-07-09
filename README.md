### Virtual Tutor App with GPT-4All

Este é um aplicativo de tutor virtual desenvolvido em Python usando Tkinter e GPT-4All. O aplicativo permite aos usuários fazer perguntas educacionais, que são respondidas pelo modelo GPT-4All, 
um poderoso modelo de linguagem treinado pela Alignment Lab AI. As respostas são formatadas para serem claras e concisas, não excedendo quatro linhas de texto e 250 caracteres. 

#### Funcionalidades:

- **Interface Simples:** Interface gráfica amigável usando Tkinter.
- **Histórico:** Mantém um registro das perguntas feitas e suas respectivas respostas.
- **Carregamento de Modelo:** Carrega o modelo GPT-4All especificado para responder perguntas.

#### Requisitos:

- Python 3.x
- Bibliotecas: tkinter, gpt4all

#### Como usar:

1. Digite sua pergunta na caixa de texto.
2. Clique em "Perguntar" para obter uma resposta do tutor virtual.
3. O histórico de perguntas e respostas é exibido abaixo da caixa de texto.

#### Configuração do Modelo:

O modelo GPT-4All usado neste aplicativo está localizado em `C:/Users/ADS/AppData/Local/nomic.ai/GPT4All/`. Certifique-se de ajustar o caminho conforme necessário.

#### Como Executar:

Para executar o aplicativo, execute o arquivo `virtual_tutor_app.py` com Python 3.x.
Necessario "mistral-7b-openorca.gguf2.Q4_0.gguf" como modelo treinado
---

Este projeto foi desenvolvido como parte do aprendizado e experimentação com interfaces gráficas em Python e integração de modelos de linguagem avançados para educação.
