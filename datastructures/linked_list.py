class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self, head_value = None):
        self.head = self.tail = Node(head_value)
        self.length = 0

    def prepend(self, value):
        current_head = self.head
        self.head = Node(value)
        self.head.next = current_head
        self.length += 1
        if self.length == 1:
            self.tail = self.head
            self.tail.next = None
        print(self.tail.value, self.head.value)
        print('resulted linked list--->', self.traverse())

    def append(self, value):
        current_node = Node(value)
        print('self tail', self.tail.value, self.tail.next)
        self.tail.next = current_node
        self.tail = current_node
        self.length += 1
        print('resulted linked list--->', self.traverse())

    def traverse(self):
        counter = 1
        linked_list = []
        current_node = self.head
        while (counter <= self.length):
            linked_list.append(current_node.value)
            current_node = current_node.next
            counter += 1
        return linked_list

    def insert_into_index(self, index: int, value):
        if self.length == 0:
            return self.prepend(value)
        if index >= self.length:
            return self.append(value)
        previous_node = self.get_node_by_index(index - 1)
        print('previous_node-->', previous_node.value)
        new_node = Node(value)
        new_node.next = previous_node.next
        previous_node.next = new_node
        self.length += 1
        print('resulted linked list--->', self.traverse())

    def get_node_by_index(self, index: int):
        current_node = self.head
        for i in range(0, index):
            current_node = current_node.next
        return current_node



linked_list_obj = SinglyLinkedList()
linked_list_obj.prepend('A')
linked_list_obj.prepend('B')
# linked_list_obj.prepend('E')
linked_list_obj.append('C')
linked_list_obj.append('D')
linked_list_obj.append('E')
linked_list_obj.insert_into_index(1, 'F')
linked_list_obj.insert_into_index(10, 'end')
linked_list_obj.insert_into_index(7, 'end')