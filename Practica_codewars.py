# import re


# def friend(x):
#     new_names= []
#     for str in x:
#         if len(str)== 4:
#            new_names.append (str)
#     return new_names



# def tower_builder(n_floors):
#     list=[n_floors]
#     for i in range

# Create a function that takes an integer as an argument and
# returns "Even" for even numbers or "Odd" for odd numbers.

# def add_binary(a,b):
#     binary = str(bin(sum_num))
#     return  binary

# Check to see if a string has the same amount of 'x's and 'o's.
# The method must return a boolean and be case insensitive.
#  The string can contain any char.

# Examples dna/output:

# XO("ooxx") => true

# from ast import While


# def xo(s):
#     x=0
#     o=0
#     for i in range (s):
#         if "x" in s:
#             x +=1
#         elif "o" in s:
#             o +=1
#         if x == o:
#             return True
#     else:
#         return False




# Given two integers, which can be positive and negative, find the sum of all the numbers between including them too and return it. If both numbers are equal return a or b.
# Note! a and b are not ordered!
# Example:
# get_sum(1, 0) == 1   // 1 + 0 = 1
# def get_sum(a,b):
#     if a == b:
#         return a
#     s = 0
#     for n in range(min(a,b), max(a,b)+1):
#         s += n
#     return s

from ast import Return
from asyncio import events
from audioop import reverse
from ntpath import join
from operator import ne
from pickle import FALSE
import re
from tkinter import N
from tkinter.messagebox import RETRY
from unicodedata import digit


def century(year):
    while  True:
        year -=1
        year // 100
        return  year

def find_smallest_int(arr):
    x= min(arr)
    return x

def find_smallest_int(arr):
    low_num =[arr]
    for i in range (arr):
        if i< low_num:
            return low_num

def sum_two_smallest_numbers(numbers):
    list = [numbers]
    x= min [list]
    list.delete (min)
    c= min (numbers)
    return x + c

def solution(string, ending):
    if string.endswith (ending):
        return True
    else:
        return False

# Complete the function that accepts a string parameter,
#  and reverses each word in the string. All spaces in the string should be retained.
def reverse_words(text):
    text [::-1]
    return text
reverse_words("The quick brown fox jumps over the lazy dog.")



def filter_list(l):
    filter_number = []
    for x in l:
        if type(x)== int:
            filter_number.append(x)
    return filter_number





def bouncingBall(h, bounce, window):
    if h != 0 and bounce > 0 and bounce < 1 and window < h:
      count = 1
      current = h*bounce
    while current > window:
       current *= bounce
       count += 2
        return count


def make_negative( number ):
    if number == 0:
        return 0
    elif number< 0:
        return number
    else:
        for i in range (number):
            number =number - number *2
            return number

# ATM machines allow 4 or 6 digit PIN codes and PIN
# codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.
def validate_pin(pin):
    if len(pin) in (4, 6) and pin.isdigit():
        return True
    else:
        return False

# It's pretty straightforward. Your goal is to create a function that removes the first
# and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.


def remove_char(str):
    newS = ''
    for index in range(len(str)):
        if (index != 0 and index != len(str) - 1):
            newS += str[index]

    return newS
# There is an array with some numbers.
# All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

def find_uniq(arr):
    arr.sort()
    n = arr[len(arr)-1]
    return n


def string_to_number(s):
    return(int (s))

# Convert number to reversed array of digits
# Given a random non-negative number,
# you have to return the digits of this number within an array in reverse order.

def digitize(n):
    number=[]
    for i in n:
        [-1]
        number.append(i)
        return number



# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.

def find_average(numbers):
   return sum(numbers)/len(numbers)


def odd_or_even(arr):
    if sum(arr) % 2 != 0:
        return "odd"
    else :
        return "even"

def greet(name):
    name = dna()
    print ("Hello,", name," how are you doing today?.")

# Write function RemoveExclamationMarks which removes all exclamation marks
# from a given string.

def remove_exclamation_marks(s):

    return(s.replace('!', ''))

# Given a non-empty array of integers,
# return the result of multiplying the values together in order. Example:

# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

def grow(arr):
    multi = 1
    for x in arr:
        multi= multi * x
        return multi

