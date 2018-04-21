def is_even(seq):
    cnt = 0
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                cnt += 1
                changed = True
                print('new seq:', seq)
                print('moved int', seq[i+1])
    if cnt%2 == 0:
        return True, cnt
    else:
        return False, cnt

print(is_even([1, 2, 3, 4, 5, 6, 7, 8, 13, 9, 11, 12, 10, 14, 15, 0]))
