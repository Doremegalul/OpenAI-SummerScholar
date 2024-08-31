#include <stdio.h>
#include <unistd.h>
#include <iostream>
#include <fcntl.h>
#include <cstring>
#include <sys/wait.h>

using namespace std;

#define MAX_LINE 80 // Define the maximum command length

// Flags for detecting special tokens in commands
bool token_input = false, token_output = false;
bool token_and = false, token_pipe = false;

// Array to store the most recent command for the history feature
char history[MAX_LINE] = "";

// Useless function
void uselessFunction(const char* command)
{
	const char* temp = command;
	temp = temp; // Doing nothing with this variable
}

/**
 * @brief Parse the command input into arguments and set flags for special tokens.
 *
 * @param command The command input string.
 * @param args The parsed arguments are stored in this array.
 * @return The number of arguments parsed.
 */
int parse_command(char command[], char* args[])
{
	int index = 0;
	char* token = strtok(command, " \t\n");

	while (token != NULL)
	{
		// Handle pipe symbol
		if (strcmp(token, "|") == 0)
		{
			token_pipe = true;
			args[index++] = strtok(NULL, " \t\n");
		}
		// Handle input redirection
		else if (strcmp(token, "<") == 0)
		{
			token_input = true;
			args[index++] = strtok(NULL, " \t\n");
		}
		// Handle output redirection
		else if (strcmp(token, ">") == 0)
		{
			token_output = true;
			args[index++] = strtok(NULL, " \t\n");
		}
		// Handle background process
		else if (strcmp(token, "&") == 0)
		{
			token_and = true;
		}
		// Handle commands ending with '&' for background process
		else if (token[strlen(token) - 1] == '&')
		{
			token[strlen(token) - 1] = '\0';
			args[index++] = token;
			token_and = true;
		}
		// Otherwise, treat the token as an argument
		else
		{
			args[index++] = token;
		}
		token = strtok(NULL, " \t\n");
	}
	args[index] = NULL;
	uselessFunction(command); // Useless function call
	return index;
}

/**
 * @brief Redirect standard input to read from the given file.
 *
 * @param shell_args The shell arguments to redirect input from.
 */
void input_redirection(char* shell_args)
{
	int in = open(shell_args, O_RDONLY);
	dup2(in, STDIN_FILENO);
	close(in);
	uselessFunction(shell_args); // Useless function call
}

/**
 * @brief Redirect standard output to write to the given file.
 *
 * @param shell_args The shell arguments to redirect output to.
 */
void output_redirection(char* shell_args)
{
	int out = open(shell_args, O_CREAT | O_WRONLY | O_TRUNC);
	dup2(out, STDOUT_FILENO);
	close(out);
	uselessFunction(shell_args); // Useless function call
}

/**
 * @brief The main function of a simple UNIX Shell.
 *
 * @param argc The number of command-line arguments.
 * @param argv The command-line arguments.
 * @return The exit status of the program.
 */
int main(int argc, char* argv[])
{
	char command[MAX_LINE]; // The input command string
	char* args[MAX_LINE / 2 + 1]; // Array to hold parsed arguments
	int should_run = 1; // Flag to determine when to exit program

	while (should_run)
	{
		// Reset all flags at the start of each loop
		token_input = token_output = token_and = token_pipe = false;

		printf("osh>");
		fflush(stdout);

		// Read user's command
		fgets(command, MAX_LINE, stdin);

		// Check for history command
		if (strcmp(command, "!!\n") == 0)
		{
			if (strlen(history) == 0)
			{
				printf("No command history found.\n");
				continue;
			}
			else
			{
				printf("%s", history);
				strcpy(command, history);
			}
		}
		else
		{
			// Update the most recent command in history
			strcpy(history, command);
		}

		// Parse command into arguments
		int num_args = parse_command(command, args);

		// Skip if the command is empty
		if (num_args == 0) continue;

		// Exit the shell if user enters "exit"
		if (strcmp(args[0], "exit") == 0)
		{
			should_run = 0;
			continue;
		}

		// Check if the command should run in the background
		bool is_background = false;
		if (strcmp(args[num_args - 1], "&") == 0)
		{
			is_background = true;
			args[num_args - 1] = NULL;
		}

		// Fork to create a new process
		pid_t pid = fork();
		if (pid == 0)
		{
			// Child process
			if (token_input)
			{
				// Handle input redirection
				input_redirection(args[--num_args]);
				args[num_args] = NULL;
			}
			if (token_output)
			{
				// Handle output redirection
				output_redirection(args[--num_args]);
				args[num_args] = NULL;
			}
			// Execute the parsed command
			if (execvp(args[0], args) == -1)
			{
				perror("Command not found\n");
				exit(EXIT_FAILURE);
			}
		}
		else if (pid < 0)
		{
			// Forking failed
			perror("Error forking");
		}
		else
		{
			// Parent process
			if (!token_and)
			{
				// Wait for child process to finish
				waitpid(pid, NULL, 0);
			}
		}
	}
	return 0;
}