import numpy
def grow(arr):
    a = numpy.prod(arr)
    return a

# Write a function that takes an array of numbers and returns the sum of the numbers.
#  The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.
def sum_array(a):
    sum = 0
    for i in a:
        sum += i
    return sum

def sum_array(a):
  return sum(a)

# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

def get_count(sentence):
    num_vowels=0
    for char in sentence:
        if char in "aeiouAEIOU":
            num_vowels = num_vowels+1
    return num_vowels

# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9


def opposite(number):
  return number - number *2


# Write function a that calculates body mass index (a = weight / height2).

# if a <= 18.5 return "Underweight"

# if a <= 25.0 return "Normal"

# if a <= 30.0 return "Overweight"

# if a > 30 return "Obese"

def bmi(weight, height):
    a= weight/height**2
    if a <= 18.5:
        return "Underweight"
    elif a <= 25.0 :
        return "Normal"
    elif a <= 30.0:
        return "Overweight"
    elif a > 30:
        return "Obese"

def smash(words):
    return " ".join(words) if len(words) >= 1 else ""

# Write a function to split a string
# and convert it into an array of words. For example:
# "Robin Singh" ==> ["Robin", "Singh"]

def string_to_array(s):
    a= ["".join(s)]
    if " " in s:
        return a

# Your task is to find the first element of an array that is not consecutive.

# By not consecutive we mean not exactly 1 larger than the previous element of the array.

def first_non_consecutive(arr):
    i =arr
    for i in arr:
        i +=1
        if i != arr:
            return i


def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"


# Write a program that finds the summation of every number from 1 to num.
# The number will always be a positive integer greater than 0.

def summation(num):

    result = 0
    count = 1

    while count <= num:
        result += count
        count += 1

    return result


# You will be given an array of numbers.
# You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
def sort_array(source_array):
   new= min(source_array)

def sort_odds(lst):
    sorted_odds = sorted([n for n in lst if n%2])
    new_list = []
    for n in lst:
        if n%2:
            new_list.append(sorted_odds.pop(0))
        else:
            new_list.append(n)
    return list(new_list)


def number_to_string(num):
    return str(num)

# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 !=0:
        return True
    elif flower1 % 2 != 0 and flower2 % 2 ==0:
        return True
    else:
        return False

def double_integer(i):
    return i *2

def make_upper_case(s):
    return s.upper()

def sum_mix(arr):
  sum = 0
  for num in arr:
    sum += int(num)
  return sum


def likes(names):
    if names == "":
        return None
    for i in names:
       return i,"likes this"


def duplicate_encode(word):
  chars = []
  word = word.lower()
  for char in word:
    if word.count(char) == 1:
      chars.append("(")
    else:
      chars.append(")")
  return "".join(chars)


# You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

# Write a code that gives out the total amount for different days(d).

def rental_car_cost(days):
    costPerday = 40
    total_cost= costPerday * days
    if days>= 7:
        total_cost -=50
    elif days>= 3:
        total_cost -=20
    return total_cost

# Implement a function that accepts 3 integer values a, b, c.
# The function should return true if a triangle can be built with the sides of given length and false in any other case.

def is_this_a_triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (c + a > b):
        return True
    else:
        return False
# Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).
def twice_as_old(dad_years_old, son_years_old):
    for i in new_father_year:
        new_father_year= dad_years_old -1
        if son_years_old * 2 == new_father_year:
            return new_father_year

def twice_as_old(dad_years_old, son_years_old):
    doubled_sons_age = son_years_old * 2
    if dad_years_old >= doubled_sons_age:
        return dad_years_old - doubled_sons_age
    else:
        return doubled_sons_age - dad_years_old



def productFib(prod):
    current_value = 0
    x = 0
    fib1 = fib2 = 0

    while current_value < prod:
        x += 1
        fib1 = fib(x)
        fib2 = fib(x + 1)
        current_value = fib1 * fib2

    if current_value == prod:
        return [fib1, fib2, True]
    return [fib1, fib2, False]


def fib(n):
    a,b = 1,1

    for i in range(n-1):
        a,b = b,a+b
    return a


