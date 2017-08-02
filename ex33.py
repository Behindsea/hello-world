from sys import argv
script, number = argv

def while_loop_with_number(number):
    i = 0
    while i < number:
        print(f"At the top i is {i}")
        numbers.append(i)

        i +=  1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


numbers = []
while_loop_with_number(int(number))

print("The numbers: ")

for num in numbers:
    print(num)
