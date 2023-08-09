#importing other python files
import k2key #Contails API key - To add your own make a python file names k2key.py in the same directory and ass your key like this: API_KEY = 'Example_key'

#Importing libraries
import google.generativeai as palm
import os

os.environ['TERM'] = 'xterm-256color'

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def new_palm():
    document_content = input("Paste your entire document here: ")
    while True:
        print("At any point, type 'new' to paste a new document.")
        Og_response = input("Would you like PalM to ask or answer your questions about the document?(ask/answer): ")
        if Og_response == 'ask':
            palm.configure(api_key=k2key.API_KEY)

            response = palm.chat(context=document_content, messages=(f'{Og_response} questions about the document provided.'), temperature=1)
            print(response.last)

        elif Og_response == 'answer':
            question = input("What is your question?: ")

            palm.configure(api_key=k2key.API_KEY)

            response = palm.chat(context=document_content, messages=(f'{Og_response} questions about the document. Question: {question}'), temperature=1)
            print(response.last)

        elif Og_response == 'exit':
            exit()
        elif Og_response == 'new':
            new_palm()


if __name__ == '__main__':
        new_palm()







