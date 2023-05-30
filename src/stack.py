class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    items = []

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if not Stack.items:
            return ""
        else:
            return "\n".join(Stack.items)

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        Stack.items.append(data)
        self.top = Node(data, self.top)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        delete_item = self.top.data
        self.top = self.top.next_node
        return delete_item
