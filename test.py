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

    options = ['mm', 'cm', 'm', 'km']

    units = {'1': 'mm',
             '2': 'cm',
             '3': 'm',
             '4': 'km'
            }

    # conver = {'1': 0.001,
    #           '2': 0.01,
    #           '3': 1,
    #           '4': 1000
    #           }


    user_input = ''

    for unit_key in units:
        print(unit_key + ". " + units[unit_key])

    user_input = input('Your choice: ')

    while user_input.lower() not in units.keys():
        user_input = input("Try again")

    print('You picked: ' + units[user_input])


    input_num = int(input('How many?'))

    print(* input_num)


    #
    # key = input('Choose a value to convert to:')
    #
    # print(conver[key] * 1000)


var_dist()