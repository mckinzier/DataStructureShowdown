# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
"""
2. Running Total with Reset
Track a running total of values. If a negative number is added, reset the total to 0.
Input: [5, 7, -1, 3, 2]
Output: [5, 12, 0, 3, 5]
"""

def running_total(numbers):
    total = 0
    newNumbers = []
    for number in numbers:
        if number < 0:
            total = 0
        else:
            total += number
            newNumbers.append(total)
    return newNumbers

"tests"
print(running_total([5, 7, -1, 3, 2])) 
print(running_total([2, -3, -5, -5, 6, 6, -1])) 
print(running_total([10000, 50000,-600,10]))
print(running_total([]))
"print(running_total(['Magic', 'Wand']))"

"""
Reflection
-------------
The structure I chose was a list because its a simple data structure
that allows me to store the running total values. I see no reason to
any other data structure for this problem since it didn't require any
removing or adding of values anywhere in the list. All we needed to 
do was update values already in the list. The time limit didn't really 
shape my decision. Thirty minutes was an appropriate amount of time to 
complete the problem, given that I did it right. Likewise, I don't  
think I had any tradeoffs or compromises, again, unless I did it wrong?
I do often want to add options for a user to input their own values. I 
think if I was to do that, I'd need to think of more tests since I don't 
think of everything possible to test. That would be something I'd have to 
compromise on possibly? The tests gave me my expected outcomes; I would 
have liked to add a response to incorrect inputs but I didn't think about 
that until now, and don't have time remaining. I also feel it would be 
unnnecessary since I don't have a user giving an input. It's my own tests.
"""