class Node():

    def __repr__(self) -> str:
        return f"Node(data={self.data}), next={self.next}"

    def __init__(self, data) -> None:
        self.next = None
        self.data = data


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def printOut(self) -> str:
        node = self.head
        res = ""
        while node:
            res += str(node.data) + " -> "
            node = node.next
        return res + "None"

    def insert(self, new_node, tail=None) -> None:
        if not self.head:
            self.head = new_node
            return new_node
        node = self.head
        if not tail:
            while node:
                if not node.next:
                    node.next = new_node
                    return new_node
                node = node.next
        else:
            tail.next = new_node
            return new_node

    def insertBehind(self, new_node, behind) -> None:
        node = self.head
        while node:
            if node.data == behind:
                new_node.next = node.next
                node.next = new_node
            node = node.next

    def remove(self, value) -> None:
        prevNode = None
        if not self.head:
            return -1
        node = self.head

        while node:
            if node.data == value:
                if prevNode:
                    prevNode.next = node.next
                else:
                    self.head = node.next
                return 1
            prevNode = node
            node = node.next

    def reverse(self) -> None:
        prev = None
        node = self.head
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        self.head = prev


# Creating Linked List
MyList = LinkedList()
# Nodes to Insert
n1, n2, n3 = Node(4), Node(6), Node(8)

# O(1) Inserting
a = MyList.insert(n1)
a = MyList.insert(n2, a)
a = MyList.insert(n3, a)

# Inserting without "insert" function
# MyList.head = n1
# n1.next = n2
# n2.next = n3
print(MyList.printOut())
MyList.reverse()
print(MyList.printOut())