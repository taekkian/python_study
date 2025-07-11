for i in range(0, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzBuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print("*")