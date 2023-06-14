# def scramble(s1, s2):
#     counter = 0
#     for char in s2:
#         if char in s1:
#             counter += 1
#             idx = s1.find(char)
#             tmp = list(s1)
#             tmp[idx] = " "
#             s1 = "".join(tmp)
            
#     return counter == len(s2)

# def scramble(s1, s2):
#     counter = 0
#     for char in s2:
#         if char in s1:
#             counter += 1
#             s1 = s1.replace(char, " ", 1)
            
#     return counter == len(s2)


# def scramble(s1, s2):
#     counter = 0
#     for char in s2:
#         if char in s1:
#             counter += 1
            
#     return counter == len(s2)

# def scramble(s1, s2):
#     counter = 0
#     for char in s2:
#         counter2 = 0
#         for j in range(len(s1)):
#             if char == s1[j] and counter2 == 0:
#                 counter += 1
#                 tmp = list(s1)
#                 tmp[j] = " "
#                 s1 = "".join(tmp)
#                 counter2 += 1

#     return counter == len(s2)

def scramble(s1, s2):
    counter = 0
    char_count = {}
    
    for char in s1:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    for char in s2:
        if char in char_count and char_count[char] > 0:
            counter += 1
            char_count[char] -= 1
    
    return counter == len(s2)
