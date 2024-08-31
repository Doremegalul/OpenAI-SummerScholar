
#include <iostream>
#include "buffer.h"
#include <unistd.h>

using namespace std;

#include <pthread.h>
#include <semaphore.h>

// global buffer object
Buffer buffer;

sem_t empty;
pthread_mutex_t mutex;
sem_t full;


// Producer thread function
// Implementation of the producer thread
void *producer(void *param) {
    // Each producer insert its own ID into the buffer
    // For example, thread 1 will insert 1, thread 2 will insert 2, and so on.
    buffer_item item = *((int *) param);

    while (true) {
        /* sleep for a random period of time */
        usleep(rand()%1000000);
		
        // Add synchronization code
		sem_wait(&empty);
		pthread_mutex_lock(&mutex);
		
        if (buffer.insert_item(item)) {
            cout << "Producer " << item << ": Inserted item " << item << endl;
            buffer.print_buffer();
        } else {
            cout << "Producer error condition"  << endl;    // shouldn't come here
        }
		pthread_mutex_unlock(&mutex);
        sem_post(&full);
    }
}

// Consumer thread function
// Implementation of the consumer thread
void *consumer(void *param) {
    buffer_item item;

    while (true) {
        /* sleep for a random period of time */
        usleep(rand() % 1000000);
		
        // Add synchronization code
		sem_wait(&full);
        pthread_mutex_lock(&mutex);
		
        if (buffer.remove_item(&item)) {
            cout << "Consumer " << item << ": Removed item " << item << endl;
            buffer.print_buffer();
        } else {
            cout << "Consumer error condition" << endl;    // shouldn't come here
        }
		
		pthread_mutex_unlock(&mutex);
        sem_post(&empty);
    }
}

int main(int argc, char *argv[]) {
    // Main function with command-line arguments.

    // Check if the correct number of arguments is provided.
    if (argc != 4) {
        cerr << "Usage: " << argv[0] << " <sleep time> <number of producing> <number of consuming>" << endl;
        return -1; // Exit with an error if the argument count is incorrect.
    }

    /* 1. Get command line arguments argv[1],argv[2],argv[3] */
    // Convert command-line arguments to integers.
    int sleep_time = atoi(argv[1]); // Sleep time for the main thread.
    int producing = atoi(argv[2]); // Number of producer threads.
    int consuming = atoi(argv[3]); // Number of consumer threads.
    
    /* 2. Initialize buffer and synchronization primitives */
    // Initialize synchronization primitives for thread management.
    pthread_mutex_init(&mutex, NULL); // Initialize mutex.
    sem_init(&empty, 0, buffer.get_size()); // Initialize semaphore for empty slots in the buffer.
    sem_init(&full, 0, 0); // Initialize semaphore for full slots in the buffer.
    
    /* 3. Create producer thread(s). */
    // Create producer threads.
    pthread_t producing_thread[producing]; // Array to hold producer thread identifiers.
    for (int i = 0; i < producing; i++) {
        pthread_create(&producing_thread[i], NULL, &producer, &i); // Create each producer thread.
    }
    
    /* 4. Create consumer thread(s) */
    // Create consumer threads.
    pthread_t consuming_threads[consuming]; // Array to hold consumer thread identifiers.
    for (int i = 0; i < consuming; i++) {
        pthread_create(&consuming_threads[i], NULL, &consumer, NULL); // Create each consumer thread.
    }
    
    /* 5. Main thread sleep */
    sleep(sleep_time); // Main thread sleeps for the specified duration.

    /* 6. Exit */
    return 0; // Exit the program successfully.
}
