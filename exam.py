#Challenge 1:
# Write a function that takes a natural number as input and outputs the number of digit in it.
# Conversion of number to string is not allowed

user_input = int(input("enter a whole number please: "))


def digit_count(num):
    if user_input == 0:
        print("please enter a whole number greater than zero")
    else:
        num_digits = 0
        while num !=0:
            num //=10
            num_digits +=1
        print(f"number of digits in {user_input} is : {num_digits}")

digit_count(user_input)

#Challenge 2:
# Write a function that takes a natural number as input and outputs the reverse of that number.
#Conversion of number to string is not allowed

user_input = int(input("enter a whole number please: "))


def reverse_num(num):
    if user_input == 0:
        print("please enter a whole number greater than zero")
    else:
        reversed_num = 0
        while num !=0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10
        print(f"reversed number of {user_input} is : {reversed_num}")

reverse_num(user_input)

#Challenge 3 :
# Write a function where user will enter a natural number as input and
# output returns the number of zeroes in the end of the factorial of that number.

user_input = int(input("enter a whole number please: "))


def zero_in_fact (num):
    if user_input == 0 or user_input < 0:
        print("please enter a whole number greater than zero")
    else:
        x = num // 5
        zeros = x
        while x > 0:
            x /= 5
            zeros += int(x)
        factorial = 1
        for i in range(1, num + 1):
            factorial = factorial * i
        print(f"number of zeros at the end in  {user_input} factorial  {factorial} is : {zeros}")

zero_in_fact(user_input)

#Challenge 4 :
# list1 = ["India" , "England", "Spain"]list2 = ["Delhi","London","Madrid"]
# Write your own function that takes list1 and list2 as inputs and
# returns a dictionary like dict1 = {"India” : “Delhi” , “England”:”London”, “Spain”:”Madrid”}


list1 = ["India" , "England", "Spain"]
list2 = ["Delhi","London","Madrid"]
def create_dict_from_two_lists (key_list,value_list):
    if len(key_list) != len(value_list):
        print(" please ensure the lists have equal elements")
    else:
        dict1 = {key_list[i]: value_list[i] for i in range(len(key_list))}
        return(dict1)

print(create_dict_from_two_lists(list1,list2))


#Challenge 5 :Given places = {(“19.07'53.2”, “72.54'51.0”): "Mumbai",
#(“28.33'34.1”, “77.06'16.6”): "Delhi"}
#Write code to create a new dictionary using given dictionary
# city = {
#    "Mumbai": {“Latitude”: “19.07'53.2” , “Longitude”: “72.54'51.0”},
#    “Delhi” : {“Latitude”: “28.33'34.1” , “Longitude”: “77.06'16.6”}
# }


#challnege 6 : Given mylist = [3, 5 ,4 , 6, 9, 10 , 2 , 8, 7 ,1]
#using for loop find the sum of all even numbers in mylist

mylist = [3, 5 ,4 , 6, 9, 10, 2 , 8, 7 ,1]

def sum_even_nos_in_list(l1):
    even_num_sum = 0
    for i in l1:
        if i%2 == 0:
            even_num_sum += i
        else:
            continue
    return (even_num_sum)

print(sum_even_nos_in_list(mylist))


