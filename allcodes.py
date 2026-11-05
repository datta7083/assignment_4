# # Q.1 even or odd number

# # num = int(input("enter a number: "))
# # if num % 2 == 0:
# #     print("even number")
# # else:
# #     print("odd number")
**************************************************************************************************************************************

# #Q.2 larggest of three numbers

# # a = int(input("enter first number: "))
# # b = int(input("enter second number: "))
# # c = int(input("enter third number: "))  

# # if a > b and a > c:
# #     print("a is largest number")

# # elif b > a and b > c:
# #     print("b is largest number")
# # else:
# #     print("largest number is c")
# # # check prime number
# # num =int(input("enter number:"))
# # if num <= 1:
# #     print("not prime number")
# # else:
# #     for i in range(2,num):
# #         if num % i == 0:
# #             print("not a prime number")
# #             break
# #     else:
# #         print("prime number")
**************************************************************************************************************************************

# #Q.3 chack prime number
# # num =int(input("enter number:"))
# # if num <= 1:
# #     print("not prime number")

# # else:
# #     for i in range(2,num):
# #         if num % i == 0:
# #             print("not a prime number")
# #             break
# #         else:
# #             print("prime number")
**************************************************************************************************************************************

# #Q.4 fibonacci series
# # n = int(input("enter number:"))

# # a = 0
# # b = 1
# # for i in range(n):
# #     print(a)
# #     c = a + b
# #     a = b
# #     b = c
**************************************************************************************************************************************

# # Q.5 factorial of a number

# # num = int(input("enter number:"))
# # fact = 1
# # if num < 0:
# #   print("factorial doen not possible")
# # else:
# #  for i in range(1,num+1):
# #    fact = fact * i
# #  print("factorial:",fact)

# # Q.6 reverse string without using [::-1]

# # text = input("enter string:")
# # reverse = ""
# # for ch in text:
# #     reverse = ch = reverse
# #     print("reverse string:",reverse)
**************************************************************************************************************************************

# 7. Check Palindrome String

# text = input("Enter a string: ")

# reverse = ""

# for ch in text:
#     reverse = ch + reverse

# if text == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
**************************************************************************************************************************************

# 8. Count Vowels and Consonants
# text = input("Enter a string: ")

# vowels = 0
# consonants = 0

# for ch in text.lower():

#     if ch.isalpha():

#         if ch in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)
**************************************************************************************************************************************

# 9. Sum of All Elements in a List

# numbers = [10, 20, 30, 40, 50]

# total = 0

# for num in numbers:
#     total = total + num

# print("Sum:", total)
**************************************************************************************************************************************

# Q.10 Write a program to find the largest and smallest elements in a list.

# numbers = [10, 50, 20, 5, 40]

# largest = numbers[0]
# smallest = numbers[0]

# for num in numbers:

#     if num > largest:
#         largest = num

#     if num < smallest:
#         smallest = num

# print("Largest:", largest)
# print("Smallest:", smallest)
**************************************************************************************************************************************

# Q. 11 Write a program to remove duplicate elements from a list.

# numbers = [10, 20, 10, 30, 20, 40]

# unique = []

# for num in numbers:

#     if num not in unique:
#         unique.append(num)

# print("Original List:", numbers)
# print("Unique List:", unique)
**************************************************************************************************************************************

# Q.12 Write a program to count how many times each element appears in a list using a dictionary.

# numbers = [10, 20, 10, 30, 20, 10]

# frequency = {}

# for num in numbers:

#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1

# print("Frequency:", frequency)
**************************************************************************************************************************************

# Q.13 Write a program to find the second-largest number in a list.

# numbers = [10, 20, 50, 30, 40, 50]

# largest = float('-inf')
# second = float('-inf')

# for num in numbers:

#     if num > largest:
#         second = largest
#         largest = num

#     elif num > second and num != largest:
#         second = num

# if second == float('-inf'):
#     print("Second largest does not exist")
# else:
#     print("Second Largest:", second)
**************************************************************************************************************************************

# Q.14 Write a program to sort a list without using built-in sorting functions.

# numbers = [50, 20, 40, 10, 30]

# n = len(numbers)

# for i in range(n):

#     for j in range(0, n-i-1):

#         if numbers[j] > numbers[j+1]:
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# print("Sorted List:", numbers)
**************************************************************************************************************************************

# Q.15 Write a function that accepts a list of numbers and returns a list containing only even numbers.

# def even_numbers(numbers):

#     result = []

#     for num in numbers:

#         if num % 2 == 0:
#             result.append(num)

#     return result


# my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# print("Even Numbers:", even_numbers(my_list))
**************************************************************************************************************************************

# Q.16 Write a program to find the frequency of each character in a string.

# text = input("Enter a string: ")

# frequency = {}

# for ch in text:

#     if ch in frequency:
#         frequency[ch] += 1
#     else:
#         frequency[ch] = 1

# print("Character Frequency:", frequency)
**************************************************************************************************************************************

# Q.17 Write a program to check whether two strings are anagrams of each other.

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# str1 = str1.replace(" ", "").lower()
# str2 = str2.replace(" ", "").lower()

# if sorted(str1) == sorted(str2):
#     print("Anagram Strings")
# else:
#     print("Not Anagram Strings")
**************************************************************************************************************************************

# Q.18. Find All Duplicate Values in a List

# numbers = [10, 20, 30, 10, 40, 20, 50]

# duplicates = []

# for num in numbers:

#     if numbers.count(num) > 1 and num not in duplicates:
#         duplicates.append(num)

# print("Duplicate Values:", duplicates)

**************************************************************************************************************************************

# Q.19 Write a program that takes a sentence and finds the longest word.

# sentence = input("Enter a sentence: ")

# words = sentence.split()

# longest = ""

# for word in words:

#     if len(word) > len(longest):
#         longest = word

# print("Longest Word:", longest)
# print("Length:", len(longest))
**************************************************************************************************************************************
# Q. 20 Create a simple student marks program that

# marks = []

# for i in range(1, 6):

#     mark = float(input(f"Enter marks for subject {i}: "))

#     marks.append(mark)

# total = sum(marks)

# percentage = total / 5

# print("\n----- STUDENT RESULT -----")

# print("Total Marks:", total)
# print("Percentage:", percentage, "%")

# if any(mark < 0 or mark > 100 for mark in marks):
#     print("Invalid Marks")

# elif any(mark < 35 for mark in marks):
#     print("Result: FAIL")
#     print("Grade: F")

# else:
#     print("Result: PASS")

#     if percentage >= 90:
#         print("Grade: A+")

#     elif percentage >= 80:
#         print("Grade: A")

#     elif percentage >= 70:
#         print("Grade: B")

#     elif percentage >= 60:
#         print("Grade: C")

#     elif percentage >= 50:
#         print("Grade: D")

#     else:
#         print("Grade: E")