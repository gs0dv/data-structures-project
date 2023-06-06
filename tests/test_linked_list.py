"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest

from src.linked_list import LinkedList, Node


class TestLinkedList(unittest.TestCase):

    def test_Node(self):
        node = Node({'id': 1})
        self.assertEqual(node.data, {'id': 1})
        self.assertEqual(node.next_node, None)
        self.assertEqual(repr(node), "Node({'id': 1})")

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.head.next_node, None)
        self.assertEqual(ll.tail.data, {'id': 1})
        self.assertEqual(ll.tail.next_node, None)
        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.head.data, {'id': 0})
        self.assertEqual(ll.head.next_node.data, {'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        lst = ll.to_list()
        self.assertEqual(lst[0], {'id': 0, 'username': 'serebro'})
        self.assertEqual(lst[3], {'id': 3, 'username': 'mosh_s'})

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        user_data = ll.get_data_by_id(3)
        self.assertEqual(user_data, {'id': 3, 'username': 'mosh_s'})

    def test_get_data_by_id__AttributeError(self):
        ll = LinkedList()
        ll.insert_beginning([1, 2, 3])
        self.assertEqual(ll.get_data_by_id(1), None)
