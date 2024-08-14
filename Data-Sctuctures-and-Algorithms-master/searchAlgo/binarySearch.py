class SearchAlgorithms:

    def binarySearchIterative(self, key, elements):
        # Binary Search using Iterative approach.
        elements.sort()
        low = 0
        high = len(elements)-1
        mid = 0

        while low <= high:

            mid = (high+low)//2

            if elements[mid] < key:
                low = mid + 1
            elif elements[mid] > key:
                high = mid - 1
            else:
                return mid+1, True
        return False

    def binarySearchRecursive(self, key, elements, low, high):
        # Binary Search using Recursive approach.
        if high >= low:
            mid = (high + low)//2

            if elements[mid] == key:
                return mid+1, True
            elif elements[mid] > key:
                return self.binarySearchRecursive(key, elements, low, mid-1)
            else:
                return self.binarySearchRecursive(key, elements, mid+1, high)
        return False

    def dfs():
        return

    def bfs():
        return


key = 1
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

search = SearchAlgorithms()

print(search.binarySearchIterative(key, elements))

print(search.binarySearchRecursive(key, elements, 0, len(elements)-1))

