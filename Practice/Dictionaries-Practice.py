'''
1. **Create a Dictionary**
    
    Write a program that creates a dictionary to store the names of five students and their corresponding grades. After creating the dictionary, print each student's name along with their grade.
'''
students_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90,
    "Ethan": 88
}
for student, grade in students_grades.items():
    print(f"{student}: {grade}")
'''
2. **Accessing Values**
    
    Given the following dictionary:
    
    ```python
    student = {"name": "Alice", "age": 16, "grade": "A"}
    ```
    
    Write a program that accesses and prints the student's name and age.
'''
student = {"name": "Alice", "age": 16, "grade": "A"}
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
'''
3. **Updating Values**
    
    Extend the previous problem by writing a program that updates the student's grade to "A+" and then prints the updated dictionary.
'''
student["grade"] = "A+"
print(student)
'''
4. **Adding New Key-Value Pairs**
    
    Create a dictionary to store the names of three favorite movies and their release years. Write a program that allows the user to add a new movie and its release year to the dictionary, then print the updated dictionary.
'''
favorite_movies = {
    "Inception": 2010,
    "The Matrix": 1999,
    "Interstellar": 2014
}
new_movie = input("Enter the name of a new movie: ")
new_year = int(input("Enter the release year of the movie: "))
favorite_movies[new_movie] = new_year
print(favorite_movies)
'''
5. **Removing Key-Value Pairs**
    
    Write a program that creates a dictionary of five fruits and their prices. Allow the user to input the name of a fruit to remove it from the dictionary. After removal, print the updated dictionary.
'''
fruits_prices = {
    "Apple": 1.2,
    "Banana": 0.5,
    "Orange": 0.8,
    "Grapes": 2.0,
    "Mango": 1.5
}
fruit_to_remove = input("Enter the name of the fruit to remove: ")
if fruit_to_remove in fruits_prices:
    fruits_prices.pop(fruit_to_remove)
else:
    print(f"{fruit_to_remove} not found in the dictionary.")
print(fruits_prices)
'''
6. **Looping Through a Dictionary**
    
    Given the following dictionary:
    
    ```python
    inventory = {"apples": 10, "bananas": 5, "oranges": 8}
    ```
    
    Write a program that loops through the dictionary and prints each fruit along with its quantity in a formatted string.
'''
inventory = {"apples": 10, "bananas": 5, "oranges": 8}
for fruit, quantity in inventory.items():
    print(f"There are {quantity} {fruit}.")
'''
7. **Counting Occurrences**
    
    Write a program that takes a list of words and counts the occurrences of each word using a dictionary. Print the resulting dictionary with words as keys and their counts as values.
'''
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
'''
8. **Nested Dictionaries**
    
    Create a dictionary that contains information about three different books, where each book has a title, author, and publication year. Write a program that prints the details of each book.
'''
books = {
    "book1": {"title": "1984", "author": "George Orwell", "year": 1949},
    "book2": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    "book3": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
}
for book_id, details in books.items():
    print(f"{details['title']} by {details['author']}, published in {details['year']}")
'''
9. **Dictionary Comprehension**
    
    Use dictionary comprehension to create a dictionary that maps integers from 1 to 10 to their squares. Print the resulting dictionary.
'''
squares = {x: x**2 for x in range(1, 11)}
print(squares)
'''
10. **Finding Maximum Value**
    
    Write a program that takes a dictionary of employees with their salaries and finds the employee with the highest salary. Print the name of the employee along with their salary.
'''
employees_salaries = {
    "Alice": 70000,
    "Bob": 85000,
    "Charlie": 60000,
    "Diana": 95000,
    "Ethan": 75000
}
max_salary_employee = max(employees_salaries, key=employees_salaries.get)
print(f"The highest salary is {employees_salaries[max_salary_employee]} by {max_salary_employee}.")