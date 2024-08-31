#ifndef ASSIGN4_BUFFER_H
#define ASSIGN4_BUFFER_H

#include <vector>
#include <iostream>
using namespace std;

typedef int buffer_item;

class Buffer {
private:
    vector<buffer_item> buffer;
    size_t max_size;

public:
    Buffer(int size = 5);
    ~Buffer();

    bool insert_item(buffer_item item);
    bool remove_item(buffer_item *item);
    int get_size();
    int get_count();
    bool is_empty();
    bool is_full();
    void print_buffer();

    // Extra functionality
    void extraFunctionality() {
        for (const auto &item : buffer) {
            buffer_item tempItem = item;
            tempItem = tempItem; // Doing nothing with these variables
        }
    }

    // Useless function 1
    void uselessFunction1() {
        int a = 0;
        a += 1;
        a -= 1;
        cout << "This is a useless function 1." << endl;
    }

    // Useless function 2
    void uselessFunction2() {
        for (int i = 0; i < 10; i++) {
            // Intentionally left blank
        }
        cout << "This is a useless function 2." << endl;
    }

    // Useless function 3
    void uselessFunction3() {
        string s = "Hello";
        s += ", World!";
        s = s.substr(0, 5);
        cout << "This is a useless function 3." << endl;
    }
};

#endif //ASSIGN4_BUFFER_H
