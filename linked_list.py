import unittest


class Node:

    def __init__(self, item):
        self.val = item
        self.next = None


class LinkedList:

    def __init__(self, item):
        self.head = Node(item)

    def add(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)

    def printll(self):

        cur = self.head
        while cur is not None:
            print(cur.val, end=" ")
            cur = cur.next
        print()

    def search(self, item):

        cur = self.head
        while cur is not None:
            if cur.val == item:
                return True
            cur = cur.next

        return False

    def pop(self):
        cur = self.head
        if not cur.next:
            self.head = None
        else:
            while cur.next.next:
                cur = cur.next
            cur.next = None


class LinkedListTest(unittest.TestCase):

    def test(self):
        ll = LinkedList(3)
        self.assertEqual(ll.head.val, 3)
        ll.add(4)
        self.assertEqual(ll.head.next.val, 4)
        ll.add(5)
        self.assertEqual(ll.head.next.next.val, 5)
        ll.printll()
        result = ll.search(5)
        self.assertTrue(result)

        result = ll.search(6)
        result = ll.search(6)
        self.assertFalse(result)

        ll.add(6)
        result = ll.pop()
        ll.printll()
        result = ll.pop()
        ll.printll()
        result = ll.pop()
        ll.printll()
        result = ll.pop()
        ll.printll()


unittest.main()
