import random

def get_numbers_ticket(min, max, quantity):
    list_of_numbers = []
    if min > 0 and max < 1001:
            while len(list_of_numbers) < quantity:
                random_number = random.randint(min, max)
                if random_number not in list_of_numbers:
                     list_of_numbers.append(random_number)
                else:
                     continue

            list_of_numbers.sort()
            return list_of_numbers
    else:
        return list_of_numbers


def main():
    try:
       result = get_numbers_ticket(min=int(input('Enter minimum possible number (not less than 1): ')), 
                        max=int(input('Enter maximum possible number (no more than 1000): ')), 
                        quantity=int(input('Enter number of numbers that need to be selected (values between min and max)')))
    except:
        print('Incorrect data')
        main()
    print("Ваші лотерейні числа:", result)
    

if __name__ == '__main__':
    main()
