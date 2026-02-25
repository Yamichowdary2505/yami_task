#for a in range(25, 40, 2):
#    print(a, end=" ")

#string = " yami"
#for i in string:
#    print(i, end=" ")

#for i in range(10):
#    if i == 2:
#        break
#    print(i) 

#sum = 0
#for i in range(1, 10):
#    sum += i
#    print("SUM:", sum)
#print("Final Sum:", sum) 

#i = 1
#while i <= 10:
#    print(i)
#    i += 1

#while True:
#    print("yami") 

#string = "SOURSEYS"

#print(len(string))
#print(string[3])
#print(string[3:])
#print(string[:3])
#print(string[0:6])
#print(string.lower())
#print(string.replace("S", "A"))
#print(string.replace("E", "e"))
#print(string.count("A"))
#print("U" in string)
#print(string.find("E"))
#print(string.strip())
#print(string)  

#string = "YAMI"
#reverse = string[::-1]
#print("reversed string:", reverse)
#print("string:", string) 

#name = input("Enter the name: ")
#age = int(input("Enter the age: "))
#print(f"name is {name}, age is {age}")
#print("my name is {}, my age is {}".format(name, age))

#a = "Yami Chowdary"
#reverse = a[::-1]
#print("reversed string is:", reverse)

#name = input("Enter the Employee Detail: ")
#ID = int(input("Enter the employee ID: "))
#print(f"employee name {name}, employee Id {ID}")

#num = int(input("Enter the number: "))

#for i in range(10):
#    if i == 3:
#        break
#    print("false")

#n= 15
#if n<15:
#    print("you are eligible")
#elif n == 15:
#   print("You should be more than 15 yrs old to be eligible")
#else :
#    print("Entered value should be less than 15")  


#n= 11
#if n<15:
#    print("you are eligible")
#    if n > 30 :
#        print("you are too old")
#    else :
#        print("you are good")
#elif n == 15:
#    print("You should be more than 15 yrs old to be eligible")
#else :
#    print("Entered value should be less than 15")  

#list = [[1,2,3,4,5,6, True,False,"MOM"],[True,False,"8","c"]]
#list_1 = [ 7,8,9]
#list_2 =list + list_1
#print(list[1])
#print(list[:])
#for item in list:
#    print(item)

#list.append("Appa")
#print(list)

#del list[2]
#print(list) 

#list_1 =[x for x in range(10) if x%2 ==0]
#print(list_1)

#listofstrings = ["Apple","Banana","Carrot"]
#uppercasestrings =[string.upper() for string in listofstrings]
#print(listofstrings)
#print(uppercasestrings)

#pairs = [(x,y) for x in [1,2,3,4] for y in [3,4,5,6]]
#print(pairs)

#tuple =(4,)   # we need to include , so it is considered as tuple 
#l = [4]
#print(type(tuple))
#print(type(l))

#tuple_1 =(3,4,5,6)
#tuple_2 =(4,5,6,7)
#tuple_3 = tuple_1 + tuple_2*2
#print(tuple_3)
#for i in tuple_1:
#    print(i)
#tuple_1[0]=10
#print[tuple_1]
#print(3  not in tuple_1)

#String = "SASTRA "
#for i in String :
#    print(i,end=",")  

#details = ("Yami", 25, "Sastra", 20)
#for item in details:
#    print(item,end=",") 
#if type(item) == int:
#        print("Number:", item)

#data = ("Yami", 10, "Sastra", 20, 30)
#total = 0
#for item in data:
#    if type(item) == int:
#        total += item
#print("Total of numbers:", total)
#count = 0
#for item in data:
#    if type(item) == str:
#        for letter in item:
#            count += 1
#print("Total letters:", count)

#date = ("Yami", 250, "Sastra", 20)
#for item in date:
#    if type(item) == int:
#        print(item * 2)

#data = ("Yami", 100, "Sastra", 25)
#for item in data:    
#    if type(item) == str:
#        print("Reversed string:", item[::-1])    
#    if type(item) == int:
#        print("Square of number:", item ** 2)

