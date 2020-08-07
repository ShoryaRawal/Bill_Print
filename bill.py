import subprocess
import pandas 

def one() :
    item1 = str(input("Item name: "))
    item1_price = int(input("Price: "))
    item1_quantity = int(input("quantity: "))

    item1_subtotal = item1_price * item1_quantity
    total = item1_subtotal

    List = {"Name":[item1], "Price":[item1_price], "Quantity":[item1_quantity], "Subtotal":[item1_subtotal]}
    df = pandas.DataFrame(List)
    print(df)
    print("Total - " + str(total))

def two() :
    item1 = input("First Item: ")
    item1_price = input("Price(single): ")
    item1_quantity = input("Quantity: ")
    
    print("\n")
    
    item2 = input("Second Item: ")
    item2_price = input("Price: ")
    item2_quantity = input("quantity: ")
    
    print("\n")
 
    item1_subtotal = int(item1_price) * int(item1_quantity)
    item2_subtotal = int(item2_price) * int(item2_quantity)

    total = item1_subtotal + item2_subtotal

    List = {"Name":[item1, item2], "Price":[item1_price, item2_price], "Quantity":[item1_quantity, item2_quantity], "Subtotal":[item1_subtotal, item2_subtotal]}
    df = pandas.DataFrame(List)
    print(df)
    print("total: " + str(total))

def three() :
    item1 = input("First item: ")
    item1_price = input("Price: ")
    item1_quantity = input("quantity: ")
    print("\n")

    item2 = input("Second item: ")
    item2_price = input("Price: ")
    item2_quantity = input("Quantity: ")

    print("\n")

    item3 = input("Third name:")
    item3_price = input("Price: ")
    item3_quantity = input("Quantity: ")

    print("\n")
    
    item1_subtotal = int(item1_price) * int(item1_quantity)
    item2_subtotal = int(item2_price) * int(item2_quantity)
    item3_subtotal = int(item3_price) * int(item3_quantity)

    total = item1_subtotal + item2_subtotal + item3_subtotal

    List = {"Name":[item1, item2, item3], "Price":[item1_price, item2_price, item3_price], "Quantity":[item1_quantity, item2_quantity, item3_quantity], "subtotal":[item1_subtotal, item2_subtotal, item3_subtotal]}
    df = pandas.DataFrame(List)
    print(df)
    print("Total - " + str(total))

def four() :
    item1 = input("First Item: ")
    item1_price = input("Price: ")
    item1_quantity = input("Quantity: ")

    print("\n")

    item2 = input("Second item: ")
    item2_price = input("Price: ")
    item2_quantity = input("Quantity: ")

    print("\n")

    item3 = input("Third item: ")
    item3_price = input("Price: ")
    item3_quantity = input("Quantity: ")

    print("\n")

    item4 = input("Fourth Item: ")
    item4_price = input("Price: ")
    item4_quantity = input("Quantity: ")

    item1_subtotal = int(item1_price) * int(item1_quantity)
    item2_subtotal = int(item2_price) * int(item2_quantity)
    item3_subtotal = int(item3_price) * int(item3_quantity)
    item4_subtotal = int(item4_price) * int(item4_quantity)

    total = item1_subtotal + item2_subtotal + item3_subtotal + item4_subtotal

    List = {"Name":[item1, item2, item3, item4], "Price":[item1_price, item2_price, item3_price, item4_price], 
            "Quantity":[item1_quantity, item2_quantity, item3_quantity, item4_quantity], "subtotal":[item1_subtotal, item2_subtotal, item3_subtotal, item4_subtotal]}

    df = pandas.DataFrame(List)
    print(df)
    print("Total" + str(total))

def five() :
    item1 = input("First Item: ")
    item1_price = input("Price: ")
    item1_quantity = input("Quantity: ")

    print("\n")

    item2 = input("Second Item: ")
    item2_price = input("Price: ")
    item2_quantity = input("Qunatity: ")

    print("\n")

    item3 = input("Third Item: ")
    item3_price = input("Price: ")
    item3_quantity = input("Quantity: ")

    print("\n")

    item4 = input("Fourth Item: ")
    item4_price = input("Price: ")
    item4_quantity = input("Quantity: ")

    print("\n")

    item5 = input("Fifth Item: ")
    item5_price = input("Price: ")
    item5_quantity = input("Quantity: ")

    item1_subtotal = int(item1_price) * int(item1_quantity)
    item2_subtotal = int(item2_price) * int(item2_quantity)
    item3_subtotal = int(item3_price) * int(item3_quantity)
    item4_subtotal = int(item4_price) * int(item4_quantity)
    item5_subtotal = int(item5_price) * int(item5_quantity)

    total = item1_subtotal + item2_subtotal + item3_subtotal + item4_subtotal + item5_subtotal
    List = {"Name":[item1, item2, item3, item4, item5],
            "Price":[item1_price, item2_price, item3_price, item4_price, item5_price], 
            "Quantity":[item1_quantity, item2_quantity, item3_quantity, item4_quantity, item5_quantity],
            "Subtotal":[item1_subtotal, item2_subtotal, item3_subtotal, item4_subtotal, item5_subtotal]}
    df = pandas.DataFrame(List)
    print(df)
    print("Total = " + str(total))

