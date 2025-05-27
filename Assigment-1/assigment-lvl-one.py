
# Level 1 Calculator:
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"

print(calculate(5, 3, '*'))

#Example 2

def convert_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(convert_temperature(25))


#Example 3 
def get_vowel_count(string):
    voewl='aeiou'
    return sum(1 for char in string if char in voewl)

print(get_vowel_count("Hello world"))

#Example 4
#list=[1,2,3,4,5]
def compute_list(list, operation):
    if operation == 'sum' and all(isinstance(item, int) for item in list):
        return sum(list)
    elif operation == 'average' and all(isinstance(item, int) for item in list):
        return sum(list)/len(list)
    elif operation == 'max' and all(isinstance(item, int) for item in list):
        return max(list)
    elif operation=='reverse'and all(isinstance(item, str) for item in list):
        return list[::-1]
    else:
        return "Invalid operation"

print(compute_list([1, 5, 3, 8, 2], 'sum'))
print(compute_list(['a', 'b', 'c'], 'reverse'))
