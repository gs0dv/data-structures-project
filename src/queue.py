class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    items = []

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if not Queue.items:
            return ""
        else:
            return "\n".join(Queue.items)

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        self.items.append(data)
        new_data = Node(data, None)

        if not self.head:
            self.head = new_data
            self.tail = self.head
        else:
            self.tail.next_node = new_data
            self.tail = new_data

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            self.tail = None
            return

        data = self.head.data
        self.head = self.head.next_node
        return data
