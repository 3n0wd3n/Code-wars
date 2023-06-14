# def sum_strings(x, y):
#     number_x = 0
#     for char in x:
#         if number_x == 0:
#             number_x += int(char)
#         else:
#             number_x *= 10
#             number_x += int(char)
#     number_y = 0
#     for char in y:
#         if number_y == 0:
#             number_y += int(char)
#         else:
#             number_y *= 10
#             number_y += int(char)
#     return str(number_x + number_y)

# def sum_strings(x, y):
#     num_x = 0
#     num_y = 0
    
#     num_x_len = len(x)
#     num_y_len = len(y)
    
#     # vybere se delší z čísel     
#     num_len = num_x_len if num_x_len > num_y_len else num_y_len
    
#     for i in range(num_len):
#         if num_x_len > i:
#             if num_x == 0:
#                 num_x += int(x[i])
#             else:
#                 num_x *= 10
#                 num_x += int(x[i])
#         if num_y_len > i:
#             if num_y == 0:
#                 num_y += int(y[i])
#             else:
#                 num_y *= 10
#                 num_y += int(y[i])
                
#     return str(num_x + num_y)

def sum_strings(x, y):
    # Reverse the input strings for easier iteration
    x = x[::-1]
    y = y[::-1]

    result = []
    carry = 0
    max_len = max(len(x), len(y))

    for i in range(max_len):
        # Get the digits at the current position
        digit_x = int(x[i]) if i < len(x) else 0
        digit_y = int(y[i]) if i < len(y) else 0

        # Calculate the sum of digits and carry
        digit_sum = digit_x + digit_y + carry
        carry = digit_sum // 10  # Get the carry by integer division
        digit_sum %= 10  # Get the current digit by modulo division

        # Add the current digit to the result
        result.append(str(digit_sum))

    # If there is a remaining carry, add it to the result
    if carry > 0:
        result.append(str(carry))

    # Reverse the result and join the digits into a string
    res = ''.join(result[::-1])
    if len(res) == 0:
        return "0"
    if res[0] == "0" and len(res) > 1:
        return res[1:]
    else:
        return res
    return res
