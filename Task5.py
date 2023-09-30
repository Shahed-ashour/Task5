name = input("Enter your name : ")
age = int(input("Enter your age : "))
street = input("Enter the street : ")
city = input("Enter A city : ")
country = input("Enter A country : ")
print(" ")
print(f'"Name : {name}"')
print(f'"Age : {age}"')
print(f'"Address : {street}, {city}, {country}"')
print(" ")
print(f'''"Hello {name} Your age is {age-5} Years Old,
Your Address is {street}, {city}, {country}."''')
print(" ")
print(type(name))
print(type(age))
print(type(street))
print(type(city))
print(type(country))
print(" ")
print(f'''"Hello {name}, How Are You? \ """ Your Age Is "{age-5}"" +
And Your Country Is: {country}''')
print(" ")
print(f'''"Hello '{name}', How Are You? \\
""" Your Age Is "{age-5}"" + And
Your City Is: {city}''')
print(" ")
name1 = 'ITF Gsg Python'
print(f'First Letter Is "{name1[0]}"')
print(f'Third Letter Is "{name1[2]}"')
print(f'Last Letter Is "{name1[-1]}"')
print(" ")
print(name1[-3:])
print(name1[0:3])
print(name1[0:8:2])
print(name1[-1:-7:-1])
print(" ")
name2 = "$&$&Mohammed$&$&"
new_str = name2.replace("$&$&", "")
print(new_str)
print(" ")
msg = "I %7 Python And Although I %7 GSG with Zakaria"
new_msg = msg.replace("%7", "Love")
print(new_msg)
print(" ")
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num5.zfill(5))
print(num6.zfill(5))
print(" ")
q = "shahed nabil"
print(q.title())
print(q.capitalize())
print(" ")
first_name = "Shahed"
print("*"*10,first_name)
print(first_name.center(20,"*"))
print(first_name,"*"*10)
print(" ")
name_one = "SaMER"
name_two = "Abed"
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())
print(" ")
print(name_one.isupper())
print(name_two.islower())
print(" ")
print(name_one.startswith('S'))
print(name_two.endswith('HD'))
print(" ")
msg1 = "I Love Python And Although I Love GSG with Zakaria"
print(f"Number of <Love> is: {msg1.count('Love')}")
print(f"Number of <t> is: {msg1.count('t')}")
print(" ")
msg2 = "I %7 Python And Although I %7 GSG with Zakaria"
n_msg2 = msg2.replace('%7','Love',1)
print(n_msg2)
