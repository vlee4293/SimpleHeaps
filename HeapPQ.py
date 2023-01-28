# Simple priority queue using my heap class


import Heaps
import random


def main():
    queue = Heaps.MaxHeap()
    for customer in random.choices(range(0, 60), k=10):
        queue.insert(customer)
    print(queue.heap)
    for customer in range(queue.index+1):
        print(f"Processing {queue.heap[0]}")
        queue.remove()


if __name__ == "__main__":
    main()