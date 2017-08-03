people = 30
cars = 40
trucks = 15

# if for one case, elif for another, and else for all else.
if cars > people:
    print("We should take the cars.")
elif cats < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
