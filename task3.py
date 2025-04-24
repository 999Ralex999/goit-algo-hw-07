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

def sum_tree(root):
    """
    Обчислює суму всіх значень у двійковому дереві пошуку або AVL-дереві.

    Args:
        root (TreeNode): Корінь дерева

    Returns:
        int or float: Сума всіх значень у дереві
    """
    if root is None:
        return 0
    return root.value + sum_tree(root.left) + sum_tree(root.right)

if __name__ == "__main__":
    # Структура дерева:
    #         8
    #        / \
    #       3   10
    #      / \    \
    #     1   6    14
    #        / \   /
    #       4   7 13

    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)

    total_sum = sum_tree(root)
    print(f"The sum of all values in the tree is: {total_sum}")  # Очікуємо: 66
