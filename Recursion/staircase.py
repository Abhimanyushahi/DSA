def num_way(num):
    if num ==1:
        return 1
    if num == 2:
        return 2
    if num ==3:
        return 4
    else:
        return num_way(num-1)+num_way(num-2)+num_way(num-3)

num=int(input())
print(num_way(num))