def hoop_count(n):
    if n>=10:
        return "Great, now move on to tricks"

    else:
        return "Keep at it until you get it"

# Your task is to create a function that does four basic mathematical operations.

# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

def basic_op(operator, value1, value2):
    if operator== "+":
        return value1 + value2
    elif operator== "-":
        return value1 - value2
    elif operator== "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    for i in s:
        if s.isupper():
            return "".join

# Task
# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

# The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

# Mind the dna validation.

def sum_array(arr):
    if not arr or len(arr) <= 2:
        return 0
    else:
        arr.sort()
        return sum(arr[1:-1])

def greet(name, owner):
    if name or owner =="owner":
        return "Hello boss"
    else:
        return "Hello guest"
        
# Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.

# For example: ["3:1", "2:2", "0:1", ...]

# Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:

# if x>y - 3 points
# if x<y - 0 point
# if x=y - 1 point

def points(games):
    our_points = 0
    for game in games:
        if game[0] > game[2]:
            our_points = our_points + 3
        elif game[0] == game[2]:
            our_points = our_points + 1
        else: #it is okay to ignore the else case here
            pass
    return our_points


def open_or_senior(data):
    outpout=[]
    for i in data:
        if i[0]>=55 and i[1]>7:
            outpout.append('Senior')
        else:
             outpout.append('Open')
    return outpout

def openOrSenior(data):
    output = []
    for i in data:
        if i[0] > 54 and i[1] > 7:
            output.append('Senior')
        else:
            output.append('Open')
    return output

# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

def correct(s):
    for i in s:
        if i==5:
            s=s.replace(i,5)
        elif i== 0:
            return "O"
        elif i == 1:
            return "I"
def correct(string):
    mis = {"0":"O", "5":"S", "1":"I"}
    for c in string:
        if c in mis:
            string = string.replace(c, mis[c])
    return string

def check(seq, elem):
    if (seq)>=1 and (elem)>1:
        return True
    else:
        return False

# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).

def find_odds(seq):
    odds = set()
    contador= 0
    for x in seq:
        if x % 2 != 0:
            contador += 1
        if contador % 2 !=0:

# The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

# For example:

# 1.08 --> 30


def cockroach_speed(s):
    return s * 27.778


def cockroach_speed(s):
    i= s / 0.036
    return int(i)

# The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.

# In effect: 89 = 8^1 + 9^2

# The next number in having this property is 135.

# See this property again: 135 = 1^1 + 3^2 + 5^3

# We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    for i in a,b:
        if  a**1  + b**2 == i:
            return [i]
def sum_dig_pow(a, b):
    res = []
    for num in range(a, b + 1):
        summed = sum(int(d) ** (idx + 1) for idx, d in enumerate(str(num)))
        if summed == num:
            res.append(num)
    return res
# You are given an odd-length array of integers, in which all of them are the same, except for one single number.

# Complete the method which accepts such an array, and returns that single different number.

# The dna array will always be valid! (odd-length >= 3)
def stray(arr):
    for num in arr:
        if arr.count(num) == [1][0]:
            return num


# Task Overview:
# You have to write a function that accepts three parameters:

# cap is the amount of people the bus can hold excluding the driver.
# on is the number of people on the bus excluding the driver.
# wait is the number of people waiting to get on to the bus excluding the driver.
# If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.
def enough(cap, on, wait):
    number_of_passenger = cap - on -wait
    if number_of_passenger >= 0:
        return 0
    else:
        return number_of_passenger



def area_or_perimeter(l , w):
    if l == w:
        return l*w
    elif l != w:
        return l*2+w*2
# Simple, remove the spaces from the string, then return the resultant string.
def no_space(x):
    return x.replace(" ","")


def invert(lst):
    for i in lst:
        return i *-1
# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.
def quarter_of(month):
    if month<=3:
        return 1
    elif month <=6:
        return 2
    elif month<=9:
        return 3
    else:
        return 4
# Write a function named setAlarm which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.

def set_alarm(employed, vacation):
    if employed ==True and vacation == False:
        return True
    else:
        return False

def count_positives_sum_negatives(arr):
    contador = 0
    a=0
    for i in arr:
        if i>0 and i<0:
            contador +=1
            return contador and sum(i)
        else:
            return [a]

