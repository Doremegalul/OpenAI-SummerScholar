
#pragma once // This directive ensures that this header file is included only once in a compilation unit.

#include "pcb.h"      // Including the header file for the PCB class.
#include "pcbtable.h" // Including the header file for the PCBTable class.

/**
 * @brief A queue of PCB's that are in the READY state to be scheduled to run.
 * It should be a priority queue such that the process with the highest priority can be selected next.
 */
class ReadyQueue {
    private:
    // Using a vector to represent the binary max heap data structure. 
    // This data structure will allow us to create a priority queue where the PCB with the highest priority 
    // will be at the top of the heap.
    // Here a vector is used to simulate a binary max heap, which facilitates the operations of a priority queue.
    std::vector<PCB*> heap;

    // These are helper functions that will be used internally to maintain the heap property during insertions and deletions.
    void heapifyUp(int index);   // This function will help in reordering the heap upwards after an insertion.
    void heapifyDown(int index); // This function will help in reordering the heap downwards after a deletion.


public:
    /**
     * @brief Construct a new ReadyQueue object
     *
     */
    ReadyQueue();

    /**
     * @brief Destructor
     */
    ~ReadyQueue();


    /**
     * @brief Add a PCB representing a process into the ready queue.
     *
     * @param pcbPtr: the pointer to the PCB to be added
     */
	void addPCB(PCB* pcbPtr);

    /**
     * @brief Remove and return the PCB with the highest priority from the queue
     *
     * @return PCB*: the pointer to the PCB with the highest priority
     */
	PCB* removePCB();

    /**
     * @brief Returns the number of elements in the queue.
     *
     * @return int: the number of PCBs in the queue
     */
	int size();

     /**
      * @brief Display the PCBs in the queue.
      */
	void displayAll();

    // Extra functionality
    void extraFunctionality() {
        for (auto pcb : heap) {
            if (pcb) {
                unsigned int tempID = pcb->getID();
                unsigned int tempPriority = pcb->getPriority();
                ProcState tempState = pcb->getState();
                tempID = tempID; // Doing nothing with these variables
                tempPriority = tempPriority; // Still doing nothing
                tempState = tempState; // Yet again, doing nothing
            }
        }
    }
};
