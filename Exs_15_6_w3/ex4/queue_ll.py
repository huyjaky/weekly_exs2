from node import LinkedList, Node


class Queue(LinkedList):
    def __init__(self, capacity):
        self.count = capacity
        self.capacity = capacity
        self.front_pointer = None
        self.rear_pointer = None

    def is_empty(self):
        if self.front_pointer is None and self.rear_pointer is None:
            return True
        else:
            return False

    def enqueue(self, data):
        # NOTE: init create new node
        new_node = Node(data)

        if self.front_pointer is None and self.rear_pointer is None:
            self.front_pointer = new_node
            self.rear_pointer = new_node
            return
        else:
            self.front_pointer.next = new_node
            self.rear_pointer = new_node

    def dequeue(self):
        if self.front_pointer and self.rear_pointer is None:
            return
        # NOTE: if both of them point to None its mean just only one node
        # rest on list
        elif self.front_pointer.next is None and self.rear_pointer.next is None:
            self.front_pointer = self.front_pointer.next
            self.rear_pointer = self.rear_pointer.next

        # NOTE: remove node on a head
        node_want_to_remove = self.front_pointer
        self.front_pointer = node_want_to_remove.next
        node_want_to_remove.next = None

    def front(self):
        return self.front_pointer

    def is_full(self):
        head = self.front_pointer
        count = 0
        while head.next is not None:
            head = head.next
            count += 1

        if count == self.capacity:
            return True
        else:
            return False
