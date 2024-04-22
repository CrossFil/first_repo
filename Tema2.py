


# def compere_2(a, b):
#     if a > b:
#         print(a, "biger then", b)
#     elif a == b:
#         print(a, " is equal to ", b)
#     else:
#         print(b, "more then ", a)
    
# compere_2(15, 8)

# x = 12
# y = 12
# compere_2(x, y)

# def add_nummers(num1: int, num2: int) -> int:
#     sum = num1 + num2
#     return sum
# result = add_nummers(12, 4)
# print(result)

# num11 = 13
# num22 = 32
# result = add_nummers(num11, num22)
# print(result)

# def greet(name: str) -> str:
#     return f"Hello, {name}!"
# greeting = greet(input('Enter your name >>> '))
# print(greeting)

# def modify_sring(original: str) -> str:
#     original = 'оригінал'
#     return original
# # print(modify_sring(original=''))
# str_var = 'змінено'
# print(modify_sring(str_var))
# print(str_var)

# def strting_to_codes(string: str) -> dict:
#     codes = {}
#     for ch in string:
#         if ch not in codes:
#             codes[ch] = ord(ch)
#     return codes 
# result = strting_to_codes('Hello world!')
# print(result)

# x = 50
# def func() -> None:
#     x = 2
#     print('local x = ', x)
# func()
# print('global x = ', x)    

# def invite_to_event(name):
#     return f'Dear {name}, we have the honour to invite you to our event'

# name = input('What is your name bro? >>> ')
# print(invite_to_event(name))

# def outr_func():
#     enclosing_var = "Я змінна що охоплює"
#     def innr_func():
#         print("Я знінна всередині ->", enclosing_var)

#     innr_func()

# outr_func()

# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price
#         price *= (1-discount / 100)
#     apply_discount()
#     return int(price)
# # price = 120
# # discount = 20
# discount_price = discount_price(150, 15)
# print(discount_price)

# def get_fullname(first_name, last_name, middle_name=''):
#     if middle_name:
#         fullname = f'{first_name}, {middle_name}, {last_name}'
#     else:
#         fullname = f'{first_name}, {last_name}'
#     return fullname
# fullname = get_fullname("Oleg", "Sergiyovich", "Filonenko")
# print(fullname)

# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     else:
#         space = (length - len(string)) // 2
#         format_string = " " * space + string
#     return format_string #+ space + format_string

# formatted_string = format_string("Oleg", 100)
# print(formatted_string)

# def say(message, times=1):
#     print(message * times)

# say('Привіт') 
# say('Світ ', 5)


