import os

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.__value = value
        self.__left = left
        self.__right = right

    @property
    def value(self): return self.__value
    @value.setter
    def value(self, val): self.__value = val

    @property
    def left(self): return self.__left
    @left.setter
    def left(self, node): self.__left = node

    @property
    def right(self): return self.__right
    @right.setter
    def right(self, node): self.__right = node


    def print_preorder(self):
        print(self.value, end=" ")
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(self.value, end=" ")
        if self.right:
            self.right.print_inorder()

    @staticmethod
    def create_tree_file(filename):
        tree_data = "1 2 3 4 5 6 None None None None None 8 7 None 10 9 None None None None"
        with open(filename, "w") as f:
            f.write(tree_data)
        print(f" Файл '{filename}' створено.")

    @staticmethod
    def build_from_file(filename):
        if not os.path.exists(filename):
            BinaryTree.create_tree_file(filename)

        with open(filename, "r") as f:
            values = f.read().split()

        nodes = []
        for v in values:
            if v.lower() == "none":
                nodes.append(None)
            else:
                nodes.append(BinaryTree(int(v)))

        child_index = 1
        for i in range(len(nodes)):
            if nodes[i] is not None:
                if child_index < len(nodes):
                    nodes[i].left = nodes[child_index]
                    child_index += 1
                if child_index < len(nodes):
                    nodes[i].right = nodes[child_index]
                    child_index += 1
        return nodes[0] if nodes else None

    def get_height(self):
        left_h = self.left.get_height() if self.left else 0
        right_h = self.right.get_height() if self.right else 0
        return 1 + max(left_h, right_h)

    def print_horizontal(self):
        height = self.get_height()
        half = (1 << (height - 1)) - 1
        num_rows = 2 * half + 1
        num_cols = 2 * height - 1
        CW = 5
        node_grid = [[""] * num_cols for _ in range(num_rows)]
        connections = []
        root_row, root_col = half, height - 1
        node_grid[root_row][root_col] = str(self.value)

        def place_left(node, col, center_row, pr, pc):
            if node is None: return
            node_grid[center_row][col] = str(node.value)
            connections.append((pr, pc, center_row, col))
            if col == 0: return
            gap = 1 << (col - 1)
            place_left(node.left, col - 1, center_row - gap, center_row, col)
            place_left(node.right, col - 1, center_row + gap, center_row, col)

        def place_right(node, col, center_row, pr, pc):
            if node is None: return
            node_grid[center_row][col] = str(node.value)
            connections.append((pr, pc, center_row, col))
            if col == num_cols - 1: return
            gap = 1 << (num_cols - col - 2)
            place_right(node.left, col + 1, center_row - gap, center_row, col)
            place_right(node.right, col + 1, center_row + gap, center_row, col)

        if self.left: place_left(self.left, root_col - 1, root_row, root_row, root_col)
        if self.right: place_right(self.right, root_col + 1, root_row, root_row, root_col)

        W = num_cols * CW
        canvas = [[" "] * W for _ in range(num_rows * 2 - 1)]

        for r in range(num_rows):
            for c in range(num_cols):
                val = node_grid[r][c]
                if val:
                    cr, x = r * 2, (c * CW + CW // 2) - len(val) // 2
                    for i, ch in enumerate(val):
                        if 0 <= x + i < W: canvas[cr][x + i] = ch

        for (pr, pc, cr_log, cc) in connections:
            px, chx = pc * CW + CW // 2, cc * CW + CW // 2
            p_canvas, c_canvas = pr * 2, cr_log * 2
            if pr == cr_log:
                x0, x1 = (px + 1, chx - 1) if px < chx else (chx + 1, px - 1)
                for x in range(x0, x1 + 1):
                    if 0 <= x < W: canvas[p_canvas][x] = "─"
            else:
                conn_row = (p_canvas + c_canvas) // 2
                diag = "\\" if (cc < pc and cr_log < pr) or (cc > pc and cr_log > pr) else "/"
                if 0 <= conn_row < len(canvas): canvas[conn_row][chx] = diag

        for row in canvas:
            line = "".join(row).rstrip()
            if line.strip(): print(line)

filename = "tree.txt"
my_tree = BinaryTree.build_from_file(filename)
