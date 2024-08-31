#ifndef NEW_GRAPH_H
#define NEW_GRAPH_H

#include <iostream>
#include <queue>
#include <list>
#include <string>
#include <stack>
#include "new_edge.h"
#include "new_place.h"

using namespace std;

class graph {
    int num_ver;
    list<edge*>* ver_ar;
    int nextUnvisitedNodes(int* num, int start, int s);
    void DFT_helper(int v, int& i, int* num, queue<string>& q);
public:
    graph(int V);
    ~graph();
    void addEdge(int v, int u, int w = 1);
    void BFT(int start);
    void DFT(int start);
    void DijkstraShortestPath(int start, int dest, Place cityData[]);
    void extraFunctionality();
};

#endif // NEW_GRAPH_H
