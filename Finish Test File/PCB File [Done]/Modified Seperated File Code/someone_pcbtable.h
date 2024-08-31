#pragma once

#include "someone_pcb.h"
#include <vector> // Using vector for dynamic array management

/**
 * @brief TaskTable is an array of all TCBs in the system
 * 
 */
class TaskTable {
private: 
    unsigned int tableSize; // The table size
    vector<TaskControlBlock *> TCB_Pointers; // TCB Pointers to the index in the table size?

public:
    /**
     * @brief Construct a new TaskTable object of the given size (number of TCBs)
     *
     * @param size: the capacity of the TaskTable
     */
    TaskTable(int size = 100);

    /**
     * @brief Destroy the TaskTable object. Make sure to delete all the TCBs in the table.
     *
     */
    ~TaskTable(); // Destructor to clean up allocated memory

    /**
     * @brief Get the TCB at index "idx" of the TaskTable.
     *
     * @param idx: the index of the TCB to get
     * @return TaskControlBlock*: pointer to the TCB at index "idx"
     */
    TaskControlBlock* getTCB(unsigned int idx); // Method to get a pointer to a TCB object at a given index

    /**
     * @brief Overload of the operator [] that returns the TCB at idx
     *
     * @param idx
     * @return TaskControlBlock*
     */
    TaskControlBlock *operator[](unsigned int idx) {
        return getTCB(idx); // Operator overload to allow array-like access to TCB objects
    }

    /**
     * @brief Add a TCB pointer to the TaskTable at index idx.
     *
     * @param tcb: the TCB pointer to add
     * @param idx: the index to add the TCB at
     */
    void addTCB(TaskControlBlock *tcb, unsigned int idx); // Method to add a TCB pointer to the table at a given index

    /**
     * @brief Add a new TCB to the TaskTable.
     * @param taskId Id of the new TCB
     * @param priority Priority of the new TCB
     * @param idx The index of the new TCB in the TaskTable
     */
    void addNewTCB(unsigned int taskId, unsigned int priority, unsigned int idx) {
        TaskControlBlock *tcb = new TaskControlBlock(taskId, priority); // Creating a new TCB object
        addTCB(tcb, idx); // Adding the new TCB object to the table
    }
};
