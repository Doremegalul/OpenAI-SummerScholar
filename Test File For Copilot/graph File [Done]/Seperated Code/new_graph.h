#ifndef NEW_PLACE_H
#define NEW_PLACE_H

#include <string>

struct Place {
    int num;
    std::string abr;
    std::string name;
    int population;
    int elevation;
};

#endif // NEW_PLACE_H

#ifndef NEW_EDGE_H
#define NEW_EDGE_H

class edge {
    friend class graph;
    int neighbor;
    int wt;
public:
    edge() { neighbor = -999, wt = -999; };
    edge(int u, int w) { neighbor = u, wt = w; };
};

#endif // NEW_EDGE_H

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

#include "new_graph.h"

graph::graph(int num) {
    this->num_ver = num;
    ver_ar = new list<edge*>[num_ver];
}

graph::~graph() {
    for (int i = 0; i < num_ver; i++) {
        for (list<edge*>::iterator u = ver_ar[i].begin(); u != ver_ar[i].end(); u++) {
            delete *u;
        }
    }
    delete[] ver_ar;
}

void graph::addEdge(int v, int u, int w) {
    ver_ar[v].push_back(new edge(u, w));
}

void graph::DFT(int start) {
    int* num = new int[num_ver];
    queue<string> q;

    for (int i = 0; i < num_ver; i++) {
        num[i] = 0;
    }

    int i = 1;
    int temp = start;

    do {
        DFT_helper(temp, i, num, q);
        temp = nextUnvisitedNodes(num, temp, temp + 1);
    } while (temp != -1);

    displayQueue(q);
    cout << endl;
    delete[] num;
}

int graph::nextUnvisitedNodes(int* num, int start, int s) {
    for (int i = s; i != start; i = (i + 1) % num_ver) {
        if (num[i] == 0) {
            return i;
        }
    }
    return -1;
}

void graph::DFT_helper(int v, int& i, int* num, queue<string>& q) {
    num[v] = i++;
    cout << v << " ";
    for (list<edge*>::iterator u = ver_ar[v].begin(); u != ver_ar[v].end(); u++) {
        if (num[((*u)->neighbor)] == 0) {
            q.push(to_string(v) + "->" + to_string((*u)->neighbor));
            DFT_helper(((*u)->neighbor), i, num, q);
        }
    }
}

void graph::BFT(int start) {
    queue<int> q;
    queue<string> s;
    int* num = new int[num_ver];

    for (int i = 0; i < num_ver; i++) {
        num[i] = 0;
    }

    int i = 1;
    int temp = start;

    do {
        num[temp] = i++;
        q.push(temp);
        while (!q.empty()) {
            temp = q.front();
            q.pop();
            cout << temp << " ";

            for (list<edge*>::iterator u = ver_ar[temp].begin(); u != ver_ar[temp].end(); u++) {
                if (num[(*u)->neighbor] == 0) {
                    num[(*u)->neighbor] = i++;
                    q.push((*u)->neighbor);
                    s.push(to_string(temp) + "->" + to_string((*u)->neighbor));
                }
            }
        }
        temp = nextUnvisitedNodes(num, temp, temp + 1);
    } while (temp != -1);

    displayQueue(s);
    cout << endl;
    delete[] num;
}

void graph::DijkstraShortestPath(int start, int dest, Place cityData[]) {
    // Implementation of Dijkstra's algorithm
}

// Extra functionality
void graph::extraFunctionality() {
    // Implementation of extra functionality
}

template<class T>
void displayQueue(queue<T>& q) {
    while (!q.empty()) {
        cout << q.front() << ",";
        q.pop();
    }
}

void showShortestDistance(int* curDist, int* predecessor, int start, int dest, Place cityData[]) {
    // Implementation of showing the shortest distance
}

void printHeapArrays(const minHeap<int>& h, int* curDist, int* locator, int* predecessor, int num_ver) {
    // Implementation of printing heap arrays
}