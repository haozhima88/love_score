# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower_case = name1.lower()
name2_lower_case = name2.lower()

both_name = name1_lower_case + name2_lower_case

count_t = both_name.count('t')
count_r = both_name.count('r')
count_u = both_name.count('u')
count_e = both_name.count('e')
count_l = both_name.count('l')
count_o = both_name.count('o')
count_v = both_name.count('v')

count_true = count_t + count_r + count_u + count_e
count_love = count_l + count_o + count_v + count_e
love_score = count_true * 10 + count_love

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}")