#ifndef NEW_EDGE_H
#define NEW_EDGE_H

class NewEdge {
    friend class NewGraph;
    int neighbor;
    int weight;
public:
    NewEdge() { neighbor = -999, weight = -999; };
    NewEdge(int u, int w) { neighbor = u, weight = w; };
};

#endif // NEW_EDGE_H
