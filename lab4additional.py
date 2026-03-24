class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1


class AVLPriorityQueue:

    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def right_rotate(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, value, priority):
        self.root = self._insert(self.root, value, priority)

    def _insert(self, node, value, priority):

        if not node:
            return Node(value, priority)

        if priority >= node.priority:
            node.left = self._insert(node.left, value, priority)
        else:
            node.right = self._insert(node.right, value, priority)

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and priority >= node.left.priority:
            return self.right_rotate(node)

        if balance < -1 and priority < node.right.priority:
            return self.left_rotate(node)

        if balance > 1 and priority < node.left.priority:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and priority >= node.right.priority:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def get_max(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def pop(self):
        if not self.root:
            return None

        max_node = self.get_max(self.root)
        self.root = self._delete(self.root, max_node.priority)

        return max_node.value, max_node.priority

    def _delete(self, node, priority):

        if not node:
            return node

        if priority > node.priority:
            node.left = self._delete(node.left, priority)

        elif priority < node.priority:
            node.right = self._delete(node.right, priority)

        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self.get_max(node.left)

            node.value = temp.value
            node.priority = temp.priority

            node.left = self._delete(node.left, temp.priority)

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def view(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append((node.value, node.priority))
            self._inorder(node.right, result)


class Ticket:
    def __init__(self, ticket_id, price, ticket_type):
        self.ticket_id = ticket_id
        self.price = price
        self.ticket_type = ticket_type

    def __str__(self):
        return f"ID: {self.ticket_id}, Price: {self.price}, Type: {self.ticket_type}"


class TicketSystem:
    def __init__(self):
        self.queue = AVLPriorityQueue()

    def calculate_priority(self, price, ticket_type):
        if ticket_type.upper() == "VIP":
            return price + 1000
        return price

    def add_ticket(self, ticket_id, price, ticket_type):
        priority = self.calculate_priority(price, ticket_type)
        ticket = Ticket(ticket_id, price, ticket_type)
        self.queue.insert(ticket, priority)

    def book_ticket(self):
        result = self.queue.pop()
        if result is None:
            return "Немає доступних квитків"

        ticket, priority = result
        return f"Заброньовано: {ticket}"

    def show_tickets(self):
        tickets = self.queue.view()
        return [str(ticket[0]) for ticket in tickets]
