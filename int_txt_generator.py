import random

n = int(input("How many numbers you want to generate? : "))
print("Set range.")
a = int(input("From: "))
b = int(input("To: "))
i = 0
file = open("random_ints_" + str(n) + ".txt", "w")
while i < n :
    file.write(str(random.randint(a, b)) + "\n")
    i += 1
file.close()
                
