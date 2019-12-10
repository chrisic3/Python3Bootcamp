# age = input("How old are you: ")

# if age:
#     age = int(age)

#     if age >= 18 and age < 21:
#         print("You can enter, but you need a wristband.")
#     elif age >= 21:
#         print("You are good to enter and you can drink.")
#     else:
#         print("YOU, SHALL NOT, PAAASSSS!!!!")
# else:
#     print("Plese enter an age!")


age = input("How old are you: ")

if age:
    age = int(age)

    if age >= 21:
        print("You are good to come in and drink.")
    elif age >= 18:
        print("You can enter, but you need a wristband.")
    else:
        print("YOU, SHALL NOT, PAAASSSS!!!!!")
else:
    pring("Please enter an age.")