numb = [2, 4, 5, 8, 9]
no = len(numb)
numb.sort()
if no % 2 == 0:
    median1 = numb[no//2]
    median2 = numb[no//2 - 1]
    median = (median1 + median2)/2
else:
    median = numb[no//2]
print("The median of the given numbers  (", numb, ") is", str(median))