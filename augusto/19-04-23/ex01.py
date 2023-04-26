wages = {}
wages['name1'] = str(input('Name of the first worker: '))
wages['wage1'] = float(input('Wage of the first worker: '))

wages['name2'] = str(input('Name of the second worker: '))
wages['wage2'] = float(input('Wage of the second worker: '))

print(wages)

if wages['wage1'] > wages['wage2']:
    print('The bigger wage is of {} and is {}'.format(
        wages['name1'], wages['wage1']))
elif wages['wage2'] > wages['wage1']:
    print('The bigger wage is of {} and is {}'.format(
        wages['name2'], wages['wage2']))
else:
    print('The wages are equal')