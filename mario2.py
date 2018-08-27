from cs50 import get_int

#height = get_int("Height:")

heightN = get_int("Height: ")
# i = 5
# j = 0
# k = 0

# conditional while loop - while True     #prompt user      if condition:     break       WORKING
while (heightN < 1 or heightN > 9):
    print("Usage: height between 1 and 9")
    break

while (heightN > 1 or heightN < 9):
    print("value of height = ", height)

# for every row in height
# print spaces height - 1
# print hashes remainder of spaces - height
# print a new line

# for height number of rows
    rowP = heightN
    for rowP in range(1, heightN, 1):
        print("heightN starts: ", heightN)
        # row = rows - 1
        # print("row i is: ", row)

        for space in range(heightN, -1):
            print("space is: ", space)
            # space = (rows
            print("space is: ", space)
            print("^ " ),
            # print ^ for space = height - 1
            for hash in range(rowP):
                print("# " * rowP)

                # print remainder of height - j
                # for k in range(j - height):
                #     print("# ")

                #     print()
    break






