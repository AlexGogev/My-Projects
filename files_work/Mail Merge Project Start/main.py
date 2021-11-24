#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_to_send = []


with open("files_work\\Mail Merge Project Start\\Input\\Names\\invited_names.txt", "r") as names:
    for i in names.readlines():
        names_to_send.append(i)

names = []
for i in names_to_send:
    if "\n" in i:
        names.append(i[0:-1])
 
#print(names)

PLACE_HOLDER = "[name]"

with open("files_work\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    print(letter_content)
    for name in names:
        new_letter = letter_content.replace(PLACE_HOLDER, name)
        with open(f"files_work\\Mail Merge Project Start\\Output\\ReadyToSend\\To {name}.txt", "w") as send_to:
            send_to.write(new_letter)