#include "probabilities.h"

using namespace std;

int main() 
{
    // Ask the user for the input file name
    string filename;
    cout << "Enter a file name: ";
    cin >> filename;

    map<string, double> probabilities;
    if (!readProbabilitiesFromFile(filename, probabilities)) {
        cout << "Failed to open the file..." << endl;
        return -1;
    }

    while (true) 
    {
        // Ask the user to enter a word
        string word;
        cout << "Enter a word: ";
        cin >> word;

        // Exit the loop if the user wants to quit
        if (word == "quit") 
        {
            break;
        }

        // Calculate and display the probability of the entered word
        double probability = calculateProbability(word, probabilities);
        cout << probability << endl;
    }

    return 0;
}
