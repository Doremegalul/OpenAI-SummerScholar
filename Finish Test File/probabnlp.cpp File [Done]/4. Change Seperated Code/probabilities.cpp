#include "probabilities.h"

// Load trigram probabilities from a file into a map
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

// Compute the probability of a word using trigram probabilities
double calculateProbability(const std::string& word, const std::map<std::string, double>& probabilities) {
    double probability = 1.0;
    std::stringstream calculation;

    // Calculate initial probability P(first char)
    probability *= computeInitialProbability(word, probabilities, calculation);

    // Calculate conditional probabilities P(char|previous char)
    probability *= computeConditionalProbabilities(word, probabilities, calculation);

    // Display the probability calculation
    std::cout << calculation.str() << "=" << probability << std::endl;
    return probability;
}

// Compute the initial probability of the first character
double computeInitialProbability(const std::string& word, const std::map<std::string, double>& probabilities, std::stringstream& calculation) {
    double initial_prob = 1.0;
    if (!word.empty()) 
    {
        std::string firstProbKey = std::string(1, word[0]) + "|";
        initial_prob *= probabilities.at(firstProbKey);
        calculation << "(" << firstProbKey << ")" << probabilities.at(firstProbKey); 
    }
    return initial_prob;
}

// Compute the conditional probabilities for subsequent characters
double computeConditionalProbabilities(const std::string& word, const std::map<std::string, double>& probabilities, std::stringstream& calculation) {
    double conditional_prob = 1.0;
    for (size_t i = 1; i < word.length(); ++i) 
    {
        std::string pair;
        if (i == 1) 
        {  
            // Use bigram for the second char
            pair = std::string(1, word[i]) + "|" + std::string(1, word[i-1]); 
        } 
        else 
        {  
            // Use trigram for the third and subsequent char
            pair = std::string(1, word[i]) + "|" + word.substr(i-2, 2);
        }
        conditional_prob *= probabilities.at(pair);
        calculation << "*(" << pair << ")" << probabilities.at(pair);	
    }
    return conditional_prob;
}
