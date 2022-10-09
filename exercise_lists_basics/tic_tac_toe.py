first_line = input().split()
second_line = input().split()
third_line = input().split()

if first_line[0] == "1" and first_line[1] == "1" and first_line[2] == "1":
    print("First player won")
# 111
# ***
# ***
elif second_line[0] == "1" and second_line[1] == "1" and second_line[2] == "1":
    print("First player won")
# ***
# 111
# ***
elif third_line[0] == "1" and third_line[1] == "1" and third_line[2] == "1":  #
    print("First player won")
# ***
# ***
# 111

elif first_line[0] == "1" and second_line[0] == "1" and third_line[0] == "1":
    print("First player won")
# 1**
# 1**
# 1**
elif first_line[1] == "1" and second_line[1] == "1" and third_line[1] == "1":
    print("First player won")

# *1*
# *1*
# *1*
elif first_line[2] == "1" and second_line[2] == "1" and third_line[2] == "1":
    print("First player won")
# **1
# **1
# **1
elif first_line[0] == "1" and second_line[1] == "1" and third_line[2] == "1":
    print("First player won")
# 1**
# *1*
# **1
elif first_line[2] == "1" and second_line[1] == "1" and third_line[0] == "1":
    print("First player won")
# **1
# *1*
# 1**

# now we repeat the same thing, but for the second player:

elif first_line[0] == "2" and first_line[1] == "2" and first_line[2] == "2":
    print("Second player won")
# 222
# ***
# ***
elif second_line[0] == "2" and second_line[1] == "2" and second_line[2] == "2":
    print("Second player won")
# ***
# 222
# ***
elif third_line[0] == "2" and third_line[1] == "2" and third_line[2] == "2":  #
    print("Second player won")
# ***
# ***
# 222

elif first_line[0] == "2" and second_line[0] == "2" and third_line[0] == "2":
    print("Second player won")
# 2**
# 2**
# 2**
elif first_line[1] == "2" and second_line[1] == "2" and third_line[1] == "2":
    print("Second player won")

# *2*
# *2*
# *2*
elif first_line[2] == "2" and second_line[2] == "2" and third_line[2] == "2":
    print("Second player won")
# **2
# **2
# **2
elif first_line[0] == "2" and second_line[1] == "2" and third_line[2] == "2":
    print("Second player won")
# 2**
# *2*
# **2
elif first_line[2] == "2" and second_line[1] == "2" and third_line[0] == "2":
    print("Second player won")
# **2
# *2*
# 2**

else:
    print("Draw!")