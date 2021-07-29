#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

start_letter = open("Input/Letters/starting_letter.docx")
letter=start_letter.read()
k=0
# with open("Input/Names/invited_names.txt",mode='w') as names:
names=open("Input/Names/invited_names.txt")
print (names)
line=names.readlines()
# print(line)
for name in line:
    if name != line[len(line)-1]:
        k = letter.replace("[name]",name[0:len(name)-2])
    else:
        k = letter.replace("[name]",name)

    print(k)
    with open("lice.txt",mode='a') as scriere:
        scriere.write(k)
        scriere.write('\n')
start_letter.close()
names.close()