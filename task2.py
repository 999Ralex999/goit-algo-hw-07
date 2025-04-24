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

def find_min_value(root):
    """
    Знаходить найменше значення у двійковому дереві пошуку або AVL-дереві.

    Args:
        root (TreeNode): Корінь дерева

    Returns:
        int or float: Найменше значення в дереві або None, якщо дерево порожнє
    """
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left

    return current.value

if __name__ == "__main__":
    # Cтруктура дерева:
    #         50
    #        /  \
    #      25    75
    #     /     /  \
    #    10    60   80
    #   /
    #  5
    root = TreeNode(50)
    root.left = TreeNode(25)
    root.left.left = TreeNode(10)
    root.left.left.left = TreeNode(5)
    root.right = TreeNode(75)
    root.right.left = TreeNode(60)
    root.right.right = TreeNode(80)

    min_value = find_min_value(root)
    print(f"The minimum value in the tree is: {min_value}")  # Очікуємо: 5
