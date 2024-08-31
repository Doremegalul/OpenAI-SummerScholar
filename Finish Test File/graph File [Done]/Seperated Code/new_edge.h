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
