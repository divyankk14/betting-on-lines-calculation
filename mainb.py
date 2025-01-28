import random


#global Constaint
MAX_LINES = 3
MAX_bet = 100
MIN_BET = 1

WIN_MULTIPLIER = 2
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
            print(f"You cannot bet more than your balance of ₹{balance}.")
            continue
        # balance update here
        balance -= total_bet
        print(f"Total bet: ₹{total_bet}. Remaining balance: ₹{balance}.")
        
        # Computer randoml chooses for a line
        computer_line = random.randint(1, MAX_LINES)
        print(f"Computer chose line: {computer_line}.")
        
        # Check if user won
        if computer_line in range(1, lines + 1):  # User wins if computer choice matches user's range
            winnings = total_bet * WIN_MULTIPLIER
            balance += winnings
            print(f"Congratulations! You won ₹{winnings}. Your updated balance is ₹{balance}.")
        else:
            print("You lost this round. Better luck next time!")
        
        # Check if user wants to continue
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes' or balance < MIN_BET:
            print(f"\nThank you for playing! Your final balance is ₹{balance}.")
            break

# Run the program
main()