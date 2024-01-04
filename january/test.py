def countlaser(arr):
    prev = 0
    curr = 0
    count = 0

    for i in arr:
        for j in i:
            if j == '1':
                curr+=1
        if curr == 0:
            continue
        count = count + (prev*curr)
        prev = curr
        curr = 0
    return count

bank = ["011001","000000","010100","001000"]
print(countlaser(bank))