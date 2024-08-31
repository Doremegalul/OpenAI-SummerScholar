import os
import openai
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the API key from the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def read_multiple_files(file_paths):
    combined_content = ""
    for file_path in file_paths:
        combined_content += read_file(file_path) + "\n\n" 
    return combined_content
 
# If doing multiple files, add a comma at the end and make a new lines
original_file_paths = [
   '/workspaces/OpenAI-SummerScholar/Finish Test File/probabnlp.cpp File [Done]/OG_probabnlp.cpp'
]
compare_file_paths = [
    '/workspaces/OpenAI-SummerScholar/Finish Test File/probabnlp.cpp File [Done]/5. Change Modified Seperated Code/main.cpp',
    '/workspaces/OpenAI-SummerScholar/Finish Test File/probabnlp.cpp File [Done]/5. Change Modified Seperated Code/trigram_probabilities.cpp',
    '/workspaces/OpenAI-SummerScholar/Finish Test File/probabnlp.cpp File [Done]/5. Change Modified Seperated Code/trigram_probabilities.h'
]

# Read the contents of the files
original_content = read_multiple_files(original_file_paths)
compare_content = read_multiple_files(compare_file_paths)

# Prompt engineering
prompt = f"""
You are an AI model tasked with comparing two sets of files: original files and compare files. 
Your goal is to analyze the compare files in relation to the original files, 
considering specific transformations related to unnecessary code, 
refactoring into functions, 
and splitting code into multiple files.

Also, you won't print out the entire code when giving the result.

When doing the comparison, consider the following transformation rules:
1. Adding unnecessary, random, or useless functions or code. Ignore these parts while determining similarity.
2. Separating code from the main block into functions, potentially with changes in names and variables. Recognize that functionality remains the same.
3. Splitting code from a single file into multiple files, potentially with changes in names and variables. Recognize that functionality remains the same.

Compare the compare files to the original files and provide the following:
1. A determination if the compare files are the same as the original files by answering yes or no.
2. The percent of similarity between the compare files and the original files.
3. A brief summary of the major differences between the compare files and the original files, focusing on significant changes such as added functions, major refactoring, or code splitting. Ignore minor differences like comments, indentation, or minor formatting changes.

Original Files:
{original_content}

Compare Files:
{compare_content}
"""

response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",  # Using an instruct model
    prompt=prompt,
    max_tokens=750 # Max tokens is 4130
)

print(response.choices[0].text.strip())
