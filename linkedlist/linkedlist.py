class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node in the list

class LinkedList:
    def __init__(self):
        self.head = None  # Head of the list (first node)

    def append(self, data):
        """Adds a new node to the end of the linked list."""
        new_node = LinkedListNode(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:  # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node  # Append the new node at the end

    def display(self):
        """Prints the elements of the linked list."""
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        print("Linked List:", " -> ".join(map(str, elements)))

# Example Usage of Linked List
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.display()  # Output: Linked List: 10 -> 20 -> 30