import hashlib

#Variable were using to count the lines to see how many words have been used for hash comparison.
lineCounter = 0
#Variable set to be used when we want to print out the amount of theoretical passwords we have checked.
updateNum = 100000
#Asks the user the hash that we will be comparing in the dictionary.
hword = input("Input hash: ")
print("Hash: " + str(hword))
#Variable used to stop while loop once we find a match.
match = False
#Below line opens and reads the list of theoretical passwords were are using to compare hashes.
a_file = open("fakepwdlist.txt",'r')
#While loop that loops until we find a match.
while match == False:
    #Try and except statement is for the purpose of "skipping" words that may cause a unicode or runtime error.
    try:
        #reads line on the text file, after one iteration it reads the next. Also stores it into line variable.
        line = a_file.readline()
        #hashes the line and stores it into the Hline variable (Hline = hashed line
        Hline = hashlib.md5(line.encode('utf-8').strip()).hexdigest()
        #If statement to compare the Hashed Line to the Hashed Word. If there is a match we print "Match: " with the line (theoretical password)
        #and break the loop.
        if Hline == hword:
            print("Match: "+line)
            match = True
    #Except Statement to skipp over the Unicode error.
    except UnicodeDecodeError as e:
        pass
    #Updates with the amount of lines in the file that have already been checked.
    if lineCounter%updateNum == 0:
        print("Checked: "+str(lineCounter))
    #Used to track how many lines have already been checked in the file.
    lineCounter = lineCounter + 1
