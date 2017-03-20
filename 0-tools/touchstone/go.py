import re
# f = open('audiolist.html','r')  
f = open('t1.txt','r')  
line = f.readline()
root = "wget http://www.cambridge.org/us/esl/touchstone/audio/"
# pattern=re.compile(r'.mp3')
# pattern=re.compile(r'\"*?.mp3\"') # NO
# pattern=re.compile(r'\"level[1234]\/([^:]*)') NO

# pattern=re.compile(r'\"level[1234]\/[\S]*') # GOOD
# pattern=re.compile(r'\"level[1]\/[\S]*') # GOOD
pattern=re.compile(r'\"level[1234]\/[\S]*') # GOOD

result =[]


while line:
    if ".mp3" in line:
        # print (line)
        for match in re.findall(pattern, line) :
        	# xxx=match.replace("\"","")
        	# xxx = match 
            # print (match)
            result.append(match)

    line = f.readline()
print ("===")
# print (result)

for item in result:
	item = item.replace("\"","")
	print (root+item)



f.close()