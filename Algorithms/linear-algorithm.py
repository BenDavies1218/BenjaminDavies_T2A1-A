def linearSearch(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


# big0 (n) constant time
# writin as bigO(1)


def verify(index):
    if index is not None:
        print("Target found at in index", index)
    else:
        print("Target not found in list")


numbers = range(1, 999999999)
result = linearSearch(numbers, 9998334)
verify(result)