def minimum(arr):
    return min(arr)
def maximum(arr):
    return max(arr)

# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: dna will never be an empty string

def fake_bin(x):
    result =""
    a=x
    for i in a:
        if int(i)>=5:
            result ="1"
        else:
            result ="0"
    return result

def fake_bin(x):
  result = "";
  stringNum = x;
  for digit in stringNum:
    if int(digit) >= 5:
      result += "1";
    if int(digit) < 5:
      result += "0";
  return result;


def solution(string):
    return string[-1]


def order(sentence):
    for i in sentence:
      if i.isdigit():
          return sentence

def how_much_i_love_you(nb_petals):
    means = ["not at all", "I love you", "a little", "a lot", "passionately", "madly"]
    return means[nb_petals % 6]


def increment_string(strng):
    x= 1
    for i in strng:
        if strng[::-1].isdigit():
            return strng +1
        else:
            return strng + x

def sort_by_length(arr):
    i= sorted(arr)
    return i
# Will you make it?
# You were camping with your friends far away from home,
# but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left. Considering these factors, write a function that tells you if it is possible to get to the pump or not. Function should return true (1 in Prolog and NASM) if it is possible and false (0 in Prolog and NASM) if not. The dna values are always positive.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump<= mpg * fuel_left:
        return True
    else:
        return False



def DNA_strand(dna):
    output = ''
    a=[]
    for letter in dna:
        letter = letter.upper()

        if letter == 'A':
            output += 'T'
        elif letter == 'T':
            output += 'A'
        elif letter == 'G':
            output += 'C'
        else:
            output += 'G'

    return(output[::-1])

# You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.

# Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.

def update_light(current):
    if current== "green":
        return "yellow"
    elif current== "yellow":
        return "red"
    else:
        return "green"
def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]
# A hero is on his way to the castle to complete his mission.
# However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

# Return True if yes, False otherwise :)

def hero(bullets, dragons):
    while bullets >= dragons*2:
        return True
    else:
        return False
def hero(bullets, dragons):
    return bullets >= dragons * 2

# Your task is to create the functionisDivideBy (or is_divide_by) to check if an integer number is divisible by both integers a and b.

def is_divide_by(number, a, b):
    if number % a==0 and number % b ==0:
        return True
    else:
        return False
def is_divide_by(number, a, b):
    return number % a == 0 and number % b == 0

# Create a function with two arguments that will return an array of the first (n) multiples of (x).

# Assume both the given number and the number of times to count will be positive numbers greater than 0.

# Return the results as an array (or list in Python, Haskell or Elixir)

def count_by(x, n):
    new_array=[]
    for i in range(1,n+1):
        i * n
        new_array.append (i)
        return new_array
def count_by(x, n):
    for i in range(n+1):
        return i * x

# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.

# You receive an array with your peers' test scores. Now calculate the average and compare your score!

# Return True if you're better, else False!

def better_than_average(class_points, your_points):
    if sum(class_points)< your_points* len(class_points)
        return True
    else:
        return False

# Your task is to make function, which returns the sum of a sequence of integers.

# The sequence is defined by 3 non-negative values: begin, end, step (inclusive).

# If begin value is greater than the end, function should returns 0
def sequence_sum(begin_number, end_number, step):
    for i in end_number:
        new_sum= sum (begin_number+step)==end_number
        if begin_number > end_number:
            return 0
        else:
            return new_sum
def sequence_sum(begin_number, end_number, step):
    return sum([i for i in range(begin_number, end_number+1, step)])

# You are given an array with positive numbers and a non-negative number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.You are given an array with positive numbers and a non-negative number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.
def index(array, n):
    if len(array)> n:
        return array[n]**n
    else:
        return -1
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

# For example:

# time = 3 ----> litres = 1
def litres(time):
    return int(time * 0.5)

def boolean_to_string(b):
    return str(b)
# Your task is to write function findSum.

# Upto and including n, this function will return the sum of all multiples of 3 and 5.

# For example:

# findSum(5) should return 8 (3 + 5)

def find(n):
    x= []
    for i in range(1,n):
        if i%3 or i%5 ==0:
            x.append(i)
    return sum(x)
