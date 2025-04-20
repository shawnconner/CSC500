a = 1
b = 2
c = 3

if(a < b and b <c) :
    print("true")
else:
    print("false")

if(a < b and b <c and c < a) :
    print("true")
else:
    print("false")

if(a < b or  c < a) :
    print("true")
else:
    print("false")

if(c < a or (a < b and b <c )) :
    print("true")
else:
    print("false")