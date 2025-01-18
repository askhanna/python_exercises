import turtle

def koch(t, length):
  """
  Draws a Koch curve using the given turtle and length.

  Args:
    t: A turtle object.
    length: The length of the Koch curve.
  """

  if length < 30:
    t.forward(length)
  else:
    koch(t, length/3)
    t.left(60)
    koch(t, length/3)
    t.right(120)
    koch(t, length/3)
    t.left(60)
    koch(t, length/3)


if __name__ == "__main__":
  length = input("Enter turtle length: ")
  t = turtle.Turtle()
  koch(t,int(length))
  #t.forward(10)
  turtle.done()
