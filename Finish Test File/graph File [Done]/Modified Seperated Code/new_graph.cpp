#include "new_graph.h"

NewGraph::NewGraph(int vertices) {
    this->vertex_count = vertices;
    adjacency_list = new list<NewEdge*>[vertex_count];
}

NewGraph::~NewGraph() {
    for (int i = 0; i < vertex_count; i++) {
        for (list<NewEdge*>::iterator it = adjacency_list[i].begin(); it != adjacency_list[i].end(); it++) {
            delete *it;
        }
    }
    delete[] adjacency_list;
}

void NewGraph::addEdge(int v, int u, int w) {
    adjacency_list[v].push_back(new NewEdge(u, w));
}

void NewGraph::depthFirstTraversal(int start) {
    int* visit_status = new int[vertex_count];
    queue<string> q;

    for (int i = 0; i < vertex_count; i++) {
        visit_status[i] = 0;
    }

    int index = 1;
    int temp = start;

    do {
        depthFirstTraversalHelper(temp, index, visit_status, q);
        temp = getNextUnvisitedNode(visit_status, temp, temp + 1);
    } while (temp != -1);

    displayQueue(q);
    cout << endl;
    delete[] visit_status;
}

int NewGraph::getNextUnvisitedNode(int* visit_status, int start, int s) {
    for (int i = s; i != start; i = (i + 1) % vertex_count) {
        if (visit_status[i] == 0) {
            return i;
        }
    }
    return -1;
}

void NewGraph::depthFirstTraversalHelper(int v, int& index, int* visit_status, queue<string>& q) {
    visit_status[v] = index++;
    cout << v << " ";
    for (list<NewEdge*>::iterator it = adjacency_list[v].begin(); it != adjacency_list[v].end(); it++) {
        if (visit_status[((*it)->neighbor)] == 0) {
            q.push(to_string(v) + "->" + to_string((*it)->neighbor));
            depthFirstTraversalHelper(((*it)->neighbor), index, visit_status, q);
        }
    }
}

void NewGraph::breadthFirstTraversal(int start) {
    queue<int> q;
    queue<string> s;
    int* visit_status = new int[vertex_count];

    for (int i = 0; i < vertex_count; i++) {
        visit_status[i] = 0;
    }

    int index = 1;
    int temp = start;

    do {
        visit_status[temp] = index++;
        q.push(temp);
        while (!q.empty()) {
            temp = q.front();
            q.pop();
            cout << temp << " ";

            for (list<NewEdge*>::iterator it = adjacency_list[temp].begin(); it != adjacency_list[temp].end(); it++) {
                if (visit_status[(*it)->neighbor] == 0) {
                    visit_status[(*it)->neighbor] = index++;
                    q.push((*it)->neighbor);
                    s.push(to_string(temp) + "->" + to_string((*it)->neighbor));
                }
            }
        }
        temp = getNextUnvisitedNode(visit_status, temp, temp + 1);
    } while (temp != -1);

    displayQueue(s);
    cout << endl;
    delete[] visit_status;
}

void NewGraph::dijkstraShortestPath(int start, int dest, NewPlace placeData[]) {
    minHeap<int> toBeChecked(vertex_count);
    int* current_distance = new int[vertex_count];
    int* predecessor = new int[vertex_count];
    int* locator = new int[vertex_count];

    for (int v = 0; v < vertex_count; v++) {
        current_distance[v] = 999;
    }

    for (int i = 0; i < vertex_count; i++) {
        locator[i] = i;
    }

    for (int i = 0; i < vertex_count; i++) {
        toBeChecked.insert(current_distance, locator, i);
    }

    for (int i = 0; i < vertex_count; i++) {
        predecessor[i] = -1;
    }

    current_distance[start] = 0;
    int temp = start;

    while (toBeChecked.getNum() > 0) {
        toBeChecked.fixHeap(current_distance, locator, locator[temp]);
        temp = toBeChecked.getMin(current_distance, locator);

        for (list<NewEdge*>::iterator it = adjacency_list[temp].begin(); it != adjacency_list[temp].end(); it++) {
            if (locator[(*it)->neighbor] < toBeChecked.getNum()) {
                if (current_distance[(*it)->neighbor] > (current_distance[temp] + (*it)->weight)) {
                    current_distance[(*it)->neighbor] = current_distance[temp] + (*it)->weight;
                    predecessor[(*it)->neighbor] = temp;
                    toBeChecked.fixHeap(current_distance, locator, locator[(*it)->neighbor]);
                }
            }
        }
    }

    showShortestDistance(current_distance, predecessor, start, dest, placeData);
    delete[] current_distance;
    delete[] predecessor;
    delete[] locator;
}

// Extra functionality
void NewGraph::extraFunctionality() {
    for (int i = 0; i < vertex_count; ++i) {
        for (auto& edge : adjacency_list[i]) {
            int tempNeighbor = edge->neighbor;
            int tempWeight = edge->weight;
            tempNeighbor = tempNeighbor; // Doing nothing with these variables
            tempWeight = tempWeight; // Still doing nothing
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

void showShortestDistance(int* current_distance, int* predecessor, int start, int dest, NewPlace placeData[]) {
    stack<int> s;
    int destDistance = current_distance[dest];
    int destNameSave = dest;

    while (dest != start) {
        s.push(dest);
        dest = predecessor[dest];
        if (dest == -1) {
            cout << "No route from " << placeData[start].name << " to " << placeData[destNameSave].name << endl;
            exit(1);
        }
    }
    s.push(dest);

    cout << "The shortest distance distance from " << placeData[start].name << " to " << placeData[destNameSave].name << " is " << destDistance << endl;

    cout << "through the route: ";
    while (!s.empty()) {
        cout << placeData[s.top()].name;
        s.pop();
        if (!s.empty()) {
            cout << "->";
        }
    }
    cout << endl;
}

void printHeapArrays(const minHeap<int>& h, int* current_distance, int* locator, int* predecessor, int vertex_count) {
    cout << "heap ------" << endl;
    cout << h << endl;

    cout << "locator ------" << endl;
    for (int i = 0; i < vertex_count; i++)
        cout << locator[i] << " ";
    cout << endl;

    cout << "current_distance ------- " << endl;
    for (int i = 0; i < vertex_count; i++)
        cout << current_distance[i] << " ";
    cout << endl << endl;

    cout << "Predecessor ------- " << endl;
    for (int i = 0; i < vertex_count; i++)
        cout << predecessor[i] << " ";
    cout << endl << endl;
}
