from cs50 import get_int

#height = get_int("Height:")

height = get_int("Height: ")
heightN = height
rowP = height
space = rowP


# conditional while loop - while True     #prompt user      if condition:     break       WORKING
while (height < 1 or height > 9):
    print("Usage: height between 1 and 9")
    break

while (height > 1 or height < 9):
    print("value of height = ", height)

# for every row in height
# print spaces height - 1
# print hashes remainder of spaces - height
# print a new line

# for height number of rows
    for rowP in range(1, (height + 1), 1):
        # print("heightN starts: ", heightN)
        rowP = rowP
        # print("rowP is: ", rowP)
        print("^ " * (height - rowP), end = "")

    # for space in range(rowP, 1, -1):
        # print("space is: ", space)
        print("# " * (rowP)),
        # space = (height - 1)
        # print("space is: ", space)
        # print("^ " * space, end=""),
        # print ^ for space = height - 1
        # for hash in range(rowP):
        #     hash = rowP - space
        #     print("# " * hash)

            # print remainder of height - j
            # for k in range(j - height):
            #     print("# ")

            #     print()
    break






