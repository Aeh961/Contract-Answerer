# Contract Answerer

## Background
This project was custom-built to provide expert advice on contracts for users, such as union members and representatives. The goal is to streamline the process of getting contract-related information, reducing the need to navigate complex documents and systems. Recognizing the potential for automation, I utilized my programming skills to develop this tool. The application is designed to be user-friendly, efficient, and informative, ensuring that users receive accurate responses to their inquiries.

## Description
**Contract Answerer** is a web application built using Streamlit and Langchain, allowing users to interact with contract-related information easily. This tool utilizes OpenAI's language models to provide accurate answers to user queries, streamlining the process of obtaining contract insights.

## Features
- Ask questions about contracts and receive instant expert advice.
- Built with a user-friendly interface for ease of use.
- Integrates OpenAI's language model for accurate responses.
- Customizable settings for advanced users.

## Installation
To run the application, you need to have Python installed on your machine. Then, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   
2. **Create a virtual environment:**

    ```bash
    Copy code
    python -m venv env

3. **Activate the virtual environment:**

    ```On macOS/Linux:
    bash
    Copy code
    source env/bin/activate
    On Windows:
    bash
    Copy code
    .\env\Scripts\activate

4. **Install the required packages:**

    ```bash
    Copy code
    pip install -r requirements.txt
    
5. **Obtain your own OpenAI API key. You will need this key to use the application effectively.**

6. **Run the application:**

    ```bash
    Copy code
    streamlit run app.py

##How to Use
Install the required packages and run the application as described in the installation section.
Open your web browser and navigate to the local address provided by Streamlit.
Enter your question regarding contracts in the input field and click "Submit."
Review the expert response generated by the application.
Please remember to obtain your own OpenAI API key, as it is required for the application to function.

##Changelog
V 1.0.0

Initial release with core functionality to answer contract-related questions.
User-friendly interface with basic styling and layout.