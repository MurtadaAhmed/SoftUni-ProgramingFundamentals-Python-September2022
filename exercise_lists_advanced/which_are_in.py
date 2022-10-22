first_string = input().split(", ")
second_string = input().split(", ")
new_list = []

for i in first_string:  # "arp"
    for j in second_string:  # "lively"
        if i in j:
            if i not in new_list:
                new_list.append(i)
print(new_list)
