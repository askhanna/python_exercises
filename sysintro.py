import sys
if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("hello, world!", sys.argv[1])

for arg in sys.argv[1:]:
    print("hello, world!", arg) 

for arg in sys.argv[-1:]:
    print("hello, world!", arg) 
