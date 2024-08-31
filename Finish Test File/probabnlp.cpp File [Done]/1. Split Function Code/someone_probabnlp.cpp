#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <sstream>

using namespace std;

bool getFileName(string &filename);
bool readProbabilities(const string &filename, map<string, double> &probabilities);
void processWords(const map<string, double> &probabilities);
double calculateProbability(const string &word, const map<string, double> &probabilities, stringstream &calculation);

int main() 
{
    string filename;
    if (!getFileName(filename)) {
        return -1;
    }

    map<string, double> probabilities;
    if (!readProbabilities(filename, probabilities)) {
        return -1;
    }

    processWords(probabilities);

    return 0;
}

bool getFileName(string &filename) {
    cout << "Enter a file name: ";
    cin >> filename;

    ifstream file(filename);
    if (!file.is_open()) {
        cout << "Failed to open the file..." << endl;
        return false;
    }
    file.close();
    return true;
}

bool readProbabilities(const string &filename, map<string, double> &probabilities) {
    ifstream file(filename);
    if (!file.is_open()) {
        cout << "Failed to open the file..." << endl;
        return false;
    }

    string key;
    double value;
    while (file >> key >> value) {
        probabilities[key] = value;
    }
    file.close();
    return true;
}

void processWords(const map<string, double> &probabilities) {
    while (true) {
        string word;
        cout << "Enter a word: ";
        cin >> word;

        if (word == "quit") {
            break;
        }

        stringstream calculation;
        double probability = calculateProbability(word, probabilities, calculation);
        cout << calculation.str() << "=" << probability << endl;
    }
}

double calculateProbability(const string &word, const map<string, double> &probabilities, stringstream &calculation) {
    double probability = 1.0;

    if (!word.empty()) { 
        string firstProbKey = string(1, word[0]) + "|";
        probability *= probabilities.at(firstProbKey);
        calculation << "(" << firstProbKey << ")" << probabilities.at(firstProbKey);
    }

    for (size_t i = 1; i < word.length(); ++i) {
        string pair;
        if (i == 1) {
            pair = string(1, word[i]) + "|" + string(1, word[i - 1]);
        } else {
            pair = string(1, word[i]) + "|" + word.substr(i - 2, 2);
        }
        probability *= probabilities.at(pair);
        calculation << "*(" << pair << ")" << probabilities.at(pair);
    }

    return probability;
}
