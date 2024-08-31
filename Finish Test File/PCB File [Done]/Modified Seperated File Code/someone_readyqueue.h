#pragma once // This directive ensures that this header file is included only once in a compilation unit.

#include "someone_pcb.h"      // Including the header file for the TaskControlBlock class.
#include "someone_pcbtable.h" // Including the header file for the TaskTable class.

/**
 * @brief A queue of TCBs that are in the READY state to be scheduled to run.
 * It should be a priority queue such that the task with the highest priority can be selected next.
 */
class TaskQueue {
private:
    // Using a vector to represent the binary max heap data structure. 
    // This data structure will allow us to create a priority queue where the TCB with the highest priority 
    // will be at the top of the heap.
    // Here a vector is used to simulate a binary max heap, which facilitates the operations of a priority queue.
    std::vector<TaskControlBlock*> heap;

    // These are helper functions that will be used internally to maintain the heap property during insertions and deletions.
    void heapifyUp(int index);   // This function will help in reordering the heap upwards after an insertion.
    void heapifyDown(int index); // This function will help in reordering the heap downwards after a deletion.

public:
    /**
     * @brief Construct a new TaskQueue object
     *
     */
    TaskQueue();

    /**
     * @brief Destructor
     */
    ~TaskQueue();

    /**
     * @brief Add a TCB representing a task into the ready queue.
     *
     * @param tcbPtr: the pointer to the TCB to be added
     */
    void addTCB(TaskControlBlock* tcbPtr);

    /**
     * @brief Remove and return the TCB with the highest priority from the queue
     *
     * @return TaskControlBlock*: the pointer to the TCB with the highest priority
     */
    TaskControlBlock* removeTCB();

    /**
     * @brief Returns the number of elements in the queue.
     *
     * @return int: the number of TCBs in the queue
     */
    int size();

    /**
     * @brief Display the TCBs in the queue.
     */
    void displayAll();
};
