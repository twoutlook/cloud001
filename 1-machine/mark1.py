# print ("#========== http://stackoverflow.com/questions/275018/how-can-i-remove-chomp-a-newline-in-python")

def read1():
    f1=open('cola.txt')
    lines=f1.readlines()
    f1.close()
    
    i=0
    cola="cola=['',";
    for line in lines:
        # i += 1
        # seq = "{0:02d}".format(i)
        cola += "'" + line.rstrip() + "'," 
    cola += "]"
    print(cola)

def read2():
    f1=open('colb.txt')
    lines=f1.readlines()
    f1.close()
    
    i=0
    cola="colb=['',";
    for line in lines:
        # i += 1
        # seq = "{0:02d}".format(i)
        cola += "'" + line.rstrip() + "'," 
    cola += "]"
    print(cola)
def read3():
    f1=open('colc.txt')
    lines=f1.readlines()
    f1.close()
    
    i=0
    cola="colc=['',";
    for line in lines:
        # i += 1
        # seq = "{0:02d}".format(i)
        cola += "'" + line.rstrip() + "'," 
    cola += "]"
    print(cola)

def read4():
    f1=open('rem.txt')
    lines=f1.readlines()
    f1.close()
    
    i=0
    cola="rem=['',";
    for line in lines:
        i += 1
        # seq = "rem[{0:02d}] = ".format(i)
        # seq = "rem[{0:d}] = ".format(i)
        cola += "'" + line.rstrip() + "'," 
    print(cola)
read1()
read2()
read3()
read4()
