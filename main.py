import random

def my_pi():
    my_range = range(0,500000)
    #count_1_4th_circle = 0
    my_circle_count = 0
    my_square_count = 0

    for i in my_range:
        x = random.randint(-1000,1000)
        y = random.randint(-1000,1000)

        if pow(x, 2) + pow(y, 2) <= 1000000:
            my_circle_count += 1

        if (x>=0) and (y>=0):
            my_square_count += 1
            #count_1_4th_circle += 1

    return my_circle_count / my_square_count

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(my_pi())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
