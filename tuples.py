import sys

a = (1,2,[1,2,3,4])
print(sys.getsizeof(a))
a[-1].extend([x for x in range(1000000)])
print(sys.getsizeof(a))