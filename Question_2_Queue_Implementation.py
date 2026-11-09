# CRAWFORD UNIVERSITY
# Department of Computer Science
# 300 Level - Data Structures Assignment
#
# Question 2:
# Write an algorithm/program to implement a Queue data structure
# using the operations applicable to it.
#
# Written in Python using VS Code


# A queue follows FIFO:
# First In, First Out.
#
# Common applications of Queue:
# 1. Printer jobs
# 2. Customer service waiting lines
# 3. CPU/process scheduling
# 4. Handling requests in computer systems
# 5. Network data packets


# We use a Python list to implement the queue.
queue = []


# ENQUEUE operation
# Adds an item to the rear of the queue.
def enqueue(item):
    queue.append(item)
    print(item, "was added to the queue.")


# DEQUEUE operation
# Removes the first item from the queue.
def dequeue():
    if len(queue) == 0:
        print("Queue is empty. Nothing to remove.")
    else:
        removed = queue.pop(0)
        print(removed, "was removed from the queue.")


# FRONT operation
# Shows the first item in the queue.
def front():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Front item is:", queue[0])


# REAR operation
# Shows the last item in the queue.
def rear():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Rear item is:", queue[-1])


# IS EMPTY operation
def is_empty():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Queue is not empty.")


# SIZE operation
def queue_size():
    print("Queue size is:", len(queue))


# DISPLAY operation
def display_queue():
    print("\nCurrent Queue:")
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print(" -> ".join(queue))


# Test the queue operations
print("QUEUE DATA STRUCTURE")
print("====================")

print("\n--- ENQUEUE ---")
enqueue("Student A")
enqueue("Student B")
enqueue("Student C")
display_queue()

print("\n--- FRONT ---")
front()

print("\n--- REAR ---")
rear()

print("\n--- DEQUEUE ---")
dequeue()
display_queue()

print("\n--- SIZE ---")
queue_size()

print("\n--- IS EMPTY ---")
is_empty()

print("\n--- ADD ANOTHER ITEM ---")
enqueue("Student D")
display_queue()

print("\nProgram finished successfully.")
