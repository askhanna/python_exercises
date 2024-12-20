# a function named getCostOfCoffee() that has a parameters 
# named numberOfCoffees and pricePerCoffee.

def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    price = numberOfCoffees * pricePerCoffee
    discount = (numberOfCoffees // 9) * pricePerCoffee
    return price - discount

print(getCostOfCoffee(5, 5)) # 16 * 5 = 80
