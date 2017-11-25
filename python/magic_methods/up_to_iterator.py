class CountUpToIterator(object):
    def __init__(self, up_to):
        self.next_number = 0
        self.up_to = up_to

    def __iter__(self):
        return self

    def __next__(self):
        n = self.next_number
        if self.next_number > self.up_to:
            raise StopIteration()
        else:
            self.next_number += 1
            return n

    next = __next__
