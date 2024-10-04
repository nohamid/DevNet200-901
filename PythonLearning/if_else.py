Auto = "Audi"

if Auto == "Audi":
        print(Auto)
else: 
    print("Das ist das falsche Auto")

BMWs = ['3er', '5er' , '1er', 'iX' , '7er' , '2er' , 'M4' , 'M5']

print ("---------------------------------------------------------------------")

for BMW in BMWs:
      if BMW == "M4":
            print("Uh, we got a M4 in the List!") 
      else:
            print("There is no BMW M4 in the List!")

# More effective: Check if entry is in the List
print('M4' in BMWs)

# Check if Boolean is true or not (with boolen use is true and not ==)
M4inList = ('M4' in BMWs)
iXinList = ('iX' in BMWs)
if M4inList is True:
    print("It is in the List! ;)")
elif iXinList is True: 
    print ("We definetly have the iX in the List")
else:   
    print("nope")