from cs50 import get_string
from cs50 import sys



if len (sys.argv) != 2 :
    print ("Usage: python caesar.py key")
    # sys.exit (1)

string = get_string("Enter a string: ")


for c in string:
    print("string is: ", c)
# from __future__ import print_function
# import sys
# print(sys.argv, len(sys.argv)




# --get the key
#   --get the plain text
#       encrypt cypher text
#           print cyper text

# encypher
#   for each character in plaintext string
#       if alphabetic
#           shift character by key
#           preserving case

# sys.argv[1]



# # python print_args.py
# ['print_args.py'] 1

# # python print_args.py foo and bar
# ['print_args.py', 'foo', 'and', 'bar'] 4

# # python print_args.py "foo and bar"
# ['print_args.py', 'foo and bar'] 2

# # python print_args.py "foo and bar" and baz
# ['print_args.py', 'foo and bar', 'and', 'baz'] 4