def six() :
    item1 = input("First Item: ")
    item1_price = input("Price: ")
    item1_quantity = input("Quantity: ")

    print("\n")

    item2 = input("Second Item: ")
    item2_price = input("Price: ")
    item2_quantity = input("Qunatity: ")

    print("\n")

    item3 = input("Third Item: ")
    item3_price = input("Price: ")
    item3_quantity = input("Quantity: ")

    print("\n")

    item4 = input("Fourth Item: ")
    item4_price = input("Price: ")
    item4_quantity = input("Quantity: ")

    print("\n")

    item5 = input("Fifth Item: ")
    item5_price = input("Price: ")
    item5_quantity = input("Quantity: ")

    print("\n")

    item6 = input("Sixth Item: ")
    item6_price = input("Price: ")
    item6_quantity = input("Quantity: ")

    item1_subtotal = int(item1_price) * int(item1_quantity)
    item2_subtotal = int(item2_price) * int(item2_quantity)
    item3_subtotal = int(item3_price) * int(item3_quantity)
    item4_subtotal = int(item4_price) * int(item4_quantity)
    item5_subtotal = int(item5_price) * int(item5_quantity)
    item6_subtotal = int(item6_price) * int(item6_quantity)

    total = item1_subtotal + item2_subtotal + item3_subtotal + item4_subtotal + item5_subtotal + item6_subtotal
    List = {"Name":[item1, item2, item3, item4, item5, item6],
            "Price":[item1_price, item2_price, item3_price, item4_price, item5_price, item6_price], 
            "Quantity":[item1_quantity, item2_quantity, item3_quantity, item4_quantity, item5_quantity, item6_quantity],
            "Subtotal":[item1_subtotal, item2_subtotal, item3_subtotal, item4_subtotal, item5_subtotal, item6_subtotal]}
    df = pandas.DataFrame(List)
    print(df)
    print("Total = " + str(total))

def seven() :
    item1 = input("First Item: ")
    item1_price = input("Price: ")
    item1_quantity = input("Quantity: ")

    print("\n")

    item2 = input("Second Item: ")
    item2_price = input("Price: ")
    item2_quantity = input("Qunatity: ")

    print("\n")

    item3 = input("Third Item: ")
    item3_price = input("Price: ")
    item3_quantity = input("Quantity: ")

    print("\n")

    item4 = input("Fourth Item: ")
    item4_price = input("Price: ")
    item4_quantity = input("Quantity: ")

    print("\n")

    item5 = input("Fifth Item: ")
    item5_price = input("Price: ")
    item5_quantity = input("Quantity: ")

    print("\n")

    item6 = input("Sixth Item: ")
    item6_price = input("Price: ")
    item6_quantity = input("Quantity: ")

    print("\n")

    item7 = input("Seventh Item: ")
    item7_price = input("Price: ")
    item7_quantity = input("Quantity: ")

    item1_subtotal = int(item1_price) * int(item1_quantity)
    item2_subtotal = int(item2_price) * int(item2_quantity)
    item3_subtotal = int(item3_price) * int(item3_quantity)
    item4_subtotal = int(item4_price) * int(item4_quantity)
    item5_subtotal = int(item5_price) * int(item5_quantity)
    item6_subtotal = int(item6_price) * int(item6_quantity)
    item7_subtotal = int(item7_price) * int(item7_quantity)

    total = item1_subtotal + item2_subtotal + item3_subtotal + item4_subtotal + item5_subtotal + item6_subtotal + item7_subtotal
    List = {"Name":[item1, item2, item3, item4, item5, item6, item7],
            "Price":[item1_price, item2_price, item3_price, item4_price, item5_price, item6_price, item7_price], 
            "Quantity":[item1_quantity, item2_quantity, item3_quantity, item4_quantity, item5_quantity, item6_quantity, item7_quantity],
            "Subtotal":[item1_subtotal, item2_subtotal, item3_subtotal, item4_subtotal, item5_subtotal, item6_subtotal, item7_subtotal]}
    df = pandas.DataFrame(List)
    print(df)
    print("Total = " + str(total))

