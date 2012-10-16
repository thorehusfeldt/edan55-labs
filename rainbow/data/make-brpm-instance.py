# Use like this:
# python make-brpm-instance.py 3 1 | python brpm.py 


import sys

n = int(sys.argv[1])

yes = int(sys.argv[2]) # 0 : no instance, 1: yes instance

print n
# First n-2 vertices connected rainbow to the right half
for i in range(n-2):
    for j in range(n):
        print i, j, j
# Last two vertices: connect rainbow for yes, connect all red (color 0) for no
for i in range(n-2,n): 
    for j in range(n):
        print i, j, (0,j)[yes]
