#importing other python files
import k2key #Contails API key - To add your own make a python file names k2key.py in the same directory and ass your key like this: API_KEY = 'Example_key'

#Importing libraries
import google.generativeai as palm
import os

os.environ['TERM'] = 'xterm-256color'

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def new_palm():
    document_content = input("Paste your entire document here or enter x to exit the program: ")
    print("At any point, type 'new' to paste a new document.")

    while True:
        Og_response = input("Would you like PalM to ask you questions, or answer your questions about the document?(ask/answer): ")
        if Og_response == 'ask':

            palm.configure(api_key=k2key.API_KEY)
            while True:
                response = palm.chat(context=document_content, messages=(f'{Og_response} ask one singular question about this document. Do not repeat questions.'), temperature=1)
                print(response.last)
                answer = input('Enter the answer to the question or press x to exit: ')
                if answer == 'x':
                    new_palm()
                else:
                    response = response.reply(f'I answered: {answer}. Answer either correct or wrong based on what I entered.')
                    print(response.last)


        elif Og_response == 'answer':
            palm.configure(api_key=k2key.API_KEY)
            while True:
                question = input("Enter your question or enter x to exit: ")
                if question == 'x':
                    new_palm()
                else:
                    response = palm.chat(context=document_content, messages=(f'{Og_response} questions about the document. Question: {question}'), temperature=1)
                    print(response.last)

        elif Og_response == 'x':
            exit()
        elif Og_response == 'new':
            new_palm()


if __name__ == '__main__':
        new_palm()







