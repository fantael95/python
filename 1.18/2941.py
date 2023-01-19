string = input()
A = ['c=', 'c-', 'dz=','d-','lj','nj','s=','z=']
for i in A:
    if  i in string:
        string = string.replace( i , 'a')        
print(len(string))
