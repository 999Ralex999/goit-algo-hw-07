class TreeNode:
    def __init__(self, value):
        """
        Ініціалізація вузла дерева.

        Args:
            value (int or float): Значення вузла
        """
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    """
    Вставляє нове значення у двійкове дерево пошуку.

    Args:
        root (TreeNode): Корінь дерева
        value (int or float): Значення для вставки

    Returns:
        TreeNode: Оновлений корінь дерева
    """
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def find_max_value(root):
    """
    Знаходить максимальне значення у двійковому дереві пошуку.

    Args:
        root (TreeNode): Корінь дерева

    Returns:
        int or float: Максимальне значення в дереві
    """
    if root is None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    return current.value

if __name__ == "__main__":
    root = None
    for value in [10, 5, 15, 3, 7, 12, 20]:
        root = insert(root, value)

    print(f"The maximum value in the tree is: {find_max_value(root)}")  # Очікуємо 20
