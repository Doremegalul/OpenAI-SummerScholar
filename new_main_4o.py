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
    '/workspaces/OpenAI-SummerScholar/Finish Test File/PCB File [Done]/pcb.h',
    '/workspaces/OpenAI-SummerScholar/Finish Test File/PCB File [Done]/pcbtable.cpp',
    '/workspaces/OpenAI-SummerScholar/Finish Test File/PCB File [Done]/pcbtable.h',
    '/workspaces/OpenAI-SummerScholar/Finish Test File/PCB File [Done]/readyqueue.cpp',
    '/workspaces/OpenAI-SummerScholar/Finish Test File/PCB File [Done]/readyqueue.h'
]
compare_file_paths = [
    '/workspaces/OpenAI-SummerScholar/Finish Test File/PCB File [Done]/Useless Added Code/ex_pcb.h',
    '/workspaces/OpenAI-SummerScholar/Finish Test File/PCB File [Done]/Useless Added Code/ex_pcbtable.cpp',
    '/workspaces/OpenAI-SummerScholar/Finish Test File/PCB File [Done]/Useless Added Code/ex_pcbtable.h',
    '/workspaces/OpenAI-SummerScholar/Finish Test File/PCB File [Done]/Useless Added Code/ex_readyqueue.cpp',
    '/workspaces/OpenAI-SummerScholar/Finish Test File/PCB File [Done]/Useless Added Code/ex_readyqueue.h'
]

# Read the contents of the files
original_content = read_multiple_files(original_file_paths)
compare_content = read_multiple_files(compare_file_paths)

# Prompt engineering
prompt = f"""

You are an AI model tasked with comparing two sets of files: original files and compare files. 
Your goal is to analyze the compare files in relation to the original files, considering specific transformations related to unnecessary code, refactoring into functions, and splitting code into multiple files.
Sometimes, the unnesscary code are codes that are useless or does not do anything that affect the entire codebase.
Sometimes, the splitting code into multiple files functions similarly and it is just the names or variables that only changes.
If you are looking at C++ code, you should not pay attention too much to the library of "using namespace std;". It should not matter.
Also, comments should not matter.

Compare the compare files to the original files and provide the following:
1. The percent of similarity between the compare files and the original files.
2. Conclude whether the compare files are similar to the original files or no by following this rule: if the percent of similarity is more than 90%, then answer "Yes"; otherwise, just say "No".
3. A brief summary of the major differences between the compare files and the original files, focusing on significant changes such as added functions, major refactoring, or code splitting. Ignore minor differences like comments, indentation, or minor formatting changes.

Focus on identifying changes such as:
- Renaming of variables, functions, or classes.
- Addition of useless or redundant code.
- Minor refactoring that does not change the core functionality.
- Reordering code without changing functionality.
- Formatting changes such as indentation or whitespace.

When doing the comparison, consider the following transformation rules that people usually do when they modify the original files:
1. Refactoring:
   - Removing unnecessary else.
   - Removing unnecessary self.
   - Replacing loop-based lookups with index with direct referencing.
   - Simplifying boolean expressions by removing unnecessary explicit references to True or False.
   - Converting for loops into list comprehensions.
   - Computing the hash value of a certain class that contains more than one parameter.
   - Removing unnecessary casts to int, str, float, and bool.
   - Merging multiple comparisons into a single one.
   - Replacing for loop-based summed values with sum comprehensions.
   - Creating lists with values instead of creating empty lists and appending to them.
   - Merging nested if conditions.
   - Inlining a variable or a return in the case when the variable being declared is immediately returned.
   - Removing unused index in a for loop or comprehension with an underscore.
   - Do not assign to built-in variables such as list.
   - Simplifying constant sum() call.
   - Removing unnecessary verbose length comparisons.
   - Using any rather than a for loop.
   - Lifting code into else after break in control flow.
   - Using max/min default argument instead of if statement.
   - Restructuring conditional to merge duplicative branches.
   - Replacing cases of a variable being multiplied by itself with squaring that variable.
   - Moving assignment of variables closer to their usage within a block.
   - Merging else clause nested if statement into elif.
   - Using the built-in function next instead of a for-loop.
   - Swapping if and else branches of conditionals.
   - Simplifying conditionals into a form more like a switch statement.
   - Switching not any or not all statements to all or any statements respectively.
   - Removing conditional tests where the conditional is always True or False.
   - Using str.join() instead of for loop.
   - Replacing for a append loop with list extend.
   - Hoisting nested repeated code outside conditional statements.
   - Converting list/set/tuple comprehensions that do not change the input elements into.
   - Merging consecutive list appends into a single extend.

2. Reordering:
   - Using dictionary.items() in for loops to access both key and value at the same time.
   - Removing unnecessary slice indices.
   - Comparing the hash values of two operands involved in an "+" operation, and reordering them or remaining unchanged, ensuring operands with larger values always come before smaller ones.
   - Comparing the hash values of two operands involved in a "-" operation, and reordering them or remaining unchanged, ensuring operands with larger values always come before smaller ones.
   - Comparing the hash values of two operands involved in an ">" or "<" operation, and reordering them or remaining unchanged, ensuring operands with larger values always come before smaller ones.
   - Comparing the hash values of two operands involved in a ">=" or "<=" operation, and reordering them or remaining unchanged, ensuring operands with larger values always come before smaller ones.
   - Comparing the hash values of two code blocks involved in an if-else assignment, and reordering them or remaining unchanged, ensuring operands with larger values always come before smaller ones.

3. Formatting:
   - Fixing excessive indentations.
   - Fixing inconsistent whitespace around operators or keywords.
   - Fixing extraneous whitespaces.
   - Fixing whitespaces after comment signs.
   - Align closing bracket to match opening bracket.


Original Files:
{original_content}

Compare Files:
{compare_content}
"""

response = openai.ChatCompletion.create(
    model="gpt-4o",  # Using GPT-4o model
    messages=[
        {"role": "system", "content": "You are an AI model tasked with comparing code files."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=4096,  # Adjust to fit within the allowed range
    temperature=0,  # Setting temperature to 0 for deterministic results
    top_p=1.0  # Ensuring top_p is set to include the highest probability tokens
)

print(response.choices[0].message['content'].strip())
