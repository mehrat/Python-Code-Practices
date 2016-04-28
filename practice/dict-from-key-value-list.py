# lis = [{1:["Hey"]},{2:["Hello"]}]
#
# new_dict = dict()
# for l in lis:
#     new_dict[l[0]] = l[1]
#
# print new_dict
from collections import defaultdict

err = [{"field": ["This field is required."]}, {"field": ["This field is required."]}]

results = defaultdict()
for dict in err:
    for error in dict.keys():
        results[str(err.index(dict))] = dict[error]

print results
