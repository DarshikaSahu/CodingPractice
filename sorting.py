def sort(num_arr):
    length_arr = len(num_arr)
    for index in range(0, length_arr):
        for index2 in range(0, length_arr - index -1):
            if num_arr[index2] > num_arr[index2 + 1]:
                temp = num_arr[index2]
                num_arr[index2] = num_arr[index2 + 1]
                num_arr[index2 + 1] = temp
    return num_arr

print(sort([12,1,34,67,12]))
