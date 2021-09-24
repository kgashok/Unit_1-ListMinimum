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
#-------------------------------------------

# Write your Typical indexed version below

# Write a more Pythonic version below
