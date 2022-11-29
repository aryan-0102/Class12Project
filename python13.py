#numbersorting
def test(strs):
    return ' '.join([x for x in 'one two three four five six seven eight nine'.split() if x in strs])

#output

strs = "six one four one two three"
print("Original string:",strs)
print("Sort numbers based on said strings:")
print(test(strs))
strs = "six one four three two nine eight"
print("\nOriginal string:",strs)
print("Sort numbers based on said strings:")
print(test(strs))
strs = "nine eight seven six five four three two  one"
print("\nOriginal string:",strs)
print("Sort numbers based on said strings:")
print(test(strs))