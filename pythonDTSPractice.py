#1 return the product of a and b...

from audioop import mul
from dataclasses import dataclass
from tabnanny import check

from numpy import empty, isin


def product(a, b):
    """Return product of a and b.
    """
    return a * b





#2 return name of weekday,only days between 1 and 7 otherwise None

def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    week_days = ["monday" , "tuesday" , "wednesday" , "thursday" , "friday" , "saturday" , "sunday"]
    if day_of_week >= 1 and day_of_week <= 7:
        return week_days[day_of_week - 1]
    if day_of_week < 1 or day_of_week > 7:
        return (f"{day_of_week} is not a valid week number")
    





#3 return last item in list (none if list is empty)

def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    

    if len(lst) != 0:
        return lst[len(lst) -1 ]
    else:
        return None




#4report on whether a>b , b>a or b==a
def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if a == b:
        print("Numbers are equal")
    if a < b:
        print("second is greater")
    if a > b:
        print("First is greater")




#5reverse string 
def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    new_phrase = phrase[::-1]



#6how many times does letter appear in word
def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    count = 0
    for char in word:
        if letter == char:
            count += 1


        
#7 return dict of {ltr: frequency} from phrase.
def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    new_dict = {}
    for letter in phrase:
        new_dict[letter] = new_dict.get(letter,0) + 1
    return new_dict
        

#8 list_manipulation
def list_manipulation(lst, command, location, value=None):
 
        if command == "remove":
            if location == "end":
                return lst.pop()
            elif location == "beginning":
                return lst.pop(0)
            
        if command == "add":
            if location == "beginning":
                return lst.insert(0 , value)
            elif location == "end":
                lst.append(value)
                print("added")


    
list1 = [1,2,3,4,5,6,7,8,9]
        
        


#9is phrase a palindrome,return true or false if phrase is a palindrome

def is_palindrome(phrase):
    reformed = phrase.lower().replace(" " , "")
    return reformed == reformed[::-1]

#10 return frequency of term in list
def frequency(lst,search_term):
    return lst.count(search_term)


#11 flip_case , change the case everytime it appears in a phrase or swap
def flip_case(phrase, to_swap):
    to_swap = to_swap.lower()
    out = ""
    for ltr in phrase:
        ltr = ltr.lower()
        if ltr == to_swap:
            ltr = ltr.swapcase()
        out += ltr
    return out

#12 multiply the even numbers if there are no even nums return 1
def multiply_even_numbers(nums):
    product = 1
    for num in nums:
        if num % 2 == 0:
            product = num * product
    return product

#13 capitalize first letter of first word of phrase
def capitalize(phrase):
    new_phrase = (phrase[:1].upper() + (phrase[1:]))


#14 compact return a list with non-true elements removed
def compact(lst):
    new_lst = []
    for el in lst:
        if el:
            new_lst.append(el)
    return new_lst
"""or return [val for val in lst if val]"""


#15 intersection , return intersection of two list as a new list
def intersection(l1 , l2):
    return [ val for val in l1 if val in l2]



#16 partition list by predicate a list and a function 
def is_even(num):
        return num % 2 == 0
def partition(lst,fn):
    green_list = []
    red_list = []
    for num in lst:
        if is_even(num):
            green_list.append(num)
        else:
            red_list.append(num)
    return [f"evens--> {green_list},             odds--> {red_list}"]


#17 mode , returns the most-common number in list
def mode(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num,0) + 1
    max_value = max(count.values())
    for (num , freq) in count.items():
        if freq == max_value:
            return num

"""print(mode([1,2,3,3,3,3]))"""

#18 calculate truncate when neccisary ( shortin to fit integeer )
def calculate( operation, a, b, make_int=False, message= "the result is"):
    if operation == "add":
        res = a + b
    elif operation == "subtract":
        res = a - b
    elif operation == "divide":
        res = a/b
    elif operation == "multiply":
        res = a * b
    else:
        return None
    
    if make_int == True:
        res = int(res)

    return (f"{message} {res}")
"""print(calculate("subtract",10,3,True,"the answer is"))"""

#19 friend_date , see if two friends have any hobbies in common
elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
def friend_date(a,b):
    if set(a[2]) & set(b[2]):
        return True
    else:
        return False
"""print(friend_date(elmo,sauron))"""

#20 triple_and_filter return new list of trippled numbers for those nums that are divisible by 4
def triple_and_filter(nums):
    new_list = []
    for num in nums:
        if num % 4 == 0:
            new_num = num * 3
            new_list.append(new_num)
    return new_list
"""print(triple_and_filter([33,43,22,66,86,22,4466,55,334,332,433,32,776,88,33,12,43,6453,333,121,434]))
"""

#21 extract_full_names, return list of names , extracting from first+last keys in people dicts
names = [
    {
        "first" : "lvictor",
        "last": "Taylor"
    },
    {
        "first" : "roger",
        "last": "Banks"
    }
]
def extract_full_names(people):
    return [f"{person['first']} {person['last']}" for person in people]
"""print(extract_full_names(names))"""


#22 return sum of floating point numbers in nums, only adds nums that are floats
def sum_floats(nums):
    new_list = []
    for num in nums:
        if type(num) == float:
            new_list.append(num)
    return new_list
"""print(sum_floats([1,2.4,2,4.5,7.8,3,2,4]))"""