def eight() :
    item1 = input("First Item: ")
    item1_price = input("Price: ")
    item1_quantity = input("Quantity: ")

    print("\n")

    item2 = input("Second Item: ")
    item2_price = input("Price: ")
    item2_quantity = input("Qunatity: ")

    print("\n")

    item3 = input("Third Item: ")
    item3_price = input("Price: ")
    item3_quantity = input("Quantity: ")

    print("\n")

    item4 = input("Fourth Item: ")
    item4_price = input("Price: ")
    item4_quantity = input("Quantity: ")

    print("\n")

    item5 = input("Fifth Item: ")
    item5_price = input("Price: ")
    item5_quantity = input("Quantity: ")

    print("\n")

    item6 = input("Sixth Item: ")
    item6_price = input("Price: ")
    item6_quantity = input("Quantity: ")

    print("\n")

    item7 = input("Seventh Item: ")
    item7_price = input("Price: ")
    item7_quantity = input("Quantity: ")

    print("\n")
    item8 = input("Eirght Item: ")
    item8_price = input("Price: ")
    item8_quantity = input("Quantity: ")

    item1_subtotal = int(item1_price) * int(item1_quantity)
    item2_subtotal = int(item2_price) * int(item2_quantity)
    item3_subtotal = int(item3_price) * int(item3_quantity)
    item4_subtotal = int(item4_price) * int(item4_quantity)
    item5_subtotal = int(item5_price) * int(item5_quantity)
    item6_subtotal = int(item6_price) * int(item6_quantity)
    item7_subtotal = int(item7_price) * int(item7_quantity)
    item8_subtotal = int(item8_price) * int(item8_quantity)

    total = item1_subtotal + item2_subtotal + item3_subtotal + item4_subtotal + item5_subtotal + item6_subtotal + item7_subtotal + item8_subtotal
    List = {"Name":[item1, item2, item3, item4, item5, item6, item7, item8],
            "Price":[item1_price, item2_price, item3_price, item4_price, item5_price, item6_price, item7_price, item8_price], 
            "Quantity":[item1_quantity, item2_quantity, item3_quantity, item4_quantity, item5_quantity, item6_quantity, item7_quantity, item8_quantity],
            "Subtotal":[item1_subtotal, item2_subtotal, item3_subtotal, item4_subtotal, item5_subtotal, item6_subtotal, item7_subtotal, item8_subtotal]}
    df = pandas.DataFrame(List)
    print(df)
    print("Total = " + str(total))

def nine() :
    item1 = input("First Item: ")
    item1_price = input("Price: ")
    item1_quantity = input("Quantity: ")

    print("\n")

    item2 = input("Second Item: ")
    item2_price = input("Price: ")
    item2_quantity = input("Qunatity: ")

    print("\n")

    item3 = input("Third Item: ")
    item3_price = input("Price: ")
    item3_quantity = input("Quantity: ")

    print("\n")

    item4 = input("Fourth Item: ")
    item4_price = input("Price: ")
    item4_quantity = input("Quantity: ")

    print("\n")

    item5 = input("Fifth Item: ")
    item5_price = input("Price: ")
    item5_quantity = input("Quantity: ")

    print("\n")

    item6 = input("Sixth Item: ")
    item6_price = input("Price: ")
    item6_quantity = input("Quantity: ")

    print("\n")

    item7 = input("Seventh Item: ")
    item7_price = input("Price: ")
    item7_quantity = input("Quantity: ")

    print("\n")
    item8 = input("Eirght Item: ")
    item8_price = input("Price: ")
    item8_quantity = input("Quantity: ")

    print("\n")

    item9 = input("Ninth Item: ")
    item9_price = input("Price: ")
    item9_quantity = input("Qantity: ")

    item1_subtotal = int(item1_price) * int(item1_quantity)
    item2_subtotal = int(item2_price) * int(item2_quantity)
    item3_subtotal = int(item3_price) * int(item3_quantity)
    item4_subtotal = int(item4_price) * int(item4_quantity)
    item5_subtotal = int(item5_price) * int(item5_quantity)
    item6_subtotal = int(item6_price) * int(item6_quantity)
    item7_subtotal = int(item7_price) * int(item7_quantity)
    item8_subtotal = int(item8_price) * int(item8_quantity)
    item9_subtotal = int(item9_price) * int(item9_quantity)

    total = item1_subtotal + item2_subtotal + item3_subtotal + item4_subtotal + item5_subtotal + item6_subtotal + item7_subtotal + item8_subtotal + item9_subtotal
    List = {"Name":[item1, item2, item3, item4, item5, item6, item7, item8, item9],
            "Price":[item1_price, item2_price, item3_price, item4_price, item5_price, item6_price, item7_price, item8_price, item9_price], 
            "Quantity":[item1_quantity, item2_quantity, item3_quantity, item4_quantity, item5_quantity, item6_quantity, item7_quantity, item8_quantity, item9_quantity],
            "Subtotal":[item1_subtotal, item2_subtotal, item3_subtotal, item4_subtotal, item5_subtotal, item6_subtotal, item7_subtotal, item8_subtotal, item9_subtotal]}
    df = pandas.DataFrame(List)
    print(df)
    print("Total = " + str(total))

