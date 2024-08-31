#ifndef PROBABILITIES_H
#define PROBABILITIES_H

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <sstream>

// Function to load trigram probabilities from a file into a map
bool readProbabilitiesFromFile(const std::string& filename, std::map<std::string, double>& probabilities);

// Function to compute the probability of a word using trigram probabilities
double calculateProbability(const std::string& word, const std::map<std::string, double>& probabilities);

// Function to compute the initial probability of the first character
double computeInitialProbability(const std::string& word, const std::map<std::string, double>& probabilities, std::stringstream& calculation);

// Function to compute the conditional probabilities for subsequent characters
double computeConditionalProbabilities(const std::string& word, const std::map<std::string, double>& probabilities, std::stringstream& calculation);

#endif // PROBABILITIES_H
