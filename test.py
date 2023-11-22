# units = {'1': 'mm',
#          '2': 'cm',
#          '3': 'm',
#          '4': 'km'
#          }
# key = input('Enter the key: ')
#
# if key in units:
#     print('The value is:', units[key])
# else:
#     print('That key is not in the dictionary.')

def var_dist():

    units = {'1': 'mm',
             '2': 'cm',
             '3': 'm',
             '4': 'km'
            }

    user_input = ''

    for unit_key in units:
        print(unit_key + ". " + units[unit_key])

    user_input = input('Your choice: ')

    while user_input.lower() not in units.keys():
        user_input = input("Please choose the corresponding number. Try again: ")

    print('You picked: ' + units[user_input])

    units.update({'1': 0.001,
                  '2': 0.01,
                  '3': 1,
                  '4': 1000})

    input_num = int(input('How many? '))

    from_unit = (units[user_input] * input_num)

    units.update({'1': 'mm',
                  '2': 'cm',
                  '3': 'm',
                  '4': 'km'})


    to_unit = input('Choose a value to convert to:')

    while to_unit.lower() not in units.keys():
        to_unit = input("Please choose the corresponding number. Try again: ")

    print('You picked: ' + units[to_unit])

    print("{} {} to {} = ".format(input_num,units[user_input],units[to_unit]))

    units.update({'1': 0.001,
                  '2': 0.01,
                  '3': 1,
                  '4': 1000})

    print(units[to_unit] * from_unit)







var_dist()