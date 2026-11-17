#O(1) = print(n+n+n)

#O(n)
def nTimes(n):
    i = 0
    for i in range(n):
        print(i)
        i = i + 1

#O(n^2)
def nSquared(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

nTimes(10)
nSquared(5)
