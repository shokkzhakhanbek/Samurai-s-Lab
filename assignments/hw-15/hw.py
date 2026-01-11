import math
import random
from datetime import timedelta



"""
Exercise 1:
Create a Pizza class that could have ingredients added to it. Raise an error if an attempt is made to add a duplicate ingredient.
"""
class Pizza:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            raise ValueError(f"Duplicate ingredient {ingredient}")
        self.ingredients.append(ingredient)


"""
Exercise 2:
Create an Elevator class with methods to go up, go down, and get the current floor. The elevator should not be able to go below the ground floor (floor 0).
"""
class Elevator:
    def __init__(self):
        self._floor = 0

    def go_up(self):
        self._floor += 1

    def go_down(self):
        if self._floor > 0:
            self._floor -= 1

    def get_current_floor(self):
        return self._floor



"""
Exercise 3:
Create a class Stack with methods to push, pop, and check if the stack is empty. Raise an exception if a pop is attempted on an empty stack.
"""
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop  empty")
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0


"""
Exercise 4:
Design a BankAccount class with methods to deposit, withdraw, and check balance. Ensure that an account cannot go into a negative balance.
"""
class BankAccount:
    def __init__(self, initial_balance):
        if initial_balance < 0:
            raise ValueError("Initial balance can't be negative")
        self._balance = float(initial_balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if self._balance - amount < 0:
            raise ValueError("Insufficient funds can't  go negative")
        self._balance -= amount

    def check_balance(self):
        return self._balance


"""
Exercise 5:
Create a class Person with attributes for name and age. Implement a method birthday that increases the person's age by one. Raise an exception if an age less than 0 is entered.
"""
class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Age can't be less than 0")
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1



"""
Exercise 6:
Create an Animal base class and a Dog and Cat derived classes. Each animal should have a sound method which returns the sound they make.
"""
class Animal:
    def sound(self):
        raise NotImplementedError

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"




"""
Exercise 7:
Design a class Calculator with static methods for addition, subtraction, multiplication, and division. Division method should raise a ZeroDivisionError when trying to divide by zero.
"""
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ZeroDivisionError("Не может делиться на 0")
        return x / y


"""
Exercise 8:
Create a class `Car` with attributes for speed and mileage. Raise a ValueError if a negative value for speed or mileage is entered.
"""
class Car:
    def __init__(self, speed, mileage):
        if speed < 0:
            raise ValueError("Speed can't be nagative")
        if mileage < 0:
            raise ValueError("Mileage can't be negative")
        self.speed = speed
        self.mileage = mileage


"""
Exercise 9:
Create a Student class and a Course class. Each Course can enroll students and print a list of enrolled students.
"""
class Student:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student(name={self.name!r})"

class Course:
    def __init__(self):
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def print_students(self):
        for s in self.students:
            print(s.name)



"""
Exercise 10:
Create a Flight class with a destination, departure time, and a list of passengers. Implement methods to add passengers, change the destination, and delay the flight by a certain amount of time.
"""
class Flight:
    def __init__(self, destination, departure):
        self.destination = destination
        self.departure = departure
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def change_destination(self, new_destination):
        self.destination = new_destination

    def delay(self, delay_time):
        if isinstance(self.departure, str) and ":" in self.departure:
            h, m = self.departure.split(":")
            h = int(h)
            m = int(m)
            h = (h + int(delay_time)) % 24
            self.departure = f"{h:02d}:{m:02d}"
            return

        if isinstance(self.departure, (int, float)):
            self.departure += delay_time
            return

        raise TypeError("Unsupported  format")

"""
Exercise 11:
Create a Library class with a list of Book objects. The Book class should have attributes for title and author. The Library class should have methods to add books and find a book by title.
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_title(self, title):
        for b in self.books:
            if b.title == title:
                return b
        return None



"""
Exercise 12:
Design a class Matrix that represents a 2D matrix with methods for addition, subtraction, and multiplication. Implement error handling for operations that are not allowed (e.g., adding matrices of different sizes).
"""
class Matrix:
    def __init__(self, matrix):
        if not matrix or not all(isinstance(row, list) and row for row in matrix):
            raise ValueError("Matrix must be a non-empty 2D list")
        row_len = len(matrix[0])
        if any(len(row) != row_len for row in matrix):
            raise ValueError("All rows must have the same length")
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = row_len

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Can't add matrices different size")
        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Can't subtrct matrices of different size")
        result = [
            [self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Can't multiplyyy columns of A must match rows of B")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                s = 0
                for k in range(self.cols):
                    s += self.matrix[i][k] * other.matrix[k][j]
                row.append(s)
            result.append(row)
        return Matrix(result)



"""
Exercise 13:
Create a class Rectangle with attributes for height and width. Implement methods for calculating the area and perimeter of the rectangle. Also, implement a method is_square that returns true if the rectangle is a square and false otherwise.
"""
class Rectangle:
    def __init__(self, height, width):
        if height < 0 or width < 0:
            raise ValueError("Height and width can't be negative")
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def is_square(self):
        return self.height == self.width
"""
Exercise 14:
Design a class Circle with attributes for radius. Implement methods for calculating the area and the circumference of the circle. Handle exceptions for negative radius values.
"""
class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius can't be negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius


"""
Exercise 15:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""
class Triangle:
    def __init__(self, side_a, side_b, side_c):
        a, b, c = side_a, side_b, side_c
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Triangl side must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle side")
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))



