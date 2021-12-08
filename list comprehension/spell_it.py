nato = "Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango Uniform Victor Whiskey X-Ray Yankee Zulu"

nato_list = nato.split()



user = input("Spell it: ").upper()
user_list = []


spelled = []
def spell():
    for i in user:
        for b in nato_list:
            if i == b[0]:
                spelled.append(b)


#print(user_list)
spell()
spelled = ", ".join(spelled)
print(spelled)