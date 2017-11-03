'''
Name: Momina Khan
Student ID: 10190329


'''
import random

def dice_Rolling():
    grand_points = 0
    print('Welcome to the Dice Rolling Game!')
    option=input('Would you like to roll the dice (Y or N): ')
    while option != 'N':
        points = 0
        dice_One = (random.randint(1,6))
        print(dice_One)
        dice_Two =int(random.randint(1,6))
        print(dice_Two)

        if dice_One == dice_Two:
            points += 10
        elif dice_One == 6 or dice_Two == 6:
            points += 4
        elif (dice_One + dice_Two) == 7:
            points += 2
        print('You got', points,'points this roll')
        grand_points += points
        print('Total Points: ', grand_points)
        option=input('Would you like to roll the dice (Y or N): ')

    if option == 'N':
        print("Your total points are: ", grand_points)
        print('This was fun! Goodbye.')






dice_Rolling()
