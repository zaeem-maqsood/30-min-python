

def Step1(new_credit_list):
    
    print("\nStep 1 -------------------------------------------------------\n")
    new_credit_list.reverse()
    step_1_list = new_credit_list
    print("The Credit Card Numbers In Reverse Are :", step_1_list)

    step_1_list = step_1_list[::2]
    print("Every Other Digit Starting From The Right Side Is :", step_1_list)

    sum_of_step_1_list = sum(step_1_list)
    print("The Sum of Every Other Digit From The Right Side Is :", sum_of_step_1_list)
    return sum_of_step_1_list


def Step2(new_credit_list):
    
    print("\nStep 2 --------------------------------------------------------\n")
    step_2_list = new_credit_list
    step_2_list = step_2_list[1::2]
    print("The Numbers That Were Not Included In The Preceding Step :", step_2_list)
    
    double_step_2_list = []
    for number in step_2_list:
        new_number = number * 2
        print("Doubling The Number :", number, "gives : ", new_number)
        # ---------------------------------------------------------
         # This is equal to new_number_list = list(map(int, str(new_number)))
        new_number_list = []
        for x in str(new_number):
            new_number_list.append(int(x))
        # ----------------------------------------------------------
        print("Converting The Doubled Number To A List Gives :", new_number_list)
        double_step_2_list.extend(new_number_list)

    print("Doubling The Numbers That Were Not Included In The Preceding Step And Seperating The Digits :", double_step_2_list)
    sum_of_double_step_2_list = sum(double_step_2_list)
    print("Summing All The Digits :", sum_of_double_step_2_list)
    return sum_of_double_step_2_list


def Step3(step_1, step_2):
    
    print("\nStep 3 --------------------------------------------------------\n")
    total = step_1 + step_2
    print("Adding Step 1 and Step 2 :", total)
    return total


def FinalValidation(step_3):
    
    print("\nFinal Validation -----------------------------------------------\n")
    if (step_3 % 10) == 0:
        return True
    else:
        return False


creditList = []
while len(creditList) < 8:
    creditInput=input('Please enter your 8 digit credit card number: ')
    creditList=list(creditInput)
    if len(creditList) < 8:
        print('You have entered less than 8 digits')
    else:
        new_credit_list = []
        for number in creditList:
            new_credit_list.append(int(number))
        step_1 = Step1(new_credit_list)
        step_2 = Step2(new_credit_list)
        step_3 = Step3(step_1, step_2)

        final_validation = FinalValidation(step_3)
        if final_validation == False:
            print("The Credit Card Number is not valid")
        else:
            print("The Credit Card Number is valid")
        

    











