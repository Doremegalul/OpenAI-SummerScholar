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

class NewGraph {
    int vertex_count;
    list<NewEdge*>* adjacency_list;
    int getNextUnvisitedNode(int* visit_status, int start, int s);
    void depthFirstTraversalHelper(int v, int& index, int* visit_status, queue<string>& q);
public:
    NewGraph(int vertices);
    ~NewGraph();
    void addEdge(int v, int u, int w = 1);
    void breadthFirstTraversal(int start);
    void depthFirstTraversal(int start);
    void dijkstraShortestPath(int start, int dest, NewPlace placeData[]);
    void extraFunctionality();
};

#endif // NEW_GRAPH_H
