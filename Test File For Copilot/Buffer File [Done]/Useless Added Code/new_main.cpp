// File: main.cpp
#include <iostream>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>
#include "new_buffer.h" 

using namespace std;

// Global synchronization primitives
sem_t empty;
pthread_mutex_t mutex;
sem_t full;

// Function prototypes
void *producer(void *param);
void *consumer(void *param);
void initializeSynchronizationPrimitives(int bufferSize);
void createThreads(int producing, int consuming, int sleepTime);

int main(int argc, char *argv[]) {
    if (argc != 4) {
        cerr << "Usage: " << argv[0] << " <sleep time> <number of producers> <number of consumers>" << endl;
        return -1;
    }

    int sleepTime = atoi(argv[1]);
    int producing = atoi(argv[2]);
    int consuming = atoi(argv[3]);

    Buffer buffer; // Instance of Buffer
    initializeSynchronizationPrimitives(buffer.get_size());
    createThreads(producing, consuming, sleepTime);

    return 0;
}

void initializeSynchronizationPrimitives(int bufferSize) {
    pthread_mutex_init(&mutex, NULL);
    sem_init(&empty, 0, bufferSize);
    sem_init(&full, 0, 0);
}

void createThreads(int producing, int consuming, int sleepTime) {
    pthread_t producingThreads[producing];
    for (int i = 0; i < producing; i++) {
        pthread_create(&producingThreads[i], NULL, producer, (void*)(intptr_t)i);
    }

    pthread_t consumingThreads[consuming];
    for (int i = 0; i < consuming; i++) {
        pthread_create(&consumingThreads[i], NULL, consumer, NULL);
    }

    sleep(sleepTime);
}

// File: producer_consumer.cpp
#include "buffer.h"
#include <iostream>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>

extern sem_t empty;
extern pthread_mutex_t mutex;
extern sem_t full;
extern Buffer buffer;

void *producer(void *param) {
    int item = (int)(intptr_t)param;

    while (true) {
        usleep(rand() % 1000000);

        sem_wait(&empty);
        pthread_mutex_lock(&mutex);

        if (buffer.insert_item(item)) {
            cout << "Producer " << item << ": Inserted item " << item << endl;
            buffer.print_buffer();
        } else {
            cout << "Producer error condition" << endl;
        }

        pthread_mutex_unlock(&mutex);
        sem_post(&full);
    }
}

void *consumer(void *param) {
    buffer_item item;

    while (true) {
        usleep(rand() % 1000000);

        sem_wait(&full);
        pthread_mutex_lock(&mutex);

        if (buffer.remove_item(&item)) {
            cout << "Consumer " << item << ": Removed item " << item << endl;
            buffer.print_buffer();
        } else {
            cout << "Consumer error condition" << endl;
        }

        pthread_mutex_unlock(&mutex);
        sem_post(&empty);
    }
}