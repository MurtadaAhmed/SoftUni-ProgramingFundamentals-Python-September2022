def tribonacci_sequence(num): # 4
    tribonacci_list = [1, ]
    for i in range(1, num):  # 1, 2, 3  # the last one is exclusive because we already added 1 in the list in advance
        if len(tribonacci_list) < 3:
            tribonacci_list.append(i)  # this will add number 1 and number 2 in the list
        else:  # when the list became [1, 1, 2]
            tribonacci_list.append(sum(tribonacci_list[-3:]))  # will add the sum of the last 3 elements to the list
            # == [-3: end of the list] >>> == [-3:-1]

    print(" ".join(list(map(str, tribonacci_list))))
    # the above command with:
    # 1. convert (int list) into (str list) using map.
    # 2. then it will convert the (str list) into (str) using the join and print the result


command = int(input())
tribonacci_sequence(command)