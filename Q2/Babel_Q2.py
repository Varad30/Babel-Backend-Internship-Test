# Task to find indices of start and end of string b in string a.

import re 

a=input("Input first String: ") #Taking first string as input.
b=input("Input Second String: ") #Taking second string as input.

indices= [(m.start(),m.end()+len(b)-1) for m in re.finditer('(?={0})'.format(re.escape(b)),a)]

#Checking if the b exists in a
# if exists print otherwise print -1.
if(len(indices)>0):
    for i in indices:
        print(i)
else:
    print(-1)