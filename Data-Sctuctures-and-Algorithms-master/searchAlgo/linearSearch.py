class LinearSearch:

    def linearSearch(self, key, elements):
        for i in range(len(elements)):
            if key == elements[i]:
                return i+1, True

        return False


key = 2
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

ls = LinearSearch()
print(ls.linearSearch(key, elements))
