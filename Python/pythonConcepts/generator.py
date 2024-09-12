"""
def remote_next():
    yield "cnn"
    yield "espn"                # yiels is like return keyword but its use is slightly different from return

itr = remote_next()
print(next(itr))             #here we can see the use of yield statement how it works
print(next(itr))
"""

def fib():
    a,b = 0,1

    while True:
        yield a
        a,b = b,a+b

for f in fib():
    if f > 10:
        break
    print(f)

"""
generators are better than class based iterator
- no need to define iter() and next() methods
- no need to raise StopIteration exception
"""

