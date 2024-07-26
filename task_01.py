
"""
Завдання 1
Напишіть алгоритм (функцію), який знаходить найбільше значення у двійковому дереві пошуку 
або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\\t" * level + prefix + str(self.val) + "\\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current

if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    max_val = max_value_node(root)
    print(f"Найбільше значення у двійковому дереві пошуку: {max_val}")