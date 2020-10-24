# First Python Project
from Container import *

container1 = Container("OCL", "Clothes")
container2 = Container("MAS", "Electronics")
container3 = Container("AML", "Foods")
container4 = Container._create_empty_container("BML")

while True:
    print("please provide a number: 12")
    response = input()
    if (int(response) % 7 == 0):
        print("it's reminder of 0")
        break
    else:
        print("not a reminder of 7.")
