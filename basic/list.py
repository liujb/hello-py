#FileName:list.py

lst = ['Allen','JiangBei'] # Init a list
lst.append('BBB') # Add a new item to list
print 'The length of list is', len(lst) # Length
for item in lst:
    print item, '\t' # Output the list
print lst # Direct output the list

del lst[0] # Delete a item from list
lst.sort() # Sort the list
print lst
