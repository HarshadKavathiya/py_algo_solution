class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next is not None

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count = count + 1
            current = current.get_next()
        return count


class singly_linked_list:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            nodes.append(repr(current))
            current = current.next

        return '[' + ', '.join(nodes) + ']'

    def append(self, data):
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data)

    def revers(self):
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node

    def find(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr


lst = singly_linked_list()
lst.append(55)
lst.append(65465)
lst.append("fdsd")
lst.append("fsdfsdf")
lst.append(42342)
print(lst)

lst.revers()
print(lst)

print(lst.find(55))
print(lst.find("55"))



