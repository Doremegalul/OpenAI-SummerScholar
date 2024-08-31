#include <iostream>
#include <math.h>
#include <string>

using namespace std;

struct Vertex {
    string Elem;
    int Value;
    Vertex* Left;
    Vertex* Right;
};

class MMBT {
public:
    Vertex* Root;
    int Bottom;
    
    MMBT() : Root(NULL) {
        cout << "Bottom Level is? ";
        cin >> Bottom;
    }

    ~MMBT() {
        dtraverse(Root);
        Root = NULL;
    }

    void dtraverse(Vertex *V) {
        if (V != NULL) {
            dtraverse(V->Left);
            dtraverse(V->Right);
            delete V;
        }
    }

    void Traverse(int mode) {
        string P = "-";

        if (mode == 1) {
            Root = new Vertex;
            DFSbuild(Root, 0, P);
        }
        if (mode == 2) {
            DFSdisplay(Root, 0);
        }
        if (mode == 3) {
            DFSminmax(Root, 0);
            cout << "Root Value is: " << Root->Value << endl;
            cout << "You can make a move now to ";
            if (Root->Left->Value == Root->Value) 
                cout << "the left" << endl;
            else 
                cout << "the right" << endl;
        }
    }

    void DFSbuild(Vertex *V, int L, string Path) {
        V->Elem = Path;
        indent(L);
        cout << "Visited: " << Path << endl;

        if (L == Bottom) {
            indent(L + 2);
            cout << "Bottom Level: " << L;
            if (iseven(L))
                cout << " for MAX" << endl;
            else
                cout << " for MIN" << endl;
            indent(L + 2);
            cout << "Score for this leaf: ";
            cin >> V->Value;
            return;
        } else {
            V->Left = new Vertex;
            V->Right = new Vertex;
            DFSbuild(V->Left, L + 1, Path + "L");
            DFSbuild(V->Right, L + 1, Path + "R");
        }   
    }

    void DFSdisplay(Vertex *V, int L) {
        if (L == Bottom) {
            indent(L);
            cout << " Bottom Level: " << L << " " << V->Elem << " with value " << V->Value << endl;
        } else {
            indent(L);
            cout << "Level: " << L << " " << V->Elem << endl;
            DFSdisplay(V->Left, L + 1);
            DFSdisplay(V->Right, L + 1);
        }
    }

    int DFSminmax(Vertex *V, int L) {
        int VL, VR;

        if (L != Bottom) {
            VL = DFSminmax(V->Left, L + 1);
            VR = DFSminmax(V->Right, L + 1);
            if (iseven(L))
                V->Value = maxof(VL, VR);
            else
                V->Value = minof(VL, VR);
            indent(L);
            cout << "Level " << L << " for ";
            if (iseven(L))
                cout << " for MAX, ";
            else
                cout << " for MIN, ";
            cout << V->Elem << " with " << V->Value << endl;
            return V->Value;
        }
        return V->Value;
    }

    int maxof(int A, int B) {
        return (A > B) ? A : B;
    }

    int minof(int A, int B) {
        return (A < B) ? A : B;
    }

    bool iseven(int L) {
        return (L % 2) == 0;
    }

    void indent(int L) {
        for (int i = 1; i <= L; i++)
            cout << " ";
    }
};

int main() {
    MMBT tree;
    tree.Traverse(1); // Build the tree
    tree.Traverse(2); // Display the tree
    tree.Traverse(3); // Perform Min-Max and display the root value

    return 0;
}
