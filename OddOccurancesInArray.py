# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(arr, arr_size):

    for i in range(0,arr_size):
        count = 0
        for j in range(0, arr_size):
            if arr[i] == arr[j]:
                count+=1

        if (count % 2 != 0):
            return arr[i]

    return
