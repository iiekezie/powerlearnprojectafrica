# Task 1: Create a list of integers and compute the sum
nums = input("Enter a list of integers separated by spaces: ")
num_list = [int(n) for n in nums.split()]
print("Sum of numbers:", sum(num_list))


# Task 2: Tuple of favorite books and print each
books = ("1984", "To Kill a Mockingbird", "The Great Gatsby", "Sapiens", "The Alchemist")
for book in books:
    print(book)


# Task 3: Dictionary for personal info
person = {}
person["name"] = input("Enter your name: ")
person["age"] = input("Enter your age: ")
person["favorite_color"] = input("Enter your favorite color: ")
print("Person Dictionary:", person)


# Task 4: Sets with common elements
set1 = set(map(int, input("Enter integers for Set 1 (space-separated): ").split()))
set2 = set(map(int, input("Enter integers for Set 2 (space-separated): ").split()))
common = set1 & set2
print("Common elements:", common)


# Task 5: List of words, filter those with odd number of characters
words = ["apple", "banana", "grape", "mango", "kiwi", "orange"]
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("Words with odd length:", odd_length_words)
