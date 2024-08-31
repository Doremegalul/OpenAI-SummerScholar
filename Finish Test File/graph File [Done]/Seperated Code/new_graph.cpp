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
    minHeap<int> toBeChecked(num_ver);
    int* curDist = new int[num_ver];
    int* predecessor = new int[num_ver];
    int* locator = new int[num_ver];

    for (int v = 0; v < num_ver; v++) {
        curDist[v] = 999;
    }

    for (int i = 0; i < num_ver; i++) {
        locator[i] = i;
    }

    for (int i = 0; i < num_ver; i++) {
        toBeChecked.insert(curDist, locator, i);
    }

    for (int i = 0; i < num_ver; i++) {
        predecessor[i] = -1;
    }

    curDist[start] = 0;
    int temp = start;

    while (toBeChecked.getNum() > 0) {
        toBeChecked.fixHeap(curDist, locator, locator[temp]);
        temp = toBeChecked.getMin(curDist, locator);

        for (list<edge*>::iterator u = ver_ar[temp].begin(); u != ver_ar[temp].end(); u++) {
            if (locator[(*u)->neighbor] < toBeChecked.getNum()) {
                if (curDist[(*u)->neighbor] > (curDist[temp] + (*u)->wt)) {
                    curDist[(*u)->neighbor] = curDist[temp] + (*u)->wt;
                    predecessor[(*u)->neighbor] = temp;
                    toBeChecked.fixHeap(curDist, locator, locator[(*u)->neighbor]);
                }
            }
        }
    }

    showShortestDistance(curDist, predecessor, start, dest, cityData);
    delete[] curDist;
    delete[] predecessor;
    delete[] locator;
}

// Extra functionality
void graph::extraFunctionality() {
    for (int i = 0; i < num_ver; ++i) {
        for (auto& e : ver_ar[i]) {
            int tempNeighbor = e->neighbor;
            int tempWt = e->wt;
            tempNeighbor = tempNeighbor; // Doing nothing with these variables
            tempWt = tempWt; // Still doing nothing
        }
    }
}

template<class T>
void displayQueue(queue<T>& q) {
    while (!q.empty()) {
        cout << q.front() << ",";
        q.pop();
    }
}

void showShortestDistance(int* curDist, int* predecessor, int start, int dest, Place cityData[]) {
    stack<int> s;
    int destDist = curDist[dest];
    int destNameSave = dest;

    while (dest != start) {
        s.push(dest);
        dest = predecessor[dest];
        if (dest == -1) {
            cout << "No route from " << cityData[start].name << " to " << cityData[destNameSave].name << endl;
            exit(1);
        }
    }
    s.push(dest);

    cout << "The shortest distance distance from " << cityData[start].name << " to " << cityData[destNameSave].name << " is " << destDist << endl;

    cout << "through the route: ";
    while (!s.empty()) {
        cout << cityData[s.top()].name;
        s.pop();
        if (!s.empty()) {
            cout << "->";
        }
    }
    cout << endl;
}

void printHeapArrays(const minHeap<int>& h, int* curDist, int* locator, int* predecessor, int num_ver) {
    cout << "heap ------" << endl;
    cout << h << endl;

    cout << "locator ------" << endl;
    for (int i = 0; i < num_ver; i++)
        cout << locator[i] << " ";
    cout << endl;

    cout << "curDist ------- " << endl;
    for (int i = 0; i < num_ver; i++)
        cout << curDist[i] << " ";
    cout << endl << endl;

    cout << "Predecessor ------- " << endl;
    for (int i = 0; i < num_ver; i++)
        cout << predecessor[i] << " ";
    cout << endl << endl;
}
