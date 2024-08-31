#include <iostream>
#include <algorithm>
#include "readyqueue.h"

using namespace std;

/**
 * @brief Constructor for the ReadyQueue class.
 */
ReadyQueue::ReadyQueue() {
    // The constructor doesn't have any logic as the vector heap initializes itself to an empty vector.
}

/**
 *@brief Destructor
*/
ReadyQueue::~ReadyQueue() {
    /*for(auto& pcb : heap) {
        delete pcb;
        pcb = nullptr;
    }*/
    // The commented part of the code is for deleting each PCB object in the heap and setting the pointer to nullptr.
    // It's commented because the destructor currently doesn't delete the PCB objects in the heap. 
}

/**
 * @brief Add a PCB representing a process into the ready queue.
 *
 * @param pcbPtr: the pointer to the PCB to be added
 */
void ReadyQueue::addPCB(PCB* pcbPtr) {
        if(!pcbPtr) {
        // Error handling: If the passed PCB pointer is null, it simply returns without doing anything.
        return;
    }

    pcbPtr->setState(ProcState::READY); // Setting the state of the PCB to READY
    heap.push_back(pcbPtr); // Adding the PCB at the end of the heap
    heapifyUp(heap.size() - 1); // Adjusting the heap to maintain the max heap property by moving the recently added node up as necessary
    }
    
/**
 * @brief Remove and return the PCB with the highest priority from the queue
 *
 * @return PCB*: the pointer to the PCB with the highest priority
 */
PCB* ReadyQueue::removePCB() {
    if(heap.empty()) {
        return nullptr; // If the heap is empty, return nullptr
    }
    
    PCB* topPCB = heap[0];  // Getting the PCB object with the highest priority (at the root of the max heap)
    topPCB->setState(ProcState::RUNNING); // Setting its state to RUNNING
    heap[0] = heap.back(); // Moving the last node to the root
    heap.pop_back(); // Removing the last node
    heapifyDown(0); // Adjusting the heap to maintain the max heap property by moving the root node down as necessary

    return topPCB;  // Returning the PCB object with the highest priority
}

/**
 * @brief Returns the number of elements in the queue.
 *
 * @return int: the number of PCBs in the queue
 */
int ReadyQueue::size() {
    // Returning the current size of the queue
    return heap.size();
}

/**
 * @brief Display the PCBs in the queue.
 */
void ReadyQueue::displayAll() {
    // Loop through all PCBs in the queue and call their display function
    cout << "Display Processes in ReadyQueue:" << endl;

    if(heap.empty()) {
        cout << "Heap is empty." << endl; // If the heap is empty, displaying an appropriate message
        return;
    }

    for(const auto& pcb : heap) { // Iterating through all PCB objects in the heap
        if(pcb) {
            pcb->display(); // If the PCB pointer is valid, calling its display function
        } else {
            cout << "pcb pointer is null." << endl; // If the PCB pointer is null, displaying an appropriate message
        }
    }
}

/**
 * @brief Helper function to maintain the max heap property during insertion of a node.
 */
void ReadyQueue::heapifyUp(int index) {
    int parentIndex = (index - 1) / 2;  // Calculating the index of the parent node
    
    // If the node has higher priority than its parent, swapping them and recursively calling heapifyUp on the parent
    if(index > 0 && heap[index]->getPriority() > heap[parentIndex]->getPriority()) {
        swap(heap[index], heap[parentIndex]);
        heapifyUp(parentIndex);
    }
}


/**
 * @brief Helper function to maintain the max heap property during deletion of a node.
 */
void ReadyQueue::heapifyDown(int index) {
    size_t leftChild = 2 * index + 1;  // Calculating the index of the left child
    size_t rightChild = 2 * index + 2; // Calculating the index of the right child
    size_t largest = index; // Assuming the current node is the largest

    // Finding the largest among the current node and its children
    if(leftChild < heap.size() && heap[leftChild]->getPriority() > heap[largest]->getPriority()) {
        largest = leftChild;
    }

    if(rightChild < heap.size() && heap[rightChild]->getPriority() > heap[largest]->getPriority()) {
        largest = rightChild;
    }

    // If a child has higher priority, swapping the current node with the largest child and recursively calling heapifyDown on the child
    if(largest != index) {
        swap(heap[index], heap[largest]);
        heapifyDown(largest);
    }
}