"""
Exercise 16:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""
class AbstractShape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

class Circle2(AbstractShape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cann't  be negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle2(AbstractShape):
    def __init__(self, height, width):
        if height < 0 or width < 0:
            raise ValueError("Height and width can't be negative")
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

class Triangle2(AbstractShape):
    def __init__(self, side_a, side_b, side_c):
        a, b, c = side_a, side_b, side_c
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Triangl sides must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides")
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


"""
Exercise 17:
Create a MusicPlayer class that contains a list of songs and methods to add songs, play a song, and skip to the next song. Also implement a method to shuffle the playlist.
"""
class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self.current_song = None
        self._index = 0

    def add_song(self, song):
        self.playlist.append(song)
        if self.current_song is None:
            self.current_song = song
            self._index = 0

    def play_song(self):
        if not self.playlist:
            self.current_song = None
            return None
        self.current_song = self.playlist[self._index]
        return self.current_song

    def next_song(self):
        if not self.playlist:
            self.current_song = None
            return None
        self._index = (self._index + 1) % len(self.playlist)
        return self.play_song()

    def shuffle(self):
        random.shuffle(self.playlist)
        self._index = 0
        self.play_song()




"""
Exercise 18:
Design a Product class for an online store with attributes for name, price, and quantity. Implement methods to add stock, sell product, and check stock levels. Include error handling for attempting to sell more items than are in stock.
"""
class Product:
    def __init__(self, name, price, quantity):
        if price < 0:
            raise ValueError("Price can't be negative")
        if quantity < 0:
            raise ValueError("Quantity can't be negative")
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Added quantit must be positive")
        self.quantity += quantity

    def sell(self, quantity):
        if quantity <= 0:
            raise ValueError("Sell quantity must be positive")
        if quantity > self.quantity:
            raise ValueError("Not enough  to sell")
        self.quantity -= quantity

    def check_stock(self):
        return self.quantity


"""
Exercise 19:
Create a VideoGame class with attributes for title, genre, and rating. Implement methods to change the rating, change the genre, and display game details.
"""
class VideoGame:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def change_rating(self, rating):
        self.rating = rating

    def change_genre(self, genre):
        self.genre = genre

    def display_details(self):
        return f"Title: {self.title}, Genre: {self.genre}, Rating: {self.rating}"


"""
Exercise 20:
Create a School class with a list of Teacher and Student objects. Teacher and Student classes should have attributes for name and age. The School class should have methods to add teachers, add students, and print a list of all people in the school.
"""
class Teacher(Person):
    pass

class Student(Person):
    def __init__(self, name, age=None):
        if age is None:
            self.name = name
            self.age = None
        else:
            super().__init__(name, age)

class School:
    def __init__(self):
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def get_all(self):
        return self.teachers + self.students

    def print_all(self):
        for p in self.get_all():
            if p.age is None:
                print(f"{p.name}")
            else:
                print(f"{p.name}, {p.age}")


"""
Exercise 21:
Design a Card class to represent a playing card with suit and rank. Then design a Deck class that uses the Card class. The Deck class should have methods to shuffle the deck, deal a card, and check the number of remaining cards.
"""
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if not self.cards:
            raise IndexError("Нет карт для сдачи")
        return self.cards.pop()

    def count(self):
        return len(self.cards)
