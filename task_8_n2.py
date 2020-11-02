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
                table[sum_j_i].append(elements)

    for i in table.keys():
        if len(table[i]) > 1:
            result.append(table[i])
    return result


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    print(find_forths(a))
