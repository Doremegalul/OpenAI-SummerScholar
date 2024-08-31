#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <sstream>

using namespace std;

// This program uses trigram probabilities to produce P(word) 
int main() 
{
    // ** Ask the user for the input file name
    string filename;
    cout << "Enter a file name: ";
    cin >> filename;

    ifstream file(filename);
    if (!file.is_open()) {
        cout << "Failed to open the file..." << endl;
        return -1;
    }
	
	// Map to store event names as keys and their respective probabilities as values
    map<string, double> probabilities;

    // ** Read in the trigram probabilities
    string key;
    double value;
    while (file >> key >> value) 
	{
        probabilities[key] = value;
    }
    file.close();

    while (true) 
	{
        // ** Ask the user to enter a word
        string word;
        cout << "Enter a word: ";
        cin >> word;

		// ** Repeat the following until the user wants to quit:
        if (word == "quit") 
		{
            break;
        }

		// ** Show all the probabilities you used to calculate the P(word) as I did in prob.out
        double probability = 1.0;
        stringstream calculation;

        if (!word.empty()) // Calculate initial probability P(first char)
		{
            string firstProbKey = string(1, word[0]) + "|";
            probability *= probabilities[firstProbKey];
            calculation << "(" << firstProbKey << ")" << probabilities[firstProbKey]; // (a|)
        }

        // Calculate conditional probabilities P(char|previous char)
        for (size_t i = 1; i < word.length(); ++i) {
            string pair;
            if (i == 1) // Use bigram for the second char
			{  
                pair = string(1, word[i]) + "|" + string(1, word[i-1]); 
            } 
			else // Use trigram for the third and subsequent char
			{  
                pair = string(1, word[i]) + "|" + word.substr(i-2, 2);
            }
            probability *= probabilities[pair];
            calculation << "*(" << pair << ")" << probabilities[pair];	// *(b|a)
        }
		
		// ** Show the P(word) as I did in prob.out
        cout << calculation.str() << "=" << probability << endl;
    } // ** end of loop

    return 0;