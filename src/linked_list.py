class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return f"{__class__.__name__}({self.data})"


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)

        self.tail.next_node = new_node
        self.tail = new_node

    def to_list(self) -> list:
        """Возвращает список с данными, содержащимися в односвязном списке LinkedList"""
        data_list = []

        node = self.head
        if node is None:
            return []

        while node:
            data_list.append(node.data)
            node = node.next_node

        return data_list

    def get_data_by_id(self, id_):
        """Возвращает первый найденный в LinkedList словарь с ключом 'id',
            значение которого равно переданному в метод значению"""
        node = self.head
        if node is None:
            return []

        while node:
            try:
                if node.data.get('id') == id_:
                    return node.data
            except AttributeError:
                print("Данные не являются словарем или в словаре нет id")

            node = node.next_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.strip()
