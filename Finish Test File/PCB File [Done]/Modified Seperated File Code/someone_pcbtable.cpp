#include "someone_pcbtable.h" // Including the header file that contains the class definition

/**
 * @brief Construct a new TaskTable object of the given size (number of TCBs)
 *
 * @param size: the capacity of the TaskTable
 */
TaskTable::TaskTable(int size) {
    cout << "TaskTable: Creating new TaskTable " << endl;
    TCB_Pointers.resize(size); // Creating or resizing the table so it has all the current elements
}

/**
 * @brief Destroy the TaskTable object. Make sure to delete all the TCBs in the table.
 *
 */
TaskTable::~TaskTable() {
    for (size_t i = 0; i < TCB_Pointers.size(); i++) {
        delete TCB_Pointers[i]; // Deleting each TCB object pointed to by the pointers in the vector
        TCB_Pointers[i] = nullptr; // Setting the pointer to null to avoid dangling pointers
    }
}

/**
 * @brief Get the TCB at index "idx" of the TaskTable.
 *
 * @param idx: the index of the TCB to get
 * @return TaskControlBlock*: pointer to the TCB at index "idx"
 */
TaskControlBlock* TaskTable::getTCB(unsigned int idx) {
    if (idx >= TCB_Pointers.size()) {
        // Handling the case where the index is out of bounds
        std::cerr << "Index out of bounds in getTCB: " << idx << std::endl;
        return nullptr; // Returning null pointer if the index is out of bounds
    }

    return TCB_Pointers[idx]; // Returning the pointer to the TCB object at the specified index
}

/**
 * @brief Add a TCB pointer to the TaskTable at index idx.
 *
 * @param tcb: the TCB to add
 */
void TaskTable::addTCB(TaskControlBlock *tcb, unsigned int idx) {
    if (idx >= TCB_Pointers.size()) {
        // Handling the case where the index is out of bounds
        std::cerr << "Index out of bounds in addTCB: " << idx << std::endl;
        return; // Exiting the function without adding the TCB if the index is out of bounds
    }

    // Deleting the existing TCB object at the index to prevent memory leaks before adding the new one
    delete TCB_Pointers[idx];

    TCB_Pointers[idx] = tcb; // Adding the new TCB object at the specified index
}
