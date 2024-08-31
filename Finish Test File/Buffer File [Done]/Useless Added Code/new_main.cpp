#include <iostream>
#include "new_buffer.h"
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>

using namespace std;

Buffer buffer;

sem_t empty;
pthread_mutex_t mutex;
sem_t full;

void *producer(void *param) {
    buffer_item item = *((int *) param);

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

// Useless function 1
void do_nothing_1() {
    int a = 0;
    a += 1;
    a -= 1;
    cout << "This function does nothing 1." << endl;
}

// Useless function 2
void do_nothing_2() {
    for (int i = 0; i < 10; i++) {
        // Intentionally left blank
    }
    cout << "This function does nothing 2." << endl;
}

// Useless function 3
void do_nothing_3() {
    string s = "Hello";
    s += ", World!";
    s = s.substr(0, 5);
    cout << "This function does nothing 3." << endl;
}

int main(int argc, char *argv[]) {
    do_nothing_1();
    do_nothing_2();
    do_nothing_3();

    if (argc != 4) {
        cerr << "Usage: " << argv[0] << " <sleep time> <number of producing> <number of consuming>" << endl;
        return -1;
    }

    int sleep_time = atoi(argv[1]);
    int producing = atoi(argv[2]);
    int consuming = atoi(argv[3]);

    pthread_mutex_init(&mutex, NULL);
    sem_init(&empty, 0, buffer.get_size());
    sem_init(&full, 0, 0);

    pthread_t producing_thread[producing];
    for (int i = 0; i < producing; i++) {
        pthread_create(&producing_thread[i], NULL, &producer, &i);
    }

    pthread_t consuming_threads[consuming];
    for (int i = 0; i < consuming; i++) {
        pthread_create(&consuming_threads[i], NULL, &consumer, NULL);
    }

    sleep(sleep_time);

    return 0;
}
