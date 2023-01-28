# Bare-bones Min-Max Heap Implementation


import math


class MaxHeap:

    def __init__(self):
        self.heap = []
        self.index = -1

    def insert(self, item):

        # Add the item to the end of the tree and heapify
        self.index += 1
        self.heap.append(item)
        self.heapify_up(self.index)

    def remove(self):

        # Swap the root with the newest item
        self.heap[0], self.heap[self.index] = self.heap[self.index], self.heap[0]

        # Remove the last item and heapify
        self.heap.pop(self.index)
        self.index -= 1
        self.heapify_down(0)

    def heapify_up(self, child):
        parent = math.floor((child-1)/2)

        # Check if the tree is empty and if the child is larger than the parent
        if parent != -1 and self.heap[child] > self.heap[parent]:

            # Swap the child with the parent and recursively move up the tree
            self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
            self.heapify_up(parent)

    def heapify_down(self, parent):
        large = parent
        left = parent*2+1
        right = parent*2+2

        # Check if the left child exists and if it is larger than the parent
        if left <= self.index and self.heap[left] > self.heap[large]:
            large = left

        # Check if the right child exists and if it is larger than the parent
        if right <= self.index and self.heap[right] > self.heap[large]:
            large = right

        # Check if there was a change in "large" due to the above conditions
        if large != parent:

            # Swap the larger child with the parent and recursively move down the tree
            self.heap[large], self.heap[parent] = self.heap[parent], self.heap[large]
            self.heapify_down(large)


class MinHeap:

    def __init__(self):
        self.heap = []
        self.index = -1

    def insert(self, item):

        # Add the item to the end of tree and heapify
        self.index += 1
        self.heap.append(item)
        self.heapify_up(self.index)

    def remove(self):

        # Swap the root with the newest item
        self.heap[0], self.heap[self.index] = self.heap[self.index], self.heap[0]

        # Remove the last item and heapify
        self.heap.pop(self.index)
        self.index -= 1
        self.heapify_down(0)

    def heapify_up(self, child):
        parent = math.floor((child-1)/2)

        # Check if the tree is empty and if the child is smaller than the parent
        if parent != -1 and self.heap[child] < self.heap[parent]:

            # Swap the child with the parent and recursively move up the tree
            self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
            self.heapify_up(parent)

    def heapify_down(self, parent):
        small = parent
        left = parent*2+1
        right = parent*2+2

        # Check if the left child exists and if it is smaller than parent
        if left <= self.index and self.heap[left] < self.heap[small]:
            small = left

        # Check if right child exists and if it is smaller than parent
        if right <= self.index and self.heap[right] < self.heap[small]:
            small = right

        # Check if there was a change in "small" due to the above conditions
        if small != parent:

            # Swap the smaller child with the parent and recursively move up the tree
            self.heap[small], self.heap[parent] = self.heap[parent], self.heap[small]
            self.heapify_down(small)