def ten() :
    item1 = input("First Item: ")
    item1_price = input("Price: ")
    item1_quantity = input("Quantity: ")

    print("\n")

    item2 = input("Second Item: ")
    item2_price = input("Price: ")
    item2_quantity = input("Qunatity: ")

    print("\n")

    item3 = input("Third Item: ")
    item3_price = input("Price: ")
    item3_quantity = input("Quantity: ")

    print("\n")

    item4 = input("Fourth Item: ")
    item4_price = input("Price: ")
    item4_quantity = input("Quantity: ")

    print("\n")

    item5 = input("Fifth Item: ")
    item5_price = input("Price: ")
    item5_quantity = input("Quantity: ")

    print("\n")

    item6 = input("Sixth Item: ")
    item6_price = input("Price: ")
    item6_quantity = input("Quantity: ")

    print("\n")

    item7 = input("Seventh Item: ")
    item7_price = input("Price: ")
    item7_quantity = input("Quantity: ")

    print("\n")
    
    item8 = input("Eirght Item: ")
    item8_price = input("Price: ")
    item8_quantity = input("Quantity: ")

    print("\n")

    item9 = input("Ninth Item: ")
    item9_price = input("Price: ")
    item9_quantity =  input("Quantity: ")

    print("\n")

    item10 = input("Tenth Item: ")
    item10_price = input("Price: ")
    item10_quantity = input("Quantity: ")

    item1_subtotal = int(item1_price) * int(item1_quantity)
    item2_subtotal = int(item2_price) * int(item2_quantity)
    item3_subtotal = int(item3_price) * int(item3_quantity)
    item4_subtotal = int(item4_price) * int(item4_quantity)
    item5_subtotal = int(item5_price) * int(item5_quantity)
    item6_subtotal = int(item6_price) * int(item6_quantity)
    item7_subtotal = int(item7_price) * int(item7_quantity)
    item8_subtotal = int(item8_price) * int(item8_quantity)
    item9_subtotal = int(item9_price) * int(item9_quantity)
    item10_subtotal = int(item10_price) * int(item10_quantity)

    total = item1_subtotal + item2_subtotal + item3_subtotal + item4_subtotal + item5_subtotal + item6_subtotal + item7_subtotal + item8_subtotal + item9_subtotal + item10_subtotal
    List = {"Name":[item1, item2, item3, item4, item5, item6, item7, item8, item9, item10],
            "Price":[item1_price, item2_price, item3_price, item4_price, item5_price, item6_price, item7_price, item8_price, item9_price, item10_price], 
            "Quantity":[item1_quantity, item2_quantity, item3_quantity, item4_quantity, item5_quantity, item6_quantity, item7_quantity, item8_quantity, item9_quantity, item10_quantity],
            "Subtotal":[item1_subtotal, item2_subtotal, item3_subtotal, item4_subtotal, item5_subtotal, item6_subtotal, item7_subtotal, item8_subtotal, item9_subtotal, item10_subtotal]}
    df = pandas.DataFrame(List)
    print(df)
    print("Total = " + str(total))

print("\n---BILL PRINT---\n")

Company_file = open("Company.txt", "r")
Company_name = Company_file.read()
Company_file.close()

name = input("Customer Name: ")
items = int(input("Items Bought: "))

if items == 1 :
    one()
    print("\t" + Company_name)

if items == 2 :
    two()
    print("\t" + Company_name)

if items == 3 :
    three()
    print("\t" + Company_name)

if items == 4 :
    four()
    print("\t" + Company_name)

if items == 5 :
    five()
    print("\t" + Company_name)

if items == 6 :
    six()
    print("\t" + Company_name)

if items == 7 :
    seven()
    print("\t" + Company_name)

if items == 8 :
    eight()
    print("\t" + Company_name)

if items == 9 :
    nine()
    print("\t" + Company_name)

if items == 10 :
    ten()
    print("\t" + Company_name)

else :
    print("Not Yet Available")