class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


def reverse_list(head):
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


# Test Case 1
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

head = n1

print("Test Case 1:", end=" ")
head = reverse_list(head)
print_list(head)


# Test Case 2
n4 = Node(5)

head = n4

print("Test Case 2:", end=" ")
head = reverse_list(head)
print_list(head)