import random

strings_amount = int()
numbers_amount = int()

while strings_amount <= 500 or strings_amount > 1000:
    strings_amount = int(input('Enter amount of strings (501-1000): '))
    if strings_amount <= 500 or strings_amount > 1000:
        print('Your amount of strings need to be in range 501 - 1000')

while numbers_amount < 10 or numbers_amount > 50:
    numbers_amount = int(input('Enter amount of numbers in string (11-50): '))
    if numbers_amount <= 10 or numbers_amount > 50:
        print('Your amount of numbers need to be in range 11 - 50')


def write_numbers_into_file(amount_of_strings, amount_of_numbers):
    with open('vectors.csv', 'w') as csvfile:
        i = 0
        while i < amount_of_strings:
            current_index_of_number = 0
            while current_index_of_number < amount_of_numbers:
                csvfile.write(str(random.uniform(-1.0, 1.0)))
                if amount_of_numbers == current_index_of_number + 1:
                    csvfile.write('\n')
                else:
                    csvfile.write(',')
                current_index_of_number += 1
            i += 1


write_numbers_into_file(strings_amount, numbers_amount)