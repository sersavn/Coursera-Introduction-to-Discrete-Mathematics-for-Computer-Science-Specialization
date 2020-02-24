import itertools as it

def is_solution(perm):
    for (i1, i2) in it.combinations(range(len(perm)), 2):
        print("is solution perm i1, i2 ", i1, i2)
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False
            print('False')
    print('True')
    return True

for perm in it.permutations(range(8)):
    print("it perm range 8", perm)
    if is_solution(perm):
        print(perm)
        exit()
