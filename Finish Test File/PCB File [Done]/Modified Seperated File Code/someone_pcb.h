#pragma once
#include <iostream>
using namespace std;

// Enum class of task status
// A task (TaskControlBlock) in ready queue should be in READY status
enum class TaskStatus {NEW, READY, RUNNING, WAITING, TERMINATED};

/**
 * @brief A Task Control Block (TCB) Task Control Block (TCB) is a data structure representing a task in the system.
   A task should have at least an ID and a status (i.e. NEW, READY, RUNNING, WAITING, or TERMINATED).
   It may also have other attributes, such as scheduling information (e.g. priority)
 *
 */
class TaskControlBlock {
public:
    // The unique task ID
    unsigned int taskID;
    // The priority of a task valued between 1-50. Larger number represents higher priority
    unsigned int taskPriority;
    // The current status of the task.
    // A task in the ReadyQueue should be in READY status
    TaskStatus taskStatus;

    /**
     * @brief Construct a new TaskControlBlock object
     * @param taskID: each task has a unique ID
     * @param taskPriority: the priority of the task in the range 1-50. Larger number represents higher priority
     * @param taskStatus the status of the task.
     */
    TaskControlBlock(unsigned int taskID = 0, unsigned int taskPriority = 1, TaskStatus taskStatus = TaskStatus::NEW) {
        this->taskID = taskID;
        this->taskPriority = taskPriority;
        this->taskStatus = taskStatus;
    }

    /**
     * @brief Destroy the TaskControlBlock object.
     *
     */
    ~TaskControlBlock() {}

    /**
     * @brief Get the ID of the TaskControlBlock.
     *
     * @return unsigned int: the ID of the TaskControlBlock
     */
    unsigned int getTaskID() {
        return taskID;
    }

    /**
     * @brief Get the priority of the TaskControlBlock.
     *
     * @return unsigned int: the priority of the TaskControlBlock
     */
    unsigned int getTaskPriority() {
        return taskPriority;
    }

    /**
     * @brief Get the status of the TaskControlBlock.
     *
     * @return TaskStatus: the status of the TaskControlBlock
     */
    TaskStatus getTaskStatus() {
        return taskStatus;
    }

    /**
     * @brief Change the status of the TaskControlBlock.
     * @param taskStatus			
     */
	 // TODO
    void setTaskStatus(TaskStatus taskStatus) {
        this->taskStatus = taskStatus;
    }

    /**
     * @brief Change the priority of the TaskControlBlock.
     * @param taskPriority
     */
	 // TODO
    void setTaskPriority(unsigned int taskPriority) {
        this->taskPriority = taskPriority;
    }

    /**
     * @brief Print the TaskControlBlock.
     *
     */
    void display() const {
        cout << "Task ID: " << taskID;
        cout << ", Priority: " << taskPriority;
        cout << ", Status: " ;
        switch(taskStatus) {
            case TaskStatus::NEW:
                cout << "NEW";
                break;
            case TaskStatus::READY:
                cout << "READY";
                break;
            case TaskStatus::RUNNING:
                cout << "RUNNING";
                break;
            case TaskStatus::WAITING:
                cout << "WAITING";
                break;
            case TaskStatus::TERMINATED:
                cout << "TERMINATED";
                break;
        } 
        cout << endl;
    }
};
