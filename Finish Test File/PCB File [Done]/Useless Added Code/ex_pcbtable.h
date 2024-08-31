

#pragma once

#include "pcb.h"
#include <vector> //Using vector because why not?

/**
 * @brief PCTable is an array of all PCB's in the system
 * 
 */
class PCBTable {
private: 
	unsigned int size; //The table size
	vector<PCB *> PCB_Pointers; //PCB Pointers to the index in the table size?

public:
    /**
     * @brief Construct a new PCBTable object of the given size (number of PCBs)
     *
     * @param size: the capacity of the PCBTable
     */
    PCBTable(int size = 100);

    /**
     * @brief Destroy the PCBTable object. Make sure to delete all the PCBs in the table.
     *
     */
    ~PCBTable(); // Destructor to clean up allocated memory

    /**
     * @brief Get the PCB at index "idx" of the PCBTable.
     *
     * @param idx: the index of the PCB to get
     * @return PCB*: pointer to the PCB at index "idx"
     */
    PCB* getPCB(unsigned int idx); // Method to get a pointer to a PCB object at a given index

    /**
     * @brief Overload of the operator [] that returns the PCB at idx
     *
     * @param idx
     * @return PCB*
     */
    PCB *operator[](unsigned int idx) {
        return getPCB(idx); // Operator overload to allow array-like access to PCB objects
    }

    /**
     * @brief Add a PCB pointer to the PCBTable at index idx.
     *
     * @param pcb: the PCB pointer to add
     * @param idx: the index to add the PCB at
     */
    void addPCB(PCB *pcb, unsigned int idx); // Method to add a PCB pointer to the table at a given index

    /**
     * @brief Add a new PCB to the PCBTable.
     * @param pid Id of the new PCB
     * @param priority Priority of the new PCB
     * @param idx The index of the new PCB in the PCBTable
     */
    void addNewPCB(unsigned int pid, unsigned int priority, unsigned int idx) {
        PCB *pcb = new PCB(pid, priority); // Creating a new PCB object
        addPCB(pcb, idx); // Adding the new PCB object to the table
    }

    // Extra functionality
    void extraFunctionality() {
        for (auto pcb : PCB_Pointers) {
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