def find(number):
    result = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)

    return sum(result)
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
def expanded_form(num):
    a=[]
    i= []
    residuo= num % 10 == a
    a= residuo% 10 == i
    return a ,"+",i

# Build a function that returns an array of integers from n to 1 where n>0.

# Example : n=5 --> [5,4,3,2,1]

def reverse_seq(n):
    for i in range(n-1):
        print (n)
def reverseseq(n):
    return list(range(1,n+1))[::-1]
        
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga+ copaDelRey+championsLeague
# Kata Task
# I have a cat and a dog.

# I got them at the same time as kitten/puppy. That was humanYears years ago.

# Return their respective ages now as [humanYears,catYears,dogYears]


# humanYears >= 1
# humanYears are whole numbers only
def human_years_cat_years_dog_years(human_years):
    new_age=[humanYears,catYears,dogYears]
    for i in human_years:
        if catyears
        return [0,0,0]
def final_grade(exam, projects):
    if exam>=90 or projects>=10:
        return 100
    elif exam>=75 and projects>=5:
        return 90
    elif exam>=50 and projects>=2:
        return 75
    else:
        return 0
def final_grade(exam, projects):
  if exam > 90 or  projects > 10: return 100
  if exam > 75 and projects >= 5: return 90
  if exam > 50 and projects >= 2: return 75
  return 0
# In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

# The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

# Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

# You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

# The string has a length greater or equal to one and contains only letters from ato z.
def printer_error(s):
    letter_allowed= ("a,b,c,d,e,f,g,h,,i,j,k,l,m")
    counter=0
    for i in s:
        if i not in letter_allowed:
            counter +=1
    # return (counter%"/"%len(s))
    return str(counter)+"/"+str(len(s))
# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

def longest(s1, s2):
    return "".join(sorted([c for c in set(s1 + s2)]))

# When provided with a number between 0-9, return it in words.

# Input :: 1

# Output :: "One".

# If your language supports it, try using a switch statement.
def switch_it_up(number):
    if number == 0 : return "Zero"
    if number == 1 : return "One"
    if number == 2 : return "Wwo"
    if number == 3 : return "Whree"
    if number == 4 : return "Four"
    if number == 5 : return "Five"
    if number == 6 : return "Six"
    if number == 7 : return "Seven"
    if number == 8 : return "Eigth"
    if number == 9 : return "Nine"

def switch_it_up(n):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

def unique_in_order(iterable):
    return "".join(sorted([c for c in set(iterable)]))

# Terminal game move function
# In this game, the hero moves from left to right. The player rolls the die and moves the number of spaces indicated by the die two times.

# Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.
def move(position, roll):
    return roll *2 + position
 Can you find the needle in the haystack?

# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:   
def find_needle(haystack):
    a= "found the needle at position", index
    for i in haystack:
        index= haystack.index('needle')
        return a
def find_needle(haystack):
    position = 0
    for range in haystack:
        if (range == 'needle'):
            return 'found the needle at position %s' % (position)
        else:
            position += 1
# squares = [ i for i in range(1, 100000) if i % 4== 0 and i %6 ==0 and i%9==0]
# print(squares)

def run():
    my_dict={}
    for i in range(1,101):
        if i % 3 !=0:
            my_dict[i]= i**3
    print(my_dict)

def runs():
    my_dict={i: i**3 for i in range(1,101)if i%3!=0 }

# Create a method is_uppercase() to see whether the string is ALL CAPS. For example:
def is_uppercase(inp):
    if inp.isupper():
        return True
    elif inp==[]:
        return True
    else: 
        return False

def is_uppercase(inp):
    return inp.isupper()
else:
    return True
def is_uppercase(inp):
    if inp.isupper():
        return True
    elif inp=="$%&":
        return True
    else: 
        return False
# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# For example (Input --> Output):

# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, a
def persistence(n):
    n.sort()
    while <10:
        n*
def persistence(n):
    # your code
  s = 0
  i = 1
  temp = 1
  t = 1
  while n > 9:
    temp = str (n)
    for j in range(len(temp)):
      t *= int(temp[j])
    s += 1
    n = t
    t = 1
  return s


# Clock shows h hours, m minutes and s seconds after midnight.

