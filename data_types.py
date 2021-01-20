'''
Data types:
string
integer
float
boolean
dictionary
list
'''

# String s = "book"; in Java

s = 'book'
print(f"This is what s has {s}, and this is the type of the s {type(s)}")

i = 5
print(f"This is what i has {i}, and this is the type of the i {type(i)}")


f = 4.25
print(f"This is what f has {f}, and this is the type of the f {type(f)}")

b_true = True
b_false = False
print(f"This is what b_true has {b_true}, and this is the type of the b_true {type(b_true)}")
print(f"This is what b_false has {b_false}, and this is the type of the b_false {type(b_false)}")

d = {s : 'PythonLearning', 'language' : 'english', 'id' : i}
book_name = d[s]
lan = d['language']

print(f"This is what d has {d}, and this is the type of the d {type(d)}")
print(f"This is what d has and its book's name is {book_name}, and this is the type of the d {type(d)}")
print(f"This is what d has and its lan name is {lan}, and this is the type of the d {type(d)}")


l = [s, i, f, 'this is the list']

print(f"This is what list has {l}, and the type of the list is {type(l)}")