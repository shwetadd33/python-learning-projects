# Iterator is used to iterating through the different type of data structures (list,dict,tuple)

a = ["hey","bro","you'r","awsome"]
print(dir(a)) # __iter__ is a built in function
"""
itr = iter(a)
print(itr)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
"""

itr = reversed(a)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


class RemoteControl():
    def __init__(self):
        self.channels = ["HBO","CNN","POGO","ESPN"]
        self.index = -1

    def __iter__(self):
        return self     # It will return self object

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration

        return self.channels[self.index]


r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))