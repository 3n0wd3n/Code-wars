import re

# def increment_string(s):
#     numbers = "0123456789"
#     bool = False

#     for number in numbers:
#         if number in s:            
#             bool = True
#             break
#     if bool:
#         string_number = re.match(".*?([1-9]+)$", s)
#         if string_number:
#             string_number = re.match(".*?([1-9]+)$", s).group(1)
#             check = re.match(".*?([0-9]+)$", s).group(1)
#             number = int(string_number) + 1
#             if len(str(number)) == len(check):
#                 index = len(s) - len(str(check))
#                 string = s[0:index]
#                 strng = string + str(number)
#                 return strng
#             index = len(s) - len(str(string_number))
#             string = s[0:index]
#             strng = string + str(number)
#             return strng
#         return s
#     else:
#         string = s + "1"
#         return string
import re
def increment_string(s):
    if not s: return '1'
    if s[-1] not in '0123456789':return s+'1'
    number = re.findall(r'\d+$',s)[0]
    word = re.sub(r'\d+$','',s)
    def get_number(n):
        zeroes = re.findall(r'^0+',n)
        zeroes = zeroes[0] if zeroes else ''
        num1 = re.sub(r'^0+','',n)
        num1 = num1 if num1 else '0'
        num2 = str(int(num1) + 1) 
        x = len(num2) - len(num1) if num2 != '1' else 1
        return '0' * (len(zeroes) - x) + num2    
    return word + get_number(number)
