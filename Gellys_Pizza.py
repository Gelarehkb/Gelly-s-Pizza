menu = {
    'margarita': 10,
    'provenzale': 12,
    'rusticana': 17,
    'funghi' :16, 
    'cipolla' :13}

extras = ["egg", "cheese", "salami", "pepperoni", "garlic", "ham"]

print("Hello at the Gelly's Pizza Service!\n"
      "Please select your pizza:\n"
      "Pizza margarita: 10 Euros\n"
      "Pizza provenzale: 12 Euros\n"
      "Pizza rusticana: 17 Euros\n"
      "Pizza funghi: 16 Euros\n"
      "Pizza cipolla: 13 Euros")

pizza = input('Enter name of pizza: ')  

while pizza not in menu:
        print("Pizza not available, please try again.")
        pizza = input('Enter name of pizza: ')


print(f"You have selected pizza {pizza} for {menu[pizza]} Euros.")

extra_inputs = input("Which extras would you like? Please enter them separated by a ';'.\n"
        "egg\n"
            "cheese\n"
            "salami\n"
            "pepperoni\n"
            "garlic\n"
            "ham\n")

available=[]
not_available=[]

if extra_inputs == '':
    print('No extras selected.')
    
else:
    seperated = extra_inputs.split(";")
    
    for i in seperated:
        i = i.strip()
        if i in extras:
              available.append(i)
        else:
            not_available.append(i)

    if not not_available:
        print(f"All extras available and added.")
    elif not available and not not_available:
        print("No extras selected.")
    else:
        print(f"Extras not available: {', '.join(not_available)}")
        print(f"Extras available and added: {', '.join(available)}")
        
total = menu[pizza] + (len(available)* 1.5)
print(f"Your total price is now {total} Euros.")
print("Thank you for your order!")
