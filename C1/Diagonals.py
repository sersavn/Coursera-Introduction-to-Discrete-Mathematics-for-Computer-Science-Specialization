import numpy as np
import itertools as it

m = np.zeros((3,3))
print(m)


#number 6 equal to /
#numer 9 equal to \

#m[0][0] = 0 or 6 or 9
if m[0][0] = 0:
    (m[1][0] = 6) or (m[1][0] = 9) or (m[0][1] = 6) or (m[0][1] = 9) or
    (m[0][1] = 6 and m[1][0] = 9) #2.2; 2.5; 2.3; 2.6 ; 3.4 ; No need to put 1.1

if m[0][0] = 6:
    (m[1][0] = 6) or (m[0][1] = 6) #3.1; 3.2 No need to put 2.1

if m[0][0] = 9:
    (m[1][0] = 9) or (m[0][1] = 9) or (m[0][1] = 9 and m[1][0] = 9) #3.3; 3.5; No need to put 4.1

#m[0][0] => m[i][j]

#if m[0][0] = 6:
#    m[0][1] = 0 or

#1

#2

#3

m[0][0] = 6
print(m)
m[1][0] = 6
print(m)

'''
for line in m:
    print(line)
    for element in line:
        print(element)
'''

arr = np.arange(6).reshape(2, 3)
print(arr)
print(arr[1][1])
print(arr)
np.place(arr, arr>2, [44, 55])
