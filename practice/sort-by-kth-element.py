import sys
from numbers import Number

nm = list(map(int, raw_input().split()))

master_list = list()

for i in range(nm[0]):
    lis = list(map(int, raw_input().split()))
    master_list.append(lis)

k = int(sys.stdin.readline())


def sort_by_kth_element(master_list, k):
    for r in sorted(master_list, key=lambda x:x[k]):
        for i in r[:-1]:
            print i,
    print r[-1]


sort_by_kth_element(master_list, k)
