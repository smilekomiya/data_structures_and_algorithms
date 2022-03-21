class HashSet:
    hash_set = {}
    def add(self, value):
        if value not in self.hash_set:
            self.hash_set[value] = True

    def clear(self):
        self.hash_set.clear()

    def remove(self, value):
        if self.contains(value):
            self.hash_set.pop(value)


    def contains(self, value):
        return value in self.hash_set

hash_set = HashSet()
hash_set.add(1)
hash_set.add("a")
print(hash_set.contains(2))
print(hash_set.contains("b"))
print(hash_set.contains("a"))
print(hash_set.contains(1))
hash_set.clear()
print(hash_set.contains(1))

