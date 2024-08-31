#ifndef TRIGRAM_PROBABILITIES_H
#define TRIGRAM_PROBABILITIES_H

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <sstream>

// Function to load trigram probabilities from a file into a map
bool loadTrigramProbabilities(const std::string& filename, std::map<std::string, double>& probabilities);

// Function to compute the probability of a word using trigram probabilities
double computeWordProbability(const std::string& word, const std::map<std::string, double>& probabilities);

// Function to compute the initial probability of the first character
double computeInitialProbability(const std::string& word, const std::map<std::string, double>& probabilities, std::stringstream& prob_calculation);

// Function to compute the conditional probabilities for subsequent characters
double computeConditionalProbabilities(const std::string& word, const std::map<std::string, double>& probabilities, std::stringstream& prob_calculation);

#endif // TRIGRAM_PROBABILITIES_H
