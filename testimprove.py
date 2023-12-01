
def check_units(valid_list, question):
    while True:
        response = input(question)

        if response in valid_list:
            return response
        else:
            print("please choose from this list: ", valid_list)

valid_distance = ["mm", "cm", "m", "km"]

conversion = {'mm': 0.001,
              'cm': 0.01,
              'm': 1,
              'km': 1000}

user_input = ''

# print list

print("Please choose mm, cm, m or km")

# choose a unit one

from_unit = check_units(valid_distance, "Choose a unit to convert from? ")
print(f"you chose to convert from {from_unit}")

input_num = int(input('How many? '))


# convert to m
#
# to_standard = (conversion[user_input] * input_num)

to_unit = check_units(valid_distance, "Which unit do you want to convert to? ")
print(f"you chose {to_unit}")


# div_unit = ['1', '2']
# if to_unit in div_unit:
#     print(to_standard / conversion[to_unit], units[to_unit])
# else:
#     print(conversion[to_unit] * to_standard, units[to_unit])
#


