__author__ = 'dwight'

# Scientists measure an object’s mass in kilograms and its weight in newtons. If you know the amount of mass of an
# object in kilograms, you can calculate its weight in newtons with the following formula: weight = mass ϫ 9.8
# Write a program that asks the user to enter an object’s mass, and then calculates its weight. If the object weighs
# more than 1,000 newtons, display a message indicating that it is too heavy. If the object weighs less than 10 newtons,
# display a message indicating that it is too light.

def main():
    mass = float(input('Enter mass (kg): '))
    weight = calc_weight_n(mass)
    print('Weight:', format(weight, ',.2f'), 'Newtons')
    state_outlier(weight)


def calc_weight_n(mass_kg):
    return mass_kg * 9.8


def state_outlier(weight_n):
    light_weight_n = 10
    heavy_weight_n = 1000

    if weight_n < light_weight_n:
        print('Object is too light.')
    if weight_n > heavy_weight_n:
        print('Object is too heavy.')

main()