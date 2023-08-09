# PDFQuery

This project is a Python script that utilizes the PaLM API from Google's Generative AI library to create a chatbot. The chatbot interacts with users by asking questions and providing answers based on the document that is pasted.

## Getting Started

To use this project, you need an API key for the PaLM API. Save the API key in a Python file named `k2key.py` in the same directory as the script. You can obtain an API key from the Google Cloud Console.

## Prerequisites

- Python 3.x
- PaLM API key

## Installation

1. Clone the repository to your local machine.
2. Create a Python file named `k2key.py` in the same directory as the script.
3. Add your PaLM API key to the `k2key.py` file in the following format: `API_KEY = 'your_api_key_here'`.

## Usage

To run the script, execute it in a Python environment. The script will prompt you to enter a message to start the conversation. The `new_palm()` function handles the conversation. It prompts for user input, generates responses using the PaLM API, and continues the conversation until the user chooses to reset or exit.


## Built With

- Python
- PaLM API from Google's Generative AI library

## Acknowledgments

- The Google Generative AI Python Client was used to interact with the PaLM API.

## Contact

- [Kishan Rajeev](https://kishan.jeevsol.com/)

## License

Licensed under the MIT License.

