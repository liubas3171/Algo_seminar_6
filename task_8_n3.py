class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return "Node(" + str(self.value) + str(self.next_node) + ")"

    def __repr__(self):
        return "Node(" + str(self.value) + (self.next_node.__repr__()) + ")"


def find_forths(array):
    '''
    :param array: list of numbers
    :return: all 4 elements a, b, c, d, that a + b = c + d.
    '''
    result = []
    table = dict()
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            sum_j_i = array[i] + array[j]
            if sum_j_i not in table:
                table[sum_j_i] = [(array[i], array[j])]
            else:
                elements = (array[i], array[j])
                for k in range(len(table[sum_j_i])):
                    result.append([table[sum_j_i][k], elements])
                table[sum_j_i].append(elements)

    return result


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    print(find_forths(a))
