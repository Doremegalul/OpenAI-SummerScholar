#ifndef PROBABILITIES_H
#define PROBABILITIES_H

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <sstream>

bool readProbabilitiesFromFile(const std::string& filename, std::map<std::string, double>& probabilities);
double calculateProbability(const std::string& word, const std::map<std::string, double>& probabilities);

#endif // PROBABILITIES_H
