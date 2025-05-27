import csv

# write  a function to generate the first n fibonacci numbers
def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        fib_sequence=[0,1]
        while len(fib_sequence)<n:
            next_num=fib_sequence[-1]+fib_sequence[-2]
            fib_sequence.append(next_num)
        return fib_sequence

print(fibonacci(10))

#Example 2
#Create a program that reads a text file and counts the frequency of each word.
def count_word_frequency(file_path):
    word_frequency={}
    with open(file_path, 'r') as file:
        text=file.read()
    words=text.split()
    for word in words:
        word=word.lower()
        if word in word_frequency:
            word_frequency[word]+=1
        else:
            word_frequency[word]=1
    return word_frequency

print(count_word_frequency('file.txt'))

#Example 3
# Write a function to validate user input for different data types (e.g., integer, float, email address).
def validate_user_input(input, data_type):
    if data_type == 'integer':
        return input.isdigit()
    elif data_type == 'float':
        return input.replace('.', '', 1).isdigit()
    elif data_type == 'email':
        return '@' in input and '.' in input
    else:
        return False

print(validate_user_input('123', 'integer'))
print(validate_user_input('123.45', 'float'))
print(validate_user_input('test@example.com', 'email'))

#Example 4
# Read a CSV file containing student data and calculate average grades.
def calculate_average_grades(csv_file_path):
    with open(csv_file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            # Assume all columns except 'Name' are grades
            grades = [float(value) for key, value in row.items() if key != 'Name']
            if grades:
                avg = sum(grades) / len(grades)
                print(f"{name}: {avg:.2f}")
            else:
                print(f"{name}: No grades available")

# Example usage:
# calculate_average_grades('students.csv')

# Create a text-based address book.
class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print(f"Added contact: {name}, Phone: {phone}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"{name}: {self.contacts[name]}")
        else:
            print(f"Contact '{name}' not found.")

# Create a sample CSV file for testing
sample_data = [
    {'Name': 'Alice', 'Math': 85, 'Science': 90, 'English': 78},
    {'Name': 'Bob', 'Math': 75, 'Science': 80, 'English': 88},
    {'Name': 'Charlie', 'Math': 92, 'Science': 87, 'English': 85}
]

with open('students.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Math', 'Science', 'English']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in sample_data:
        writer.writerow(row)

