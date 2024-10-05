# Create Dict:
G60 = {'Engine': '520d' , 'Color': 'Sapphireblack' , 'EZ':'09/24'}
print(G60)
print(G60['Color']) 

# Add to Dict:
G60['accident'] = 'yes'
print(G60)

# Delete Dict Item 
del G60['Engine']
print(G60)

# Create new Dict:

G21 ={
'Engine':'330d',
'Color': 'Tansanitblue',
'EZ': '05/24',
'xDrive': 'yes'
}
print(G21)

# Print just the keys:
for x in G21:
    print (x)
print ("---------------------------------------------------------------------")

# Print just the values:
for x in G21.values():
    print (x)
print ("---------------------------------------------------------------------")

for key, value in G21.items():
    print(f"\nKey:{key}")
    print(f"\nValue:{value}")

# Sets can't have duplicated values!           
Phones = {'Apple': 'iPhone' , 'Samsung': 'Galaxy' , 'Google':'Pixel', 'Apple':'iPhone'}
# Change List in Set to sort out duplicated values! 
for Phone in set(Phones.values()):
    print (Phone.title())