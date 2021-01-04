import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_of_people = len(names)

random_choice = random.randint(0, num_of_people - 1)

random_person = names[random_choice]

print(random_person + " will pay the bill today")

