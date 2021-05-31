def enterProducts():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input("Press A to add product and Q to quit: ")
        if details == "A":
            product = input("Enter product: ")
            quantity = int(input("Enter quantity: "))
            buyingData.update({product: quantity})
        elif details == "Q":
            enterDetails = False
        else:
            print("Please select a correct option")
    return buyingData


def getPrice(product, quantity):
    priceData = {
        'Biscuit': 3,
        'Chicken': 5,
        'Egg': 1,
        'Fish': 3,
        'Coke': 2,
        'Bread': 2,
        'Apple': 3,
        'Onion': 3
    }
    subtotal = priceData[product] * quantity
    print(product + ':$' +
          str(priceData[product]) + 'x' + str(quantity) + '=' + str(subtotal))
    return subtotal


def getDiscount(billAmount, membership):
    discount = 0
    if billAmount >= 25:
        if membership == 'Gold':
            billAmount = billAmount * 0.80
            discount = 20
        elif membership == 'Silver':
            billAmount = billAmount*0.90
            discount = 10
        elif membership == 'Bronze':
            billAmount = billAmount*0.95
            discount = 5
        print(str(discount) + "% off for " + membership +
              " " + "membership on  total amount: $" + str(billAmount))
    else:
        print("No discount on amount less than $25")
    return billAmount


def makeBill(buyingData, membership):
    billAmount = 0
    for key, value in buyingData.items():
        billAmount += getPrice(key, value)
    billAmount = getDiscount(billAmount, membership)
    print("The discounted amount is $" + str(billAmount))


buyingData = enterProducts()
membership = input("Enter customer membership: ")
makeBill(buyingData, membership)
