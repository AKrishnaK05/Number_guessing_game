class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_balanced_bst(low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    root = Node(mid)

    root.left = build_balanced_bst(low, mid - 1)
    root.right = build_balanced_bst(mid + 1, high)

    return root