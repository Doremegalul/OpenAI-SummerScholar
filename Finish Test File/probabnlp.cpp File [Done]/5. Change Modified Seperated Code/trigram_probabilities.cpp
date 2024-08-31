#include "trigram_probabilities.h"

// Load trigram probabilities from a file into a map
bool loadTrigramProbabilities(const std::string& filename, std::map<std::string, double>& probabilities) {
    std::ifstream infile(filename);
    if (!infile.is_open()) {
        return false;
    }

    std::string trigram_key;
    double trigram_value;
    while (infile >> trigram_key >> trigram_value) 
    {
        probabilities[trigram_key] = trigram_value;
    }
    infile.close();

    return true;
}

// Compute the probability of a word using trigram probabilities
double computeWordProbability(const std::string& word, const std::map<std::string, double>& probabilities) {
    double word_prob = 1.0;
    std::stringstream prob_calculation;

    // Calculate initial probability P(first char)
    word_prob *= computeInitialProbability(word, probabilities, prob_calculation);

    // Calculate conditional probabilities P(char|previous char)
    word_prob *= computeConditionalProbabilities(word, probabilities, prob_calculation);

    // Display the probability calculation
    std::cout << prob_calculation.str() << "=" << word_prob << std::endl;
    return word_prob;
}

// Compute the initial probability of the first character
double computeInitialProbability(const std::string& word, const std::map<std::string, double>& probabilities, std::stringstream& prob_calculation) {
    double initial_prob = 1.0;
    if (!word.empty()) 
    {
        std::string initial_prob_key = std::string(1, word[0]) + "|";
        initial_prob *= probabilities.at(initial_prob_key);
        prob_calculation << "(" << initial_prob_key << ")" << probabilities.at(initial_prob_key); 
    }
    return initial_prob;
}

// Compute the conditional probabilities for subsequent characters
double computeConditionalProbabilities(const std::string& word, const std::map<std::string, double>& probabilities, std::stringstream& prob_calculation) {
    double conditional_prob = 1.0;
    for (size_t i = 1; i < word.length(); ++i) 
    {
        std::string trigram_key;
        if (i == 1) 
        {  
            // Use bigram for the second char
            trigram_key = std::string(1, word[i]) + "|" + std::string(1, word[i-1]); 
        } 
        else 
        {  
            // Use trigram for the third and subsequent char
            trigram_key = std::string(1, word[i]) + "|" + word.substr(i-2, 2);
        }
        conditional_prob *= probabilities.at(trigram_key);
        prob_calculation << "*(" << trigram_key << ")" << probabilities.at(trigram_key);	
    }
    return conditional_prob;
}
