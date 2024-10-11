import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
def normalize_phone_re(phone_number):

    sanitized_numbers = []
    
    for number in phone_number:
        normalized = re.sub(r'[^\d+]', '', number)
        
        normalized = re.sub(r'^380', r'+380', normalized)
        
        if not normalized.startswith('+'):
            normalized = '+38' + normalized
        
        sanitized_numbers.append(normalized)
    
    return sanitized_numbers




# Сразу не увидел, что нужно решить задачу с помощью регулярного выражения, по этому сделал так
# def normalize_phone(phone_number):

#     sanitized_numbers = []

#     for number in phone_number:
#         clean_number = ''
#         for i in number:
#             if i in ['0','1','2','3','4','5','6','7','8','9']:
#                 clean_number += i
#             else:
#                 continue

#         if clean_number[0] == '3':
#             clean_number = '+' + clean_number
#         else:
#             clean_number = '+38' + clean_number
        

#         sanitized_numbers.append(clean_number)

#     return sanitized_numbers


def main():
    result = normalize_phone_re(phone_number = raw_numbers)
    # result = normalize_phone(phone_number = raw_numbers)
    print("Нормалізовані номери телефонів для SMS-розсилки:", result)



if __name__ == "__main__":
    main()