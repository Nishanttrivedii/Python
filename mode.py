from collections import Counter
numb = [2, 3, 4, 5, 7, 2]
no = len(numb)
val = Counter(numb)
findMode = dict(val)
mode = [i for i, v in findMode.items() if v == max(list(val.values()))]  
if len(mode) == no:
    findMode = "The group of number do not have any mode"
else:
    findMode = "The mode of a number is / are: " + ', '.join(map(str, mode))
print(findMode)