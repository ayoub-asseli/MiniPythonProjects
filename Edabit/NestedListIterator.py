"""
Implement a class iterator to flatten a nested list of lists of integers. Each list element is either an integer or a list. There can be many levels of nested lists in lists.

The class initializes with a nested list. It also has two methods:

next() returns an integer in the order of appearance.
hasNext() returns True / False regarding if all integers have been retrieved or not.
Write the Class implementation for three required methods.

Example

ni, actual = NestedIterator([[1, 1], 2, [1, 1]]), []
while ni.hasNext():
    actual.append(ni.next())
actual ➞ [1, 1, 2, 1, 1]

"""

class NestedIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.count_elem = 0
        self.counter = 0
        for l in nested_list:
            if type(l) != list:
                self.counter += 1
            else:
                self.counter += len(l)

    def next(self):
        print(self.nested_list)
        for l in self.nested_list:
            if type(l) != list:
                self.count_elem += 1
                del self.nested_list[self.nested_list.index(l)]
                print(l)
                return l
            else:
                for i in range(len(l)):
                    self.count_elem += 1
                    elem = l[i]
                    del l[i]
                    print(elem)
                    return elem

    def hasNext(self):
        print('counter:', self.counter)
        print('count_elem:', self.count_elem)
        if self.count_elem != self.counter:
            return True
        else:
            return False
