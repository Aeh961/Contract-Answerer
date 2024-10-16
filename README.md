Contract Pro: Ask the Contract Pro
Background
This project was developed to provide efficient and expert advice on contracts, addressing the needs of union members and representatives. In my experience working in union environments, I recognized the challenges many faced when navigating complex contract language and requirements. To streamline this process, I leveraged my programming skills to create Ask the Contract Pro. This application simplifies access to contract-related information and enables users to ask specific questions, leading to quicker and more informed decision-making.

Description
Ask the Contract Pro is a web application built using Streamlit and Langchain, designed to facilitate expert advice on contracts. It integrates OpenAI's language model with a Chroma database for efficient document retrieval and question answering. The application aims to empower union members by providing them with easy access to contract knowledge and resources.

Features
Expert Advice: Get accurate responses to contract-related queries in real time.
Document Retrieval: Access relevant documents and information quickly through the integrated database.
User-Friendly Interface: A clean and intuitive interface that makes it easy for users to navigate and find information.
Customizable Queries: Users can ask specific questions to receive tailored answers related to their contracts.
Installation
Clone the repository to your local machine.
bash
Copy code
git clone https://github.com/yourusername/contract-pro.git
Navigate to the project directory.
bash
Copy code
cd contract-pro
Set up a virtual environment (optional but recommended).
bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install the required packages.
bash
Copy code
pip install -r requirements.txt
Obtain your own OpenAI API key: Sign up for an OpenAI account and get your API key. Make sure to keep this key secure.
Set the OpenAI API key in your application.
How to Use
Launch the application by running the following command in your terminal:
bash
Copy code
streamlit run app.py
Open your web browser and navigate to the URL provided in the terminal.
Enter your question regarding contracts in the input field.
Click the "Submit" button to receive a detailed response.
Review the provided guidelines to ensure proper contact with your union representative for additional support.
Changelog
V 1.0.0

Initial release of Ask the Contract Pro.
Integrated OpenAI for natural language processing and document retrieval via Chroma.
V 1.0.1

Improved error handling for API requests.
Added user interface enhancements for better usability.
V 1.0.2

Updated the backend to support additional document formats.
Enhanced response accuracy based on user feedback.
V 1.0.3

Fixed bugs related to document retrieval.
Updated styling for a more professional look and feel.
