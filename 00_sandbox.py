# ask users for a number
get_number = int(input("choose a number? "))

# multiply the number by 5
times_five = get_number * 5

answer = "{} times five is equal to " \
         "{}".format(get_number, times_five)

# output the result
print(answer)
