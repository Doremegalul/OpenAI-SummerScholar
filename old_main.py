import os
from dotenv import load_dotenv, find_dotenv
import openai
from difflib import SequenceMatcher

# Load the .env file
load_dotenv(find_dotenv())

# Initialize OpenAI API client
openai.api_key = os.getenv('OPENAI_API_KEY')

model = "gpt-4o"  # Using gpt-4o as per your latest confirmation
temperature = 0.1
max_tokens = 2000

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
    except Exception as e:
        return str(e)

def compare_files(content1, content2):
    similarity_ratio = SequenceMatcher(None, ''.join(content1), ''.join(content2)).ratio()
    return similarity_ratio

def display_file_content(file_content):
    return ''.join(file_content)

def chat():
    print("Welcome to the chat box! Type 'exit' to end the conversation.")
    print("Type 'upload file' to upload a file.")
    print("Type 'compare files' to compare the last two uploaded files.")
    print("Type 'show files' to see the list of uploaded files.")
    print("Type 'show content' to see the content of the last uploaded file.\n")

    conversation_history = [
        {"role": "assistant", "content": "Type 'upload file' to upload a file. Type 'compare files' to compare the last two uploaded files. Type 'show files' to see the list of uploaded files. Type 'show content' to see the content of the last uploaded file."}
    ]
    files = []
    file_names = []

    while True:
        user_input = input("You: ")
        print("")  # Add single space for readability
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Check if the user wants to provide a file
        if user_input.lower() == 'upload file':
            file_path = input("Please provide the path to the code file: ")
            file_content = read_file(file_path)
            if isinstance(file_content, str):
                print(f"Error reading file: {file_content}")
                user_input = "There was an error reading the file."
            else:
                print(f"Content of {file_path}:\n{display_file_content(file_content)}")
                files.append(file_content)
                file_names.append(file_path)
                user_input = f"Here is the content of the file {file_path}:\n{display_file_content(file_content)}"

        # Check if the user wants to compare files
        elif user_input.lower() == 'compare files':
            if len(files) >= 2:
                content1, content2 = files[-2], files[-1]
                similarity = compare_files(content1, content2)
                user_input = f"The similarity between the last two files is {similarity:.2f}"
            else:
                user_input = "You need to upload at least two files before comparing."

        # Check if the user wants to see the list of uploaded files
        elif user_input.lower() == 'show files':
            if file_names:
                user_input = "Uploaded files:\n" + "\n".join(file_names)
            else:
                user_input = "No files have been uploaded yet."

        # Check if the user wants to see the content of the last uploaded file
        elif user_input.lower() == 'show content':
            if files:
                last_file_content = files[-1]
                user_input = f"Here is the content of the last uploaded file:\n{display_file_content(last_file_content)}"
            else:
                user_input = "No files have been uploaded yet."

        # Add user input to conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Generate a response from the model without altering file content
        if user_input.lower() not in ['upload file', 'compare files', 'show files', 'show content']:
            response = openai.ChatCompletion.create(
                model=model,
                messages=conversation_history,
                temperature=temperature,
                max_tokens=max_tokens
            )

            # Extract the model's response
            bot_response = response.choices[0].message["content"].strip()
            print(f"AI: {bot_response}\n")  # Add single space for readability

            # Add the bot's response to the conversation history
            conversation_history.append({"role": "assistant", "content": bot_response})

if __name__ == "__main__":
    chat()
