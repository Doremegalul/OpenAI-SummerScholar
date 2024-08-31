#include "trigram_probabilities.h"

using namespace std;

int main() 
{
    // Ask the user for the input file name
    string input_filename;
    cout << "Enter a file name: ";
    cin >> input_filename;

    map<string, double> trigram_probs;
    if (!loadTrigramProbabilities(input_filename, trigram_probs)) {
        cout << "Failed to open the file..." << endl;
        return -1;
    }

    while (true) 
    {
        // Ask the user to enter a word
        string user_word;
        cout << "Enter a word: ";
        cin >> user_word;

        // Exit the loop if the user wants to quit
        if (user_word == "quit") 
        {
            break;
        }

        // Calculate and display the probability of the entered word
        double word_probability = computeWordProbability(user_word, trigram_probs);
        cout << word_probability << endl;
    }

    return 0;
}
