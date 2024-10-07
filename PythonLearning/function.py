def greeting(username):
    """Display a greeting"""

    print(f"Your name is: {username}")
greeting("Nomaan")

def car(manufacture, model):
    """Gives out your car"""

    print(f"Your car is a: {manufacture}, {model}")
# Call the function: Uerbegen von Variablen 
car('Volkswagen', 'Golf')
car('BMW', '5 Series')

def name_format (name, surname):
    """"Defnition on how to format the Name:"""
    full_name = f"{name.title()} {surname.title()}"
    return full_name
    
myname = name_format ("Steve" , "Jobs")
print (myname)