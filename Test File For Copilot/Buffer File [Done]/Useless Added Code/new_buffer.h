#ifndef ASSIGN4_BUFFER_H
#define ASSIGN4_BUFFER_H

#include <vector>
#include <iostream>

typedef int buffer_item;

class Buffer {
private:
    std::vector<buffer_item> buffer;
    size_t max_size;

public:
    Buffer(int size = 5) : max_size(size) {}

    ~Buffer() {}

    bool insert_item(buffer_item item) {
        if (buffer.size() < max_size) {
            buffer.push_back(item);
            return true;
        }
        return false;
    }

    bool remove_item(buffer_item *item) {
        if (!buffer.empty()) {
            *item = buffer.front();
            buffer.erase(buffer.begin());
            return true;
        }
        return false;
    }

    int get_size() {
        return max_size;
    }

    int get_count() {
        return buffer.size();
    }

    bool is_empty() {
        return buffer.empty();
    }

    bool is_full() {
        return buffer.size() == max_size;
    }

    void print_buffer() {
        std::cout << "Buffer contents: ";
        for (const auto &item : buffer) {
            std::cout << item << " ";
        }
        std::cout << std::endl;
    }
};

#endif //ASSIGN4_BUFFER_H