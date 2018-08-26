from cs50 import get_int

#height = get_int("Height:")

height = get_int("Height: ")
i = 5
j = 0
k = 0

# conditional while loop - while True     #prompt user      if condition:     break       WORKING
if (height < 1 or height > 9):
    print("Usage: height between 1 and 5")

if (height > 0 or height < 9):
    print("value of height = ", height)


# for every row in height
# print spaces height - 1
# print hashes remainder of spaces - height
# print a new line

# for height number of rows
    while i in range(height):
        print("height i starts: ", i)
        i = height - 1
        print("height i is: ", i)

        for j in range(height - i):
            j = (i - 1)
            print("^ " * j),
            # print | for j = height - 1
            for k in range(j + i):
                print("# " * k)
                # print remainder of height - j
                # for k in range(j - height):
                #     print("# ")
                #     print()





