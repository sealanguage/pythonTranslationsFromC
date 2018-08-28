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
    while i in range(5):
        print("height i starts: ", i)
        i = height - 1
        print("height i is: ", i)

        while j in range(height - i):
            print("j starts as: ", j)
            j = (i - 1)
            print("j then is: ", j)
            print("^ " * j, end ="")

            # print ^ for j = height - i
            while k in range(i):
                print("k is: ", k)
                k = (k + 1)
                print("k is now: ", k)
                print("# " * k, end =" ")
                # break
                # print remainder of height - j
                # for k in range(j - height):
                #     print("# ")
                print()
        break








# # while True:
# # prompt user
# while(height > 0 or height < 6):
#     break


# # for every row in height
# # print spaces height - 1
# # print hashes remainder of spaces - height
# # print a new line

# #for height number of rows
#     while i in range(height):
#         for j in range(height-1):
#             # print("^ ", end =" ")
#             print("^ ")
#             if(i == height -1):
#                 # break

# # # for height number of rows
# #     while i in range(height):
# #         print("^ "),
# #         # print | for j = height - 1
# #         for j in range(height - 1):
# #             print("# ")
# #             # print remainder of height - j
# #             # for k in range(j - height):
# #             #     print("# ")
# #             #     print()