#my_list = ["yami", "sastra", 1, 2, 3]
#print(my_list)
#my_list.append(4)
#print(my_list)
#my_list.append("python")
#print(my_list)
#my_list.remove("sastra")
#print(my_list)
#del my_list[0]
#print(my_list)  

#my_tuple_1 = ("yami", "sastra", 1, 2, 3)
#my_tuple_2 = ("Amma","Appa")
#my_tuple = my_tuple_1 + my_tuple_2
#TtoL = list(my_tuple)
#TtoL.append(25052005)
#print(my_tuple)
#print(TtoL)


#def greet(name,place):
#    print(f"Hello! Good morning{name},This place is {place}")

#greet("harry","India")
#greet("henry","austrailia")
#greet("John","USA")

#def add(a,b,c):
#    return a+b+c

#add1 = add(2,3,4)
#print(add1)
#add2= add(4,5,6)
#print (add2)

#add = lambda a,b,c:a+b+c
#print(add(4,5,6))
#print(add(1,2,3))

products = [
    ("P101", "Laptop", "Electronics", 2, 50000, 0.05),
    ("P102", "Phone", "Electronics", 1, 20000, 0.03)
]

discounts = {"premium": 0.10, "bulk": 0.05}

orders = []
sold = {"P101": set(), "P102": set()}
waiting = {"P101": [], "P102": []}
order_id = 1

class Product:
    def __init__(self, pid, name, cat, stock, price, disc):
        self.pid = pid
        self.name = name
        self.cat = cat
        self.stock = stock
        self.price = price
        self.disc = disc

class Customer:
    def __init__(self, name, premium):
        self.name = name
        self.premium = premium

class Order(Product, Customer):
    def __init__(self):
        pass

    def get_product(self, pid):
        for p in products:
            if p[0] == pid:
                return Product(*p)

    def calculate_price(self, product, qty, customer):
        total = product.price * qty
        if customer.premium:
            total -= total * discounts["premium"]
        if qty >= 2:
            total -= total * discounts["bulk"]
        total -= total * product.disc
        return total

    def place_order(self, pid, name, qty, premium, pay):
        global order_id
        product = self.get_product(pid)
        customer = Customer(name, premium)

        if len(sold[pid]) + qty <= product.stock:
            total = self.calculate_price(product, qty, customer)
            for _ in range(qty):
                sold[pid].add(order_id)
            orders.append({"order_id": order_id, "name": name, "pid": pid, "qty": qty, "pay": pay, "total": total})
            print("Order Placed:", order_id, total)
            order_id += 1
        else:
            waiting[pid].append((name, qty, premium, pay))
            print("Added to Waiting List:", name)

    def cancel_order(self, oid):
        for o in orders:
            if o["order_id"] == oid:
                pid = o["pid"]
                qty = o["qty"]
                orders.remove(o)
                sold[pid] = set(list(sold[pid])[:-qty])
                print("Order Cancelled:", oid)

                if waiting[pid]:
                    w = waiting[pid].pop(0)
                    self.place_order(pid, w[0], w[1], w[2], w[3])
                return

    def report(self):
        for p in products:
            pid = p[0]
            stock = p[3]
            sold_qty = len(sold[pid])
            wait = len(waiting[pid])
            revenue = sum(o["total"] for o in orders if o["pid"] == pid)
            print(pid, stock, sold_qty, wait, revenue)

    def total_revenue(self):
        total = sum(o["total"] for o in orders)
        occ = 0
        for p in products:
            occ += len(sold[p[0]]) / p[3]
        avg = (occ / len(products)) * 100
        print("Total Revenue:", total)
        print("Average Utilization:", avg)

shop = Order()

shop.place_order("P101", "Yami", 1, True, "UPI")
shop.place_order("P101", "Gopinath", 1, False, "Cash")
shop.place_order("P101", "Indravathi", 1, False, "Card")

shop.cancel_order(1)

shop.report()
shop.total_revenue()C:\Users\LENOVO\OneDrive\Documents\Sourcsyes\task.py



