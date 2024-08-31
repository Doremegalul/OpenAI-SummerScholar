#include "someone_probabilities.h"

bool readProbabilitiesFromFile(const std::string& filename, std::map<std::string, double>& probabilities) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        return false;
    }

    std::string key;
    double value;
    while (file >> key >> value) 
    {
        probabilities[key] = value;
    }
    file.close();

    return true;
}

double calculateProbability(const std::string& word, const std::map<std::string, double>& probabilities) {
    double probability = 1.0;
    std::stringstream calculation;

    if (!word.empty()) 
    {
        std::string firstProbKey = std::string(1, word[0]) + "|";
        probability *= probabilities.at(firstProbKey);
        calculation << "(" << firstProbKey << ")" << probabilities.at(firstProbKey); 
    }

    for (size_t i = 1; i < word.length(); ++i) 
    {
        std::string pair;
        if (i == 1) 
        {  
            pair = std::string(1, word[i]) + "|" + std::string(1, word[i-1]); 
        } 
        else 
        {  
            pair = std::string(1, word[i]) + "|" + word.substr(i-2, 2);
        }
        probability *= probabilities.at(pair);
        calculation << "*(" << pair << ")" << probabilities.at(pair);	
    }

    std::cout << calculation.str() << "=" << probability << std::endl;
    return probability;
}
