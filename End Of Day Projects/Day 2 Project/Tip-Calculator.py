print("Welcome to the tip calculator!")
#Asking the user how much the total bill was for each person before the tip
total_person_1 = input("\nWhat was the total bill for person 1? ")
total_person_2 = input("\nWhat was the total bill for person 2? ")
total_person_3 = input("\nWhat was the total bill for person 3? ")
total_person_4 = input("\nWhat was the total bill for person 4? ")
total_person_5 = input("\nWhat was the total bill for person 5? ")
#Asking the user how much they want to tip their server
percentage_tip = input("\nEnter the percentage tip you would like to give ")
#Asking the user how many people are going to split the bill
total_people = input("\nHow many people are going to split the tax? ")
#Asking the user how much the total tax was
total_tax = input("\nWhat is the total for the tax? ")
#Does the math for each person's bill by finding the percentage and adding it with the tax divided by the total amount of people
math_person_1 = (int(percentage_tip) / 100 + 1) * float(total_person_1) + float(total_tax) / int(total_people)
math_person_2 = (int(percentage_tip) / 100 + 1) * float(total_person_2) + float(total_tax) / int(total_people)
math_person_3 = (int(percentage_tip) / 100 + 1) * float(total_person_3) + float(total_tax) / int(total_people)
math_person_4 = (int(percentage_tip) / 100 + 1) * float(total_person_4) + float(total_tax) / int(total_people)
math_person_5 = (int(percentage_tip) / 100 + 1) * float(total_person_5) + float(total_tax) / int(total_people)
#Uses an F-string to print out each persons bill as a str from a float value
print(f"Person 1 should pay ${math_person_1:.2f}\nPerson 2 should pay ${math_person_2:.2f}\nPerson 3 should pay ${math_person_3:.2f}\nPerson 4 should pay ${math_person_4:.2f}\nPerson 5 should pay ${math_person_5:.2f}")

