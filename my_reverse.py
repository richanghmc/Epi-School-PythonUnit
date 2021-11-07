def my_reverse(l):
    reversedList = []
    index = len(l)-1
    while index >= 0:
        reversedList.append(l[index])
        index += -1
    return reversedList