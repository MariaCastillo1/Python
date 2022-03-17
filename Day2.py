#strings
#print("Hello" [4])
print("123" + "456")

#interger (son números)
print(123 + 456)

#123_456_789 los guiones bajos sirven para separar visualmemte
#los números y sea mas fácil leerlos, se puede poner así y el
#programa lo tomará como un número normal.

#Float (números con decimales)
3.1416

#Boolean
True
False

# num_char = len(input("What is your name? "))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

two_digit_number = input("Type a two digit number: ")

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

two_digit_number = first_digit + second_digit

print(two_digit_number)

#redondear numerros, se pone le numero o la operacion de division priemro y despues de una coma
#el numero de decimales que se queire, en el caos de abajo la respuesta sería 2.67
#con float // se convierte en interger osea en un numero sin decimal, por lo que 8 // 3 es 2
# se puede usar +=, -=, /=, *=
print(round(2.66666, 2))
print(8 // 3)

#para adicionar algo se peude abreviar con +=, en este ejemplo es lugar de poner
# score = socore + 1
score = 0
score += 1

#f string: es para no tener que cambiar y poner str o int a lo demas
score = 0
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height}, are you winning? {isWinning}")

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)
restYears = 90 - age_as_int
rest_days = restYears * 365
rest_weeks = restYears * 52
rest_months = restYears * 12

print (f"You have left dyas {rest_days}, {rest_months}, {rest_weeks}")

print("Welcome to the tip calculator.")
amount = input("What was your total bill? $")
amount_int = int(amount)

tip = input("What percentage of tip would you like to give, 10, 12, 15? ")
tip_int = int(tip)

everyone = input("How many people splitting the bill? ")
everyone_int = int(everyone)

cal_tip = (tip_int / 100) * amount_int
result = (amount_int + cal_tip) / everyone_int
result_round = round(result, 2)

print(f"Each person should pay ${result_round}")




