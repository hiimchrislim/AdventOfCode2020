class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBST(tree):
    return validateBSTHelper(tree, float('-inf'), float('inf'))


def validateBSTHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    return validateBSTHelper(tree.left, minValue, tree.value) and validateBSTHelper(tree.right, tree.value, maxValue)


a = BST(10)

b = BST(5)
c = BST(5)