#23 list_check are items in lst a list , check to see if all items are a list , return True or False
def list_check(lst):
    for item in lst:
        if not isinstance(item,list):
            return False
    return True
"""print(list_check([[1,2,3] , [2,3,4]]))"""


#24 return a new list of every other item in passed in OG list
def remove_every_other(lst):
    new_list = lst[::2]
    print(lst)
    return new_list
"""print(remove_every_other([1,2,3,4,5]))"""

#25 return tuple of the first pair that sums up to the goal
def sum_pairs(nums,goal):
    hold = 0
    for num in nums:
        hold = num
        for num in nums:
            if hold + num == goal:
                return(hold,num)
    return()

"""print(sum_pairs([1,2,3,4,3] , 5))"""

#26 vowel_count return frequency of vowels mapped into a dict
def vowel_count(phrase):
    mapped_letters = {}
    vowels = "aeiou"
    for char in phrase:
        lower_char = char.lower()
        if lower_char in vowels:
             mapped_letters[lower_char] = mapped_letters.get(lower_char,0) + 1
    return mapped_letters
"""print(vowel_count("How ARE YOU"))"""

#27 titleize this returns the string but only the first letter of each word in caps 
def titleize(phrase):
    return ' '.join([s.capitalize() for s in phrase.split(' ')])
"""print(titleize("YOU GIRL WhAt!"))"""

#28 find_factors 
def find_factors(num):
    factors = []
    n = 1
    while (n <= num):
        if num % n == 0:
            factors.append(n)
        n+= 1
    return factors
"""print(find_factors(892))"""

#29 create a function that looks for a certain item in an element and starts at a variable place for list
def includes(collection , search_term , start = None):
    if isinstance(collection,dict):
        return search_term in collection.values()
    if start == None or isinstance(collection,set):
        return search_term in collection
    else:
        return search_term in collection[start:]
"""print(includes([1,2,3,4] , 3, 1))"""

#30 repeat phrase the number of times you set it to 
def repeat(phrase , repeat_num):
    return (f"{phrase}  ") * repeat_num
"""print(repeat("hello" , 10))"""

#31 truncate a word that fits within a charactor that you pass in
def truncate(phrase, n):
    if n < len(phrase):
        return("number must be longer than phrase")
    if n > len(phrase):
        return phrase
    return phrase[:n -3 ] + "..."
"""print(truncate("hello" , 5))"""

#32 make a dictionary out of the keys and values you are givin, if fewer values than keys , remaining keys should have none 
def two_list_dictionary(keys,values):
    out = {}

    for (idx, val) in enumerate(keys):
        out[val] = values[idx] if idx < len(values) else None

    return out

"""print(two_list_dictionary([1,2,3,4],["yes" , "bye" , "hello"]))"""

#33 sum range sum up all the numbers , have params where to start , and end
def sum_range(nums , start = 0 , end = None):
    if end == None:
        end = len(nums)
    return sum(nums[start:end])
"""print(sum_range([1,2,3,4], 2))"""

#34 same frequency 
def freq_counter(input):
    count = {}
    for x in input:
        count[x] = count.get(x,0) + 1
    return count

def same_frequency(num1, num2):
    return (freq_counter(str(num1)) == freq_counter(str(num2)))
"""print(same_frequency(22112,21212))"""


#35 two_oldest_ages , get the two oldest ages from a list of numbers
def two_oldest_ages(ages):
    uniq_ages = set(ages)
    oldest = sorted(uniq_ages)[-2:]
    print(oldest)
"""two_oldest_ages([3,6,1,8,3,5,5])"""


#36 find_the_duplicate, return the duplicate if one is found in a list of nums
def find_the_duplicate(nums):
    uniques = []
    dups = []
    for num in nums:
        if num not in uniques:
            uniques.append(num)
        else:
            dups.append(num)
    print(dups)

"""find_the_duplicate([1,1,2,2,3,3])"""

#37 sum_up_diagonals
m1 = [
    [1,3,4],
    [4,2,5],
    [8,4,5]
]
def sum_up_diagonals(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-1 - 0]
    return total
"""print(sum_up_diagonals(m1))"""

#38 min_max_keys 
def min_max_keys(d):
    keys = d.keys()

    return (min(keys), max(keys))
"""print(min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}))"""
    

#39 find_greater_numbers
def find_greater_numbers(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                count += 1
    return count
print(find_greater_numbers([1,2,3,4,5]))




#40 is_odd_string
def is_odd_string(word):
    DIFF = ord("a") - 1

    total = sum((ord(c) - DIFF) for c in word.lower())

    return total % 2 == 1



#41 valid_parentheses
def valid_parentheses(parens):
    count = 0

    for p in parens:
        if p == '(':
            count += 1
        elif p == ')':
            count -= 1

        # fast fail: too many right parens
        if count < 0:
            return False

    return count == 0


#42 three odd numbers , return true if the next three numbers add up to be odd or even
def three_odd_numbers(nums):
     for i in range(len(nums) - 2):
        if (nums[i] + nums[i + 1] + nums[i + 2]) % 2 != 0:
            return True

     return False




#43 reverse vowels 
def reverse_vowels(s):
    vowels = set("aeiou")

    string = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1

    return "".join(string)


#44 read file and print it out 
def read_file_name(filename):
     with open(filename) as f:
        for line in f:
            # remove newline at end of line!
            line = line.strip()
            print(f"- {line}")






     
     
     
     
     
     
     
     
     
     
     
     
     
     
     




