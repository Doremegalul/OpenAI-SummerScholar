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
    std::cout << "Buffer: [";
    for (size_t i = 0; i < buffer.size(); ++i) {
        std::cout << buffer[i];
        if (i < buffer.size() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;
}