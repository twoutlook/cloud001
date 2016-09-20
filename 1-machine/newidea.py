# intput1="ITEM009.txt"
outputfile="output.txt"

def read_all_lines(filename):
    f1=open(filename)
    lines=f1.readlines()
    f1.close()
    return lines

def make_src():
    # 一次性讀入規格
    colA=read_all_lines('cola.txt')
    colB=read_all_lines('colb.txt')
    colC=read_all_lines('colc.txt')
    colG=read_all_lines('rem.txt')
    
    
    
    
    out0 = ''
    v=0
    for  v1,v2,v3,v4 in zip(colA,colB,colC,colG):
        v += 1
        #
        v1 = v1.rstrip()
        v2 = v2.rstrip()
        v3 = v3.rstrip()
        v3 = v3.replace('|', '.')
        v4 = v4.rstrip()
        v4 = v4.replace('|', '.')
        
        out0 += "{0}|{1}|{2}|{3}\n".format(v1,v2, v3,v4)
    
    
    
    
    
    output =[]
    output.append(out0)
    return output
    # print(lines1)    
    
with open(outputfile,'w') as out:
    for data in make_src():
        # out.write('\n\n\n')
        out.write(data)
    