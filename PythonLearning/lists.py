Apple = ['iPhone', 'iPad', 'MacBook', 'Apple Watch', 'AirPods',]
print(Apple[0])
print(Apple[1])
print(Apple[2])
print(Apple[3])
print(Apple[4])

print ("-----------------------")

# Mit negativen Zahlen wird die Liste von hinten abgefragt 

print(Apple[-1])
print(Apple[-2])
print(Apple[-3])
print(Apple[-4])
print(Apple[-5])

print ("-----------------------")

message = f"My favorite product is {Apple[2]}"
print(message)

# Change the List 
Apple[4] = 'Apple TV'
print (Apple)

print ("-----------------------")

# Append, hinzufuegen : 
Audi = ['A1', 'A3', 'A4', 'A5', 'A6' , 'A7']
print(Audi)
Audi.append('A8')
print(Audi)

# Insert something on a special place (This case last place:)
Audi.insert(7,'e-tron GT')
print(Audi)

# Pop / Delete something from the List:
Audi.pop(0)
print(Audi)

Auslaumodell = Audi.pop(1)
print (Auslaumodell)
print (Audi)

print ("-----------------------")

# Remove: Benefit of Removing by calling name, instead of Position:

AudiQ = ['Q2', 'Q3' , 'Q5' , 'Q7' , 'Q8']
print(AudiQ)
AudiQ.remove('Q2')
print(AudiQ)

print ("-----------------------")

# Sort: 
BMW = ['3er', '5er' , '1er', 'iX' , '7er' , '2er' , 'M4' , 'M5']
print(BMW)
BMW.sort()
print(BMW)

#Count:
wv=len(BMW)
print(wv)

print ("-----------------------")

# Find min and max in List:
digits = [1,2,3,4,5]
print(min(digits))
print(max(digits))

# Just get the first 3 Numbers:
print(digits[:3])
# Get the second until third digits:
print(digits[1:3])

print ("-----------------------")

# Tuples are Lists but you can't change the order:
dimensions = (200,50)
print(dimensions[0])
print (dimensions[1])

# have to renew the whole variable
dimensions = (300,50)
print(dimensions[0])
print (dimensions[1])
