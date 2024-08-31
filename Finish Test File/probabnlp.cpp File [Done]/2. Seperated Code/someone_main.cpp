#include "someone_probabilities.h"

using namespace std;

int main() 
{
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
        string word;
        cout << "Enter a word: ";
        cin >> word;

        if (word == "quit") 
        {
            break;
        }

        double probability = calculateProbability(word, probabilities);
        cout << probability << endl;
    }

    return 0;
}