import random


#global Constaint
MAX_LINES = 3
MAX_bet = 100
MIN_BET = 1

#deposite amount wala code

def deposite():
    while True:
        amount = input("what is your deposite rs?")
        if amount.isdigit():#below
            amount = int(amount)#to only allow int no str
            if amount > 0:
                break
            else:
                print("amount should be greater then zero")
        else:
            print("enter a no.")
    return amount
# deposite()

#tu get the no lines
def no_of_lines():
    while True:
        lines = input("what is your no of linesto bet on(1- " + str(MAX_LINES)+ "):- ")
        if lines.isdigit():#below
            lines = int(lines)#to only allow int no str
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"amount should be greater then 0 and more then {MAX_LINES}")
        else:
            print("enter a no.")
    return lines   
    
# no_of_lines()
def bets():
    while True:
        amount = input("what is your bet on line rs?")
        if amount.isdigit():#below
            amount = int(amount)#to only allow int no str
            if MIN_BET<= amount <= MAX_bet:
                break
            else:
                print(f"amount should be between {MIN_BET} - {MAX_bet}")
        else:
            print("enter a no.")
    return amount
  
  
        
#run the code again using main ()
def main():
    balance = deposite()
    lines = no_of_lines()
    while True:
        bet = bets()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'you can not bet more then the balance -  your balance is {balance}')
        else:
            break
      
    print(f"the amount of {bet}rs on {lines} lines is {total_bet} is the final bet amount")
   
    # print(balance,lines)
    
main()