def findClosestValueInBst(tree, target):
    return find_closest_helper(tree, target, tree.value)


def find_closest_helper(tree, target, closest):
    # define base case if tree is empty
    if tree is None:
        return closest
    # taking care of potential closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    # define which tree we will explore
    # left closest nodes are always smaller
    if target < tree.value:
        return find_closest_helper(tree.left, target, closest)
    elif target > tree.value:
        return find_closest_helper(tree.right, target, closest)
    else:
        return closest


def findClosestValueInBstWhile(tree, target):
    return find_closest_helper(tree, target, tree.value)


def find_closest_helper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        # taking care of potential closest
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.Value
        # define which tree we will explore
        # left closest nodes are always smaller
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return currentNode
