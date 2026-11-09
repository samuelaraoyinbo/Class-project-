# CRAWFORD UNIVERSITY
# Department of Computer Science
# 300 Level - Data Structures Assignment
#
# Question 1:
# Find real applications of Stack and where it is operational.
# Also pick an array and perform stack operations on it.
#
# Written in Python using VS Code


# A stack follows LIFO:
# Last In, First Out.
#
# Real applications of Stack:
# 1. Undo and Redo operations in applications.
# 2. Browser history - going back to a previous page.
# 3. Function calls in a program - the call stack stores functions.
# 4. Checking brackets in programming expressions.
# 5. Reversing words or strings.
#
# Stack is operational in places such as:
# - Text editors
# - Web browsers
# - Programming languages and compilers
# - Mobile and desktop applications
# - Algorithms that need backtracking


# Example array of students
students = ["David", "Samuel", "Blessing", "Daniel", "Mary"]

# We will use the last position of the list as the top of the stack.
stack = students.copy()


def display_stack():
    print("\nCurrent Stack:")
    if len(stack) == 0:
        print("Stack is empty")
    else:
        for student in reversed(stack):
            print(student)


# PUSH operation
# Adds an item to the top of the stack.
def push(item):
    stack.append(item)
    print(item, "was pushed into the stack.")


# POP operation
# Removes the item at the top of the stack.
def pop_item():
    if len(stack) == 0:
        print("Stack is empty. Nothing to remove.")
    else:
        removed = stack.pop()
        print(removed, "was popped from the stack.")


# PEEK operation
# Shows the item at the top without removing it.
def peek():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Top item is:", stack[-1])


# Check if the stack is empty
def is_empty():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Stack is not empty.")


# SIZE operation
def stack_size():
    print("Stack size is:", len(stack))


# Perform the operations
print("STACK DATA STRUCTURE")
print("====================")

display_stack()

print("\n--- PUSH ---")
push("Joshua")
display_stack()

print("\n--- PEEK ---")
peek()

print("\n--- POP ---")
pop_item()
display_stack()

print("\n--- SIZE ---")
stack_size()

print("\n--- IS EMPTY ---")
is_empty()