# Your task is to write a function which returns the time since midnight in milliseconds.

def past(h, m, s):
    seconds_hour= h*3600 
    seconds_minute= m* 60
    seconds= s *1 
    miliseconds= seconds_hour+seconds_minute+seconds 
    return miliseconds *1000


def find_short(s):
    for i in s:
        return (len(s.sort()))
def is_anagram(test, original):
    if original == test[::-1]:
        return True
    else:
        return False

# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.
def rps(p1, p2):
    if p1 =="scissors" and p2=="paper": return "Player 1 won!"
    if p1 =="rock" and p2=="scissors": return "Player 1 won!"
    if p1 =="paper" and p2=="rock": return "Player 1 won!"
    if p1 == p2: return "Draw"
    else:
        return "Player 2 won!"
# Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.
def sum_digits(number):
   a = number.split()
   b= list(a)
   return sum(b)

def sum_digits(number):
  number = abs(number);       #Make all digits positive
  total = 0;
  digits = list(str(number));
  for digit in digits:
    num = int(digit);
    total += num;
  return total;

def multiply(a,b):
    return a * b

# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present 
# in the array (true means present).

def count_sheeps(sheep):
    count= 0
    for i in sheep:
        if i == True:
            count += 1
    return count
# Story
# Ben has a very simple idea to make some profit: he buys something and sells it again.
#  Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.
def min_max(lst):
  a= min(lst)
  b= max(lst)
  return [a, b]

This function should test if the factor is a factor of base.

Return true if it is a factor or false if it is not.

About factors
Factors are numbers you can multiply together to get another number.

2 and 3 are factors of 6 because: 2 * 3 = 6

# You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
# You can use the mod operator (%) in most languages to check for a remainder
# For example 2 is not a factor of 7 because: 7 % 2 = 1

# Note: base is a non-negative number, factor is a positive number.  
def check_for_factor(base, factor):
    if factor % base ==0 or base % factor== 0 :
        return True
    else:
        return False
# Grade book
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

def get_grade(s1, s2, s3):
    average_note = (s1 + s2 + s3) // 3
    if average_note >= 90:
        return 'A'
    elif average_note >= 80:
        return 'B'
    elif average_note >= 70:
        return 'C'
    elif average_note >= 60:
        return 'D'   
    else:
        return 'F'
# Exclusive "or" (xor) Logical Operator
# Overview
# In some scripting languages like PHP, there exists a logical operator (e.g. &&, ||, and, or, etc.) called the "Exclusive Or" (hence the name of this Kata). The exclusive or evaluates two booleans. It then returns true if exactly one of the two expressions are true, false otherwise 

def xor(a,b):
    if a == True and b == True:
        return False
    elif a== True or b== True:
        return True
    else:
        return False

# Description:
# Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.
def replace_exclamation(s):
    vowels = "aeiouAEIOU"
    if vowels in s:
        return s.replace(vowels,'!')

# Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):
def sum_str(a, b):
    x= sum(a,b)
    return  x


# We want an array, but not just any old array, an array with contents!

# Write a function that produces an array with the numbers 0 to N-1 in it.

# For example, the following code will result in an array containing the numbers 0 to 4:

def arr(n): 
    for i in range(n):
        if n:
    return i


    
def arr(n=0):
    return [i for i in range(n)] if n else []


# ask
# Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ()
# In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained
def expression_matter(a, b, c):
    operation = [
        a*(b+c),
        a*b*c,
        a+b *c,
        (a+b)*c,
        a+b+c,
        a*b+c 
                ]
    return max(operation)

# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.
def to_jaden_case(string):
    for i in string:
        if " " in i:
            return string.upper
# Given an integer as input, can you round it to the next (meaning, "higher") multiple of 5?

def round_to_next5(n):
    a= n% 5
    if n%5 !=0:
        aux= a-5
        aux_2= aux* -1 +a
        return int(aux_2 *n)
    else:
        return n
nearest_multiple = base * round(a_number/base)
def round_to_next5(n):
    nearest_multiple = 5* round(n/5)
    if n ==0 or n==5:
        return n +5
    else:
        return nearest_multiple
