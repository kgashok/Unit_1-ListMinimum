import ast
# Read the values from standard in
instring = input().strip() 
print(instring)
alist = None
try:
	# what if input is in the form of [1, 2, 4, -2]?
	alist = ast.literal_eval(instring)
	assert type(alist) == list 
except:
	# what if input is just simple 1 390 4 -4 4?
	alist = instring.split(' ')
	alist = list(map(int, alist))
	print(alist)

# Typical indexed version
minval = alist[0]
n = 1
while n < len(alist):
	val = alist[n] 
	if val < minval: 
		minval = val
	n += 1

print("The minimum value is {0}".format(minval))

# A more Pythonic version
minval = alist[0]
for val in alist[1:]:
	if val < minval: 
		minval = val

print("The minimum value is {0}".format(minval))
