# usage of reverse() and reversed()
n = [1,2,3]
print n
t = n.reverse()
print n     # n is reversed
print t     # t is nothing
g = n       # g is copy from n
print g

n.reverse()
print n

for i in reversed(n):   # just used for iteration, does not affect n
    print i

print n
n.reverse   # lack of (), there is not any function
print n




[1, 2, 3]
[3, 2, 1]
None
[3, 2, 1]
[1, 2, 3]
3
2
1
[1, 2, 3]
[1, 2, 3]
