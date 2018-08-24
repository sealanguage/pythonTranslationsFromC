from cs50 import get_int

#height = get_int("Height:")

height = get_int("Height:")
i = 0
j = 0
k = 0

# conditional while loop - while True     #prompt user      if condition:     break

# while True:
# prompt user
if (height > 0 or height < 6):
    height -1;
    break


# for every row in height
# print spaces height - 1
# print hashes remainder of spaces - height
# print a new line

# for height number of rows
    while i in range(height):
        print("^ "),
        # print | for j = height - 1
        for j in range(height - 1):
            print("# ")
            # print remainder of height - j
            # for k in range(j - height):
            #     print("# ")
            #     print()






