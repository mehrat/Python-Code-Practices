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
        for i in r:
            print i,
            print ''


sort_by_kth_element(master_list, k)
