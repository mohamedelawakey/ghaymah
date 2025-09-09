# Code Assistant Chatbot

This project is a simple interactive chatbot that helps you analyze and ask questions about Python code files.

## Features
- Reads a Python file and loads its content.
- Uses an AI model (`DeepSeek-V3-0324`) for answering questions about the code.
- Provides short, clear, and concise answers.
- Keeps conversation context.
- Supports exit command (`exit` or `quit`) to end the session.

## Requirements
- Python 3.8+
- Install dependencies:
  ```bash
  pip install openai python-dotenv
  ```

## Setup
Clone or download the project.
Create a .env file and add your API key:
```bash
OPENAI_API_KEY=your_api_key_here
```
Place your Python file inside the test/ folder (default is example.py).

## Usage
Run the script:
```bash
python main.py
```
You will see:
EX:
The code is read, you can start asking about it
Type exit to exit

Then type your questions, for example:

You: What does this function do?
Bot: It reads a file and returns its content.

Type exit or quit to end the session.

## Customization
To analyze a different file, change the path in:
```bash
file_path = os.path.join("test", "example.py")
```
