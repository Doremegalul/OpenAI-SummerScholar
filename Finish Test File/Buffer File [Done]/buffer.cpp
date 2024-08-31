
#include "buffer.h" // Include the header file for the Buffer class.

/**
* @brief Construct a new Buffer object
* @param size the size of the buffer
*/
Buffer::Buffer(int size) : max_size(size) // Constructor initializing the buffer with a maximum size.
{
}

/**
 * @brief Destroy the Buffer object
 */
Buffer::~Buffer() // Destructor for the Buffer class.
{	
}

/**
 * @brief Insert an item into the buffer
 * @param item the item to insert
 * @return true if successful
 * @return false if not successful
 */
bool Buffer::insert_item(buffer_item item) // Method to insert an item into the buffer.
{
	if (buffer.size() < max_size) // Check if buffer is not full.
	{
        buffer.push_back(item); // Insert the item.
        return true; // Return true if insertion is successful.
    }
    return false; // Return false if buffer is full.
}

/**
 * @brief Remove an item from the buffer
 * @param item the item to remove
 * @return true if successful
 * @return false if not successful
 */
bool Buffer::remove_item(buffer_item *item) // Method to remove an item from the buffer.
{
	if (!buffer.empty()) // Check if buffer is not empty.
	{
        *item = buffer.front(); // Get the first item.
        buffer.erase(buffer.begin()); // Remove the first item.
        return true; // Return true if removal is successful.
    }
    return false; // Return false if buffer is empty.
}

/**
 * @brief Get the size of the buffer
 * @return the size of the buffer
 */
int Buffer::get_size() // Method to get the size of the buffer.
{
	return max_size;
}

/**
 * @brief Get the number of items in the buffer
 * @return the number of items in the buffer
 */
int Buffer::get_count() // Method to get the current number of items in the buffer.
{
	return buffer.size();
}

/**
 * @brief Check if the buffer is empty
 * @return true if the buffer is empty, else false
 */
bool Buffer::is_empty() // Method to check if the buffer is empty.
{
	if(buffer.empty()) // Check if the buffer is empty.
	{
		return true; // Return true if empty.
	}
	return false; // Return false if not empty.
}

/**
 * @brief Check if the buffer is full
 * @return true if the buffer is full, else false
 */
bool Buffer::is_full() // Method to check if the buffer is full.
{
	if(buffer.size() == max_size) // Check if the buffer size equals max size.
	{
		return true; // Return true if full.
	}
	return false; // Return false if not full.
}

/**
 * @brief Print the buffer
 */
void Buffer::print_buffer() // Method to print the contents of the buffer.
{
	cout << "Buffer: [";
	for (size_t i = 0; i < buffer.size(); ++i) { // Iterate through the buffer.
        cout << buffer[i]; // Print each item.
        if (i < buffer.size() - 1) { // Check if not the last item.
            cout << ", "; // Print a comma for separation.
        }
    }
    cout << "]" << endl; // Close the buffer print format.
}
