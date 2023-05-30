"""Здесь надо написать тесты с использованием unittest для модуля queue."""

import unittest

from src.queue import Queue

queue = Queue()


class TestStack(unittest.TestCase):

    def test_enqueue(self):
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')
        self.assertEqual(queue.tail.next_node, None)

        with self.assertRaises(AttributeError):
            print(queue.tail.next_node.data)

    def test_dequeue(self):
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(queue.dequeue(), 'data3')
        self.assertEqual(queue.dequeue(), None)
