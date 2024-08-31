#include "mmbt.h"
#include <math.h>
#include <iostream>
using namespace std;

// ======== Utility Functions for Min Max ==============

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

// Extra functionality
void utilityExtraFunctionality(int A, int B, int L) {
    int tempA = A;
    int tempB = B;
    int tempL = L;
    tempA = tempA;
    tempB = tempB;
    tempL = tempL;
}

//===== Public Functions ===============

MMBT::MMBT() {
    Root = NULL;
    cout << "Bottom Level is? "; cin >> Bottom;
}

MMBT::~MMBT() {
    dtraverse(Root);
    Root = NULL;
}

// Extra functionality
void MMBT::constructorExtraFunctionality() {
    int tempBottom = Bottom;
    tempBottom = tempBottom;
}

void MMBT::Traverse(int mode) {
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

// Extra functionality
void MMBT::traverseExtraFunctionality(int mode) {
    int tempMode = mode;
    tempMode = tempMode;
}

void MMBT::DFSbuild(Vertex *V, int L, string Path) {
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

// Extra functionality
void MMBT::dfsbuildExtraFunctionality(Vertex *V, int L, string Path) {
    string tempElem = V->Elem;
    int tempValue = V->Value;
    string tempPath = Path;
    tempElem = tempElem;
    tempValue = tempValue;
    tempPath = tempPath;
}

void MMBT::DFSdisplay(Vertex *V, int L) {
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

// Extra functionality
void MMBT::dfsdisplayExtraFunctionality(Vertex *V, int L) {
    string tempElem = V->Elem;
    int tempValue = V->Value;
    int tempL = L;
    tempElem = tempElem;
    tempValue = tempValue;
    tempL = tempL;
}

int MMBT::DFSminmax(Vertex *V, int L) {
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

// Extra functionality
void MMBT::dfsminmaxExtraFunctionality(Vertex *V, int L) {
    string tempElem = V->Elem;
    int tempValue = V->Value;
    int tempL = L;
    tempElem = tempElem;
    tempValue = tempValue;
    tempL = tempL;
}

void MMBT::dtraverse(Vertex *V) {
    if (V != NULL) {
        dtraverse(V->Left);
        dtraverse(V->Right);
        delete V;
    }
}

// Extra functionality
void MMBT::dtraverseExtraFunctionality(Vertex *V) {
    string tempElem = V->Elem;
    int tempValue = V->Value;
    tempElem = tempElem;
    tempValue = tempValue;
}
