#
import copy
def convrt(lol):
    ll =copy.deepcopy(listOfList)
    for a in ll:
        if a[0]=='2':
            a[1]='Changed'
            break;
    return ll


listOfList = [['1','One'],['2','Two'],['3','Three']]
print listOfList

print convrt(listOfList)

print listOfList