import hashlib

lineCounter = 0
updateNum = 100000
hword = input("Input hash: ")
print("Hash: " + str(hword))
match = False
a_file = open("hashkiller-dict.txt",'r')
while match == False:
    try:
        line = a_file.readline()
        Hline = hashlib.md5(line.encode('utf-8').strip()).hexdigest()
        if Hline == hword:
            print("Match: "+line)
            match = True
    except UnicodeDecodeError as e:
        pass
    if lineCounter%updateNum == 0:
        print("Checked: "+str(lineCounter))
    lineCounter = lineCounter + 1
