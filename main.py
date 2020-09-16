

def rec(c,e):
    print(" "*e+"*"+"  "*c+"*")
    if c != 5:
         rec(c+1, e-1)
    print(" "*e+"*"+"  "*c+"*")


if __name__ == "__main__":
    print(" " * 5 + "*")
    rec(1 , 4)
    print(" "*5+"*")


