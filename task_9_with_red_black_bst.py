from red_black_tree import RedBlackTree


# O(n*(logn + logn + logn)) = O(nlogn)
def find_left_max(array):
    result = []
    r_b_bst = RedBlackTree()
    r_b_bst.insert(array[0])
    result.append(-1)
    for i in range(1, len(array)):
        # O(logn)
        r_b_bst.insert(array[i])
        # O(logn)
        our_node = r_b_bst.searchTree(array[i])
        # O(logn)
        res = r_b_bst.predecessor(our_node)
        result.append(res.data) if res else result.append(-1)
    return result


if __name__ == '__main__':
    # a = [2, 3, 4, 5, 1, ]
    #  [-1, 2, 3, 4, -1]
    a = [2, 6, 9, 8, 3, 1]
    print(find_left_max(a))
