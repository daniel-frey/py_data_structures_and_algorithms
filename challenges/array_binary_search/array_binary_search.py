def binary_search(list, k):
    min_num = 0
    max_num = len(list)-1
    mid = (max_num + min_num)//2

    if not len(list):
        return - 1
    while(list[mid] != k):
        if(min_num > max_num):
            return -1
        elif(list[mid] > k):
            max_num = mid - 1
        elif(list[mid] < k):
            min_num = mid + 1
        mid = (max_num + min_num)//2

    return mid

print(binary_search([1, 2, 3, 4, 5, 6, 7], 3))