def round_to_next5(n):
    nearest_multiple = 5* round(n/5)
    while True:
        return nearest_multiple
    else:
        return n+5

# Sum of odd numbers
def row_sum_odd_numbers(n):
    odd_numbers=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 
    35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63
    , 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 
    85, 87, 89, 91, 93, 95, 97 , 99]
    for n in odd_numbers:
        return n + odd_numbers
# Task
# Given a list of digits, return the smallest number that could be formed from these digits, using the digits only once (ignore duplicates).
def min_value(digits):
    return min(digits)

# Count the number of divisors of a positive integer n.

# Random tests go up to n = 500000.
def divisors(n):
    for i in range(n+1):
        if n % i==0:
            return i

def divisors(n):
    count = 1
    i = 1
    while i <= n/2:
        if n % i == 0:
            count += 1
        i += 1
    return count
# Ask a small girl - "How old are you?". She always says strange things... Lets help her!

# For correct answer program should return int from 0 to 9.

# Assume test input string always valid and may look like "1 year old" or "5 years old", etc.. The first char is number only.

def get_age(age):
    a= int( age[:1])
    return a

# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
def double_char(s):
    while len(s)in i:
        for i  in s:    
            return i*2
def double_char(s):
    res = ''
    for i in s:
        res += i*2
    return res
# Bob needs a fast way to calculate the volume of a cuboid with three values: length, width and the height of the cuboid. Write a function to help Bob with this calculation
def getVolumeOfCubiod(length, width, height):
    return length*width*height

# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order
def array_diff(a, b):
    new_list= []
    for i in a:
        if i not in b:
            new_list.append(i)
    return new_list

# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421
def descending_order(num):
    for i in num:
        new_list= sorted(i)
        a= new_list[::-1] 
    return a
def Descending_Order(num):
    return int("".join(map(str, sorted([i for i in str(num)], reverse=True))))

# Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n (inclusive).
def powers_of_two(n):
    i=1
    x=[]
    for i in n:
        d=x.append(i*2)
    return d

def square_sum(numbers):
    for num in numbers:
        return sum(num*num)

# Make a function that returns the value multiplied by 50 and increased by 6. 
# If the value entered is a string it should return "Error".
def problem(a):
    x= a*50+6
    if x.is_integer()== False:
        return "False"
    else:
        return x


def repeat_to_at_least_length(s, wanted):
    a= s * wanted
    return  a


# Use variables to find the sum of the goals Messi scored in 3 competitions
la_liga_goals= 43
champions_league_goals= 10
copa_del_rey_goals= 5
total_goals =la_liga_goals + champions_league_goals + copa_del_rey_goals
print (la_liga_goals + champions_league_goals + copa_del_rey_goals)

# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    new_arr= 0
    for i in arr:
        if i > 0:
            new_arr += i
    return new_arr
def positive_sum(arr):
    sum = 0
    for number in arr:
        if number > 0:
            sum += number
    return sum

def reverse(st):
    # Your Code Here
    return st
# You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:

# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
def reverse_words(str):
  strList = []
  for word in str.split(' '):
      strList.append(word[::-1])
  return ' '.join(strList)    

def reverse_words(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence 

def rev_sentence(sentence): 
  
    # first split the string into words 
    words = sentence.split(' ') 
  
    # then reverse the split string list and join using space 
    reverse_sentence = ' '.join(reversed(words)) 
  
    # finally return the joined string 
    return reverse_sentence 

# You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. If they are, return true. Else, return false.

# You can assume all values in the array are numbers.
def small_enough(array, limit):
    if max(array) <= limit:
            return True
    else:
        return False

# In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b
# . You must find the difference of the cuboids' volumes regardless of which is bigger.
import math
def find_difference(a, b):
    cuboide1= math.prod(a)
    cuboide2= math.prod(b)
    rest= cuboide1-cuboide2
    return abs (rest)


def positive_sum(arr):
    new=0
    for i in arr:
        if i>0:
            new += i
    return new

def square_digits(num):
    num.separ()
    for i in num:
        return 
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
def square_digits(num):
    r = ''
    for l in str(num):
     r = r + str((int(l))**2)



def xo(s):
    number_of_x= []
    number_of_o = []
    for i in s:
        if i == x or i == 