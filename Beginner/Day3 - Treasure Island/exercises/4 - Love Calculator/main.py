# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1.lower() + name2.lower()

sum = 10 * (
  combined_string.count("t")
  +
  combined_string.count("r")
  +
  combined_string.count("u")
  +
  combined_string.count("e")
  )

sum+=(
  combined_string.count("l")
  +
  combined_string.count("o")
  +
  combined_string.count("v")
  +
  combined_string.count("e")
)

print(sum)