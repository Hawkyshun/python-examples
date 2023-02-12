class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, "r")
        self.lines = []
        
    def read(self):
        self.lines = [line for line in self.file]
        
    def count(self):
        return len(self.lines)
    
lc = LineCounter("/Users/furkanerdogan/Projects/Learning/Python/Learning/ex1.txt")

print(lc.lines)
print(lc.count())

lc.read()

#FP

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)

example_lines = read("/Users/furkanerdogan/Projects/Learning/Python/Learning/ex1.txt")
lines_count = count(example_lines)
print(lines_count)

#Anonymous Functions
def old_sum(a,b):
    return a+b

old_sum(4,5)

new_sum = lambda a,b: a+b
new_sum(4,5)

sirasiz_liste = [('b', 3), ('a', 8), ('d', 12), ('c', 1)]
sirasiz_liste

sorted(sirasiz_liste, key = lambda x: x[1])

