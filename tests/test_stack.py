"""Здесь надо написать тесты с использованием unittest для модуля stack."""

import unittest
from src.stack import Stack, Node

stack = Stack()


class TestStack(unittest.TestCase):

    def test_push(self):
        stack.push('data1')
        self.assertIsInstance(stack.top, Node, True)
        stack.push('data2')
        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.top.next_node.data, 'data1')
        self.assertEqual(stack.top.next_node.next_node, None)

        with self.assertRaises(Exception):
            print(stack.top.next_node.next_node.data)
