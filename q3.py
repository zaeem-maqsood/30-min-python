'''
Name: Momina Khan
Student ID: 10190329


'''

# Uncomment this for case 1: Marie, Alex, Aurora, and Smith not invited
facebook_Friends=['Hannah','Marie','Bob','Sam','Alex','Aurora','Smith']
party_Friends=['Joe','Sam','Carl','Hannah','Bob']




# Uncomment for case 2: Everyone is invited
# facebook_Friends=['Hannah','Marie','Bob','Sam','Alex','Aurora','Smith']
# party_Friends=['Hannah','Marie','Bob','Sam','Alex','Aurora','Smith']




# Uncomment for case 3: No one is invited
# facebook_Friends=['Hannah','Marie','Bob','Sam','Alex','Aurora','Smith']
# party_Friends=[]

# Another case for no one being invited (Jose who is not her Facebook Friend is invited):
# facebook_Friends=['Hannah','Marie','Bob','Sam','Alex','Aurora','Smith']
# party_Friends=['Jose']




# Uncomment for case 3: Alice has no friends
# facebook_Friends=[]
# party_Friends=[]




if not facebook_Friends:
    print('Alice has no friends')

elif not party_Friends:
    print('There are no guests')

elif facebook_Friends and party_Friends:
    
    # We make a temporary list to see who isn't invited from her Facebook friends
    not_invited_list = []
    
    # We have to check which of Alice's Facebook Friends are not invited and add them to our temporary list
    for facebook_friend in facebook_Friends:
        if facebook_friend not in party_Friends:
            not_invited_list.append(facebook_friend)

    # if the amount of people not invited equals the length of her Facebook Friends than no one was invited
    if len(not_invited_list) == len(facebook_Friends):
        print("No one is invited!")
    elif len(not_invited_list) == 0:
        print("Everyone is invited!")
    else:
        for friend in not_invited_list:
            print(friend, " was not invited :(")


















