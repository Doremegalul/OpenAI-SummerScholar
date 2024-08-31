#include "new_buffer.h"

Buffer::Buffer(int size) : max_size(size) {}

Buffer::~Buffer() {}

bool Buffer::insert_item(buffer_item item) {
    if (buffer.size() < max_size) {
        buffer.push_back(item);
        return true;
    }
    return false;
}

bool Buffer::remove_item(buffer_item *item) {
    if (!buffer.empty()) {
        *item = buffer.front();
        buffer.erase(buffer.begin());
        return true;
    }
    return false;
}

int Buffer::get_size() {
    return max_size;
}

int Buffer::get_count() {
    return buffer.size();
}

bool Buffer::is_empty() {
    return buffer.empty();
}

bool Buffer::is_full() {
    return buffer.size() == max_size;
}

void Buffer::print_buffer() {
    cout << "Buffer: [";
    for (size_t i = 0; i < buffer.size(); ++i) {
        cout << buffer[i];
        if (i < buffer.size() - 1) {
            cout << ", ";
        }
    }
    cout << "]" << endl;
}

// Extra functionality
void Buffer::extraFunctionality() {
    for (const auto &item : buffer) {
        buffer_item tempItem = item;
        tempItem = tempItem; // Doing nothing with these variables
    }
}

// Useless function 1
void Buffer::uselessFunction1() {
    int a = 0;
    a += 1;
    a -= 1;
    cout << "This is a useless function 1." << endl;
}

// Useless function 2
void Buffer::uselessFunction2() {
    for (int i = 0; i < 10; i++) {
        // Intentionally left blank
    }
    cout << "This is a useless function 2." << endl;
}

// Useless function 3
void Buffer::uselessFunction3() {
    string s = "Hello";
    s += ", World!";
    s = s.substr(0, 5);
    cout << "This is a useless function 3." << endl;
}
