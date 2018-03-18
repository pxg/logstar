"""
https://filippo.io/instance-monkey-patching-in-python/
"""


class Class():
    def add(self, x, y):
        return x + y

old_boring_add = Class.add


def add_is_not_enough(self, x, y):
    return old_boring_add(self, x, y) + 1

inst = Class()
print(inst.add(3, 3))

Class.add = add_is_not_enough
print(inst.add(3, 3))
