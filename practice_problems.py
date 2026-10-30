"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    seen = set()
    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)
    return False
"""
Write a 2–3 sentence comment justifying: 
(1) Why this data structure fits the task and 
(2) what operations are performed and their expected runtime

1) The problem was asking to check for duplicates in a list of product IDs. You need a set
to do that since it lets you iterate through the lsit and check if there are any matches. 
The problem didn't ask to return the duplicates or save them but just validate there being
duplicates or not.
2) The operations performed would be iteratting through the lsit of product IDS and checking 
if there are any matches. The runtime would be o(n) because you iterate through the entire list.
"""

"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        self.task = []

    def add_task(self, task):
        self.task.append(task)

    def remove_oldest_task(self):
        return self.task.pop(0) if self.task else None

"""
Write a 2–3 sentence comment justifying: 
(1) Why this data structure fits the task and 
(2) what operations are performed and their expected runtime

1) The problem was asking for a structurefd way of going about things, removing tasks 
in the front and adding next tasks to the back. That is a queue so that method is what should be used.
2) The operations performed add new tasks to the bacl of the queue and remove older or completed tasks from the front.
Runtime would be 0(1) to add tasks and 0(n) to remove tasks since you have to shift the whole list over when you remove
a task fromt he front
"""
"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.unique_values = set()

    def add(self, value):
        self.unique_values.add(value)

    def get_unique_count(self):
        return len(self.unique_values)

"""  
Write a 2–3 sentence comment justifying: 
(1) Why this data structure fits the task and 
(2) what operations are performed and their expected runtime

1) This problem asked for a way to keep tarck of unique values within a stream of integers.
It also wants you to be able to return the number of unique values. A set should be used 
because it allows you to add values and will handle the duplicates itself.
2) The operations performed are iterating through the stream of integers and keeping track of
the unique values. The runtime would be 0(1) because you're jsut adding values """