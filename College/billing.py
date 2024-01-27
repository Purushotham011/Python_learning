#while purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 1000. If quantity and price per item are input through the keyboard,write a program to calculate the total expenses

quantity=int(input("Enter the quantity : "))

price=int(input("Enter the price : "))

def tot_exp(q,p):
    if quantity>1000:
        discount=quantity*0.1
        total=quantity*price-discount
        print("Total expenses :",total)
    else:
        total=quantity*price
        print("Total expenses :",total)

tot_exp(quantity,price)