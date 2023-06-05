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
        assert str(ll) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"
