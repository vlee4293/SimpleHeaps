# Simple sorting using my heap class


import random
import Heaps


def main():
    unsorted = [round(random.normalvariate(100, 15), 2) for _ in range(100)]
    print("Unsorted:", unsorted)

    minimum = Heaps.MinHeap()
    maximum = Heaps.MaxHeap()

    for item in unsorted:
        minimum.insert(item)
        maximum.insert(item)

    sorted_min = []
    sorted_max = []

    for _ in range(len(unsorted)):
        sorted_min.append(minimum.heap[0])
        sorted_max.append(maximum.heap[0])
        minimum.remove()
        maximum.remove()

    print("Min:", sorted_min)
    print("Max:", sorted_max)


if __name__ == "__main__":
    main()
