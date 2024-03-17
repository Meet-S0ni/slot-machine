# project slot machine 

import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    #-#
    print(f"old all_sybbols {all_symbols}")
    #
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    #-#
    print(f"new all_sybbols {all_symbols}")
    #
    columns = []
    #-#
    print(f"old columns {columns}")
    #
    current_symbols = all_symbols[:]
    #-#
    print(f"old current_sybbols {current_symbols}")
    #
    for _ in range(cols):
        column = []
        #-#
        print(f"old column {column}")
        #
        for _ in range(rows):
            value = random.choice(current_symbols)
            #-#
            print(f"value {value}")
            #
            current_symbols.remove(value)
            #-#
            print(f"updated current_symbols {current_symbols}")
            #
            column.append(value)
            #-#
            print(f"updated column {column}")
            #
        columns.append(column)
        #-#
        print(f"final columns {columns}")
        #
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        #-#
        print(f"columns range {range(len(columns[0]))}")
        print(f"columns lenth {len(columns[0])}")
        #
        for i, column in enumerate(columns):
            #-#
            print(f"index {i}")
            print(f"column {column}")
            #
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposite():
    while True:
        amount = input("What would you like to deposite? : $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be grater than 0")
        else:
            print("Please enter number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines: to bet on (1-" + str(MAX_LINES) + ")? : ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines 1-" + str(MAX_LINES) + ")")
        else:
            print("Please enter number")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? : $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET} ")
        else:
            print("Please enter number")
    return amount

def main():
    balance = deposite() 
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance} ")
        else:
            break
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
main()
