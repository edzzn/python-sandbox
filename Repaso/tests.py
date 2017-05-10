
import random


def bubble_sort(items):
    """ Implementation of bubble sort """
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] < items[j+1]:
                items[j], items[j + 1] = items[j + 1], items[j]  # Swap!



random_items = [random.randint(-50, 100) for c in range(32)]

print ('Before: ', random_items)
bubble_sort(random_items)
print ('After : ', random_items)


