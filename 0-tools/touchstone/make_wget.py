f = open('audiolist.html','r')  
## Open the file with read only permit

line = f.readline()

## If the file is not empty keep reading line one at a time
## till the file is empty
while line:
    print (line)
    line = f.readline()
f.close()