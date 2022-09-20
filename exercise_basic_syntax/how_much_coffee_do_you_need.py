# 1.read the command
# 2.create variable amount of coffee
# 3.while loop, while the command != "END"
# -if the commands mentioned are in upper case:
# --add 2 to the variablr
# -elif commands are in lower case
# --add 1 to the varilable
# -receive the next input
# 4. outside while loop, check if the coffe > 5:
# -if so print "You need extra sleep".
# -else, print the variable
command = input()
coffee_count = 0
while command != "END":
    if command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffee_count += 2
    elif command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee_count += 1
    command = input()
if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)
