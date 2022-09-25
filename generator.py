import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    numbers = string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
a = open('usernames.txt', 'a+')
try:
    ad = input("> Name Starts With (Leave Blank For Random) : ")
    am = int(input("> Amount Of Letters : "))
    d = int(input("> Amount To Generate : "))
except:
    print("Please enter a valid number!")
while d > 0:
    ca = am - len(ad)
    n = ad + get_random_string(ca)
    a.write(n + "\n")
    d -= 1
