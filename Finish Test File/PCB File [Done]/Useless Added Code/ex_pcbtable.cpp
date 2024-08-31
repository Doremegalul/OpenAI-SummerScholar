

#include "pcbtable.h" // Including the header file that contains the class definition


/**
 * @brief Construct a new PCBTable object of the given size (number of PCBs)
 *
 * @param size: the capacity of the PCBTable
 */
PCBTable::PCBTable(int size) {
   cout << "PCBTable: Creating new PCBTable " << endl;
   PCB_Pointers.resize(size); //Creating or resizing the table so it have all the current elements
}

/**
 * @brief Destroy the PCBTable object. Make sure to delete all the PCBs in the table.
 *
 */
PCBTable::~PCBTable() {

   for(size_t i = 0; i < PCB_Pointers.size(); i++) {
       delete PCB_Pointers[i]; // Deleting each PCB object pointed to by the pointers in the vector
       PCB_Pointers[i] = nullptr; // Setting the pointer to null to avoid dangling pointers
   }
   
}

/**
 * @brief Get the PCB at index "idx" of the PCBTable.
 *
 * @param idx: the index of the PCB to get
 * @return PCB*: pointer to the PCB at index "idx"
 */
PCB* PCBTable::getPCB(unsigned int idx) {
        if (idx >= PCB_Pointers.size()) {
        // Handling the case where the index is out of bounds
        std::cerr << "Index out of bounds in getPCB: " << idx << std::endl;
        return nullptr; // Returning null pointer if the index is out of bounds
        }

    return PCB_Pointers[idx]; // Returning the pointer to the PCB object at the specified index
}

/**
 * @brief Add a PCB pointer to the PCBTable at index idx.
 *
 * @param pcb: the PCB to add
 */
void PCBTable::addPCB(PCB *pcb, unsigned int idx) {
        if (idx >= PCB_Pointers.size()) {
        // Handling the case where the index is out of bounds
        std::cerr << "Index out of bounds in addPCB: " << idx << std::endl;
        return; // Exiting the function without adding the PCB if the index is out of bounds
    }
    
    // Deleting the existing PCB object at the index to prevent memory leaks before adding the new one
    delete PCB_Pointers[idx];
    
    PCB_Pointers[idx] = pcb; // Adding the new PCB object at the specified index
}

/**
 * @brief Extra functionality.
 */
void PCBTable::extraFunctionality() {
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
