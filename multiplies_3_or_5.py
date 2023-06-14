def solution(number):
    summation = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            summation += i
    return summation  
