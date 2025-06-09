# OpenAI-SummerScholar

This project is part of the Summer Scholar program at CSUSM, where I worked with a faculty mentor. The goal was to utilize Artificial Intelligence (AI) to detect plagiarism and provide both an accuracy score and reasoning. With the help of the OpenAI API, I used OpenAI's models to identify potential plagiarism and developed prompt engineering techniques, with plans for fine-tuning, to improve detection performance.

new_main.py:

Compares two code files (original vs modified) using OpenAI’s GPT-3.5-turbo-instruct. It checks for similarity while ignoring useless additions or formatting changes. Outputs a similarity score and a short explanation of key differences.

new_main_4o.py:

An extended version that supports multiple files and uses GPT-4o. It applies a detailed set of rules to detect meaningful changes like function refactoring or code reorganization. Gives a similarity percentage, a yes/no verdict, and a concise summary of major transformations.
