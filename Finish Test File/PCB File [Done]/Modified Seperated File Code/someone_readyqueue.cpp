#include <iostream>
#include <algorithm>
#include "someone_readyqueue.h"

using namespace std;

/**
 * @brief Constructor for the TaskQueue class.
 */
TaskQueue::TaskQueue() {
    // The constructor doesn't have any logic as the vector heap initializes itself to an empty vector.
}

/**
 *@brief Destructor
 */
TaskQueue::~TaskQueue() {
    /*for(auto& tcb : heap) {
        delete tcb;
        tcb = nullptr;
    }*/
    // The commented part of the code is for deleting each TCB object in the heap and setting the pointer to nullptr.
    // It's commented because the destructor currently doesn't delete the TCB objects in the heap.
}

/**
 * @brief Add a TCB representing a task into the ready queue.
 *
 * @param tcbPtr: the pointer to the TCB to be added
 */
void TaskQueue::addTCB(TaskControlBlock* tcbPtr) {
    if (!tcbPtr) {
        // Error handling: If the passed TCB pointer is null, it simply returns without doing anything.
        return;
    }

    tcbPtr->setTaskStatus(TaskStatus::READY); // Setting the status of the TCB to READY
    heap.push_back(tcbPtr); // Adding the TCB at the end of the heap
    heapifyUp(heap.size() - 1); // Adjusting the heap to maintain the max heap property by moving the recently added node up as necessary
}

/**
 * @brief Remove and return the TCB with the highest priority from the queue
 *
 * @return TaskControlBlock*: the pointer to the TCB with the highest priority
 */
TaskControlBlock* TaskQueue::removeTCB() {
    if (heap.empty()) {
        return nullptr; // If the heap is empty, return nullptr
    }

    TaskControlBlock* topTCB = heap[0];  // Getting the TCB object with the highest priority (at the root of the max heap)
    topTCB->setTaskStatus(TaskStatus::RUNNING); // Setting its status to RUNNING
    heap[0] = heap.back(); // Moving the last node to the root
    heap.pop_back(); // Removing the last node
    heapifyDown(0); // Adjusting the heap to maintain the max heap property by moving the root node down as necessary

    return topTCB;  // Returning the TCB object with the highest priority
}

/**
 * @brief Returns the number of elements in the queue.
 *
 * @return int: the number of TCBs in the queue
 */
int TaskQueue::size() {
    // Returning the current size of the queue
    return heap.size();
}

/**
 * @brief Display the TCBs in the queue.
 */
void TaskQueue::displayAll() {
    // Loop through all TCBs in the queue and call their display function
    cout << "Display Tasks in TaskQueue:" << endl;

    if (heap.empty()) {
        cout << "Heap is empty." << endl; // If the heap is empty, displaying an appropriate message
        return;
    }

    for (const auto& tcb : heap) { // Iterating through all TCB objects in the heap
        if (tcb) {
            tcb->display(); // If the TCB pointer is valid, calling its display function
        } else {
            cout << "TCB pointer is null." << endl; // If the TCB pointer is null, displaying an appropriate message
        }
    }
}

/**
 * @brief Helper function to maintain the max heap property during insertion of a node.
 */
void TaskQueue::heapifyUp(int index) {
    int parentIndex = (index - 1) / 2;  // Calculating the index of the parent node

    // If the node has higher priority than its parent, swapping them and recursively calling heapifyUp on the parent
    if (index > 0 && heap[index]->getTaskPriority() > heap[parentIndex]->getTaskPriority()) {
        swap(heap[index], heap[parentIndex]);
        heapifyUp(parentIndex);
    }
}

/**
 * @brief Helper function to maintain the max heap property during deletion of a node.
 */
void TaskQueue::heapifyDown(int index) {
    size_t leftChild = 2 * index + 1;  // Calculating the index of the left child
    size_t rightChild = 2 * index + 2; // Calculating the index of the right child
    size_t largest = index; // Assuming the current node is the largest

    // Finding the largest among the current node and its children
    if (leftChild < heap.size() && heap[leftChild]->getTaskPriority() > heap[largest]->getTaskPriority()) {
        largest = leftChild;
    }

    if (rightChild < heap.size() && heap[rightChild]->getTaskPriority() > heap[largest]->getTaskPriority()) {
        largest = rightChild;
    }

    // If a child has higher priority, swapping the current node with the largest child and recursively calling heapifyDown on the child
    if (largest != index) {
        swap(heap[index], heap[largest]);
        heapifyDown(largest);
    }
}
