def solve(numbers: dict[str, int]) -> int:
    result = 0
    with open('01/input') as f:
        for line in f:
            lvalues = {line.find(key): value for key, value in numbers.items() if line.find(key) > -1}
            rvalues = {line.rfind(key): value for key, value in numbers.items() if line.rfind(key) > -1}
            result += int(f'{lvalues[min(lvalues)]}{rvalues[max(rvalues)]}')
    return result

numbers = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
print(solve(numbers))
numbers = numbers | {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
print(solve(numbers))
