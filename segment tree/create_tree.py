# take input of array to create it's corresponding segment tree
import math

def create(arr, seg, low, high, pos):
    # print(low, high, pos)
    if low == high:
        seg[pos] = arr[low]
        return
    mid = int(math.floor((low + high) / 2))
    # print(mid)
    # mid = mid if mid==int(mid) else int(mid) + 1
    # print("create 1")
    create(arr, seg, low, mid, int((2 * pos) + 1))
    # print("create 2")
    create(arr, seg, mid + 1, high, int((2 * pos) + 2))
    seg[pos] = min(seg[(2 * pos) + 1], seg[(2 * pos) + 2])

def pow(n):
    bin_count = bin(n).count("1")
    len = bin(n).__len__() - 2
    if bin_count == 1:
        print(bin(n), n, len, 2**(len-1))
        return (2**(len-1))*2
    else:
        print(bin(n), n, len, 2**(len-1))
        return  (2**(len))*2

arr = list(map(int, input().split()))
print(arr.__len__())
print(pow(arr.__len__()))
seg = [None] * (pow(arr.__len__()) -1 )
print(seg.__len__())
low, high, pos = 0, arr.__len__() - 1, 0

create(arr, seg, low, high, pos)
print(seg)