class Robot:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        self.routines = 0
    
    def sit(self):
        print(f"{self.name} is now sitting.")
    
    def walk(self):
        print(f"{self.name} is walking.")

    def number_routines(self):
        print(f"{self.name} knows {self.routines} routines!")

    def update_routines(self, rtines):
        rtines = int(rtines) 
        if rtines > 0:
            self.routines += rtines
            print (f"{self.name} now knows {self.routines} routines!")
        elif rtines < 0:
                self.routines += rtines
                rtines = abs(rtines)
                print(f"{self.name} mow knows {rtines} less routines!")
        else:
             print("pick a number greater than 0 or less than 0")
           
robot1 = Robot('Zed-6' , 6)

print(robot1.name)
print(robot1.age)
robot1.sit()
robot1.walk()            
robot1.number_routines()
robot1.update_routines(2)
robot1.update_routines(-1)

class SoldierRobot(Robot):
    def __init__(self, name, age, weapons):
         
         super().__init__(name,age)
         self.weapons = weapons
    def list_weapons(self):
         print(f"{self.name} has the following weapons: {self.weapons}")

robot2 = SoldierRobot("Chuck88" , 5 , ["laser" , "shield" , "cannon"])
print(robot2.name)
robot2.list_weapons()