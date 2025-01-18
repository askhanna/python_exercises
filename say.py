import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.stegosaurus("Hello " + sys.argv[1])