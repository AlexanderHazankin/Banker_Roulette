# This code was written without the choice() function
# print(f"{random.choice(names)} is going to buy the meal today!")

import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
random_name = (names[(random.randint(0, len(names)-1))])

print(f"{random_name} is going to buy the meal today!")
