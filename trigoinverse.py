import math as m

print("Choose from the following ")
print("1. arcsin")
print("2. arccos")
print("3. arctan")
print("4. arccot")
print("5. arcsec")
print("6. arccosec")

inverse_choice = int(input("Enter Choice : "))
number_choice = float(input("Enter a value  of whose inverse you want to find: "))


def arcsin(var):
    if var**2 - 1 <= 0:
        result1 = str(m.asin(var))
        result2 = str(m.asin(var))
    else:
        pi2 = (m.pi)/2
        calc1 = m.log(var + (var**2 - 1)**0.5)
        result1 = (str(pi2) + " - (i " + str(calc1)+")")
        result2 = (str(pi2) + " + (i " + str(calc1)+")")
    return result1, result2


def arccos(var):
    if var**2 - 1 <= 0:
        result1 = m.asin(var)
        result2 = m.asin(var)
    else:
        calc1 = m.log(var + (var**2 - 1)**0.5)
        result1 = ("- (i " + str(calc1)+")")
        result2 = ("+ (i " + str(calc1)+")")
    return result1, result2


if inverse_choice == 1:
    decision = 'arcsin'
    calculated_output1, calculated_output2 = arcsin(number_choice)
elif inverse_choice == 2:
    decision = 'arccos'
    calculated_output1, calculated_output2 = arccos(number_choice)
elif inverse_choice == 3:
    decision = 'arctan'
    calculated_output1, calculated_output2 = m.atan(number_choice)
elif inverse_choice == 4:
    decision = 'arccot'
    calculated_output1, calculated_output2 = m.atan(1/number_choice)
elif inverse_choice == 5:
    decision = 'arcsec'
    calculated_output1, calculated_output2 = arccos(1/number_choice)
elif inverse_choice == 6:
    decision = 'arccosec'
    calculated_output1, calculated_output2 = arcsin(1/number_choice)
else:
    decision = 'Unidentified Function!'

print(f'{decision} of {number_choice} is {calculated_output1} and/or {calculated_output2}')
