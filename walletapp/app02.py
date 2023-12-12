
def selection01():
    a = 33
    b = 200
    if b > a:
        print("b is greater than a")  # This line starts with indent


def selection02():
    a = 330
    b = 200
    if b > a:
        print("b is greater than a")

    print("b is greater than a") # Example of logic error

def selection03():
    a = 200
    b = 3300
    if b > a:
        print("b is greater than a")
    else:
        print("b is not greater than a")


def selection04():
    a = 3300
    b = 200
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")


def forloop01():
    fruits = ["apple", 15, "banana", "cherry","potato","tomato"]
    #1111 --> 15

    print(len(fruits))

    for x in fruits:
        print ('There is the ' + str(x)) #Casting int() float()

def forloop02():
    full_name = 'Assumption university'
    print(len(full_name))

    for x in full_name:
        if x != ' ':
            print ('The alphabet is ' + x)


def whileloop01():
    i = 1
    sum = 0
    while i < 6:
        sum += i # 1 + 2 + 3 +4 + 5
        i += 1

    print(sum)


def whileloop02():
    # Start at 10
    # increase by 5
    # End with 200
    # 10 + 15 + 20 + ... + 200
    i = 10
    sum = 0
    while i < 205:
        sum += i # 1 + 2 + 3 +4 + 5
        i += 5 # i = i + 5

    print(sum)

def forloop03():
    # Exact problem with whileloop02

    nums = range(10,201,5)
    sum = 0
    for x in nums:
        # print(x)
        sum += x
    print(sum)