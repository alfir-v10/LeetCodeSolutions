[Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o(1))
```Python
from random import choice


class RandomizedSet:
    def __init__(self):
        self.set = {}
        self.elem = []

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set[val] = len(self.elem)
        self.elem.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        last_element, idx_to_remove = self.elem[-1], self.set[val]
        self.elem[idx_to_remove], self.set[last_element] = last_element, idx_to_remove
        self.elem.pop()
        del self.set[val]
        return True

    def getRandom(self) -> int:
        return choice(self.elem)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

```Python
from random import choice
class RandomizedSet:

    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        if len(self.set):
            return choice(list(self.set))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```