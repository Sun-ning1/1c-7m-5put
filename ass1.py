def read_filles():
    first_file = open("products.txt",'r')
    first_file = first_file.read().splitlines()
    second_file = open("suppliers.txt",'r')
    second_file = second_file.read().splitlines()
    third_file = open("availability.txt",'r')
    third_file = third_file.read().splitlines()
    last_file = open('onshelves.txt','r')
    last_file = last_file.read().splitlines()
    return  first_file,second_file,third_file,last_file

def get_availability(file):
    product_code=[]
    supplier_phone=[]
    price=[]
    availability_dict={}
    for i in file:
        info = i.split(",") 
        product_code.append(info[0])
        supplier_phone.append(info[1])
        price.append(info[2])

    for i in range(len(product_code)):
        if product_code[i] in availability_dict:
            availability_dict[product_code[i]].append((supplier_phone[i],price[i]))
            
        else:availability_dict[product_code[i]] = [(supplier_phone[i],price[i])]
    
    return availability_dict

def get_products(file):
    product_code=[]
    product_name=[]
    for i in file:
        info = i.split(";")
        product_code.append(info[0])
        product_name.append(info[1])
    production_dict = dict(zip(product_code,product_name))
    return production_dict

def count_to_order(file):
    remain=[]
    product=[]
    order=[]
    for i in file:
        info = i.split("#")   
        remain.append(info[1])
        product.append(info[0])
    for i in remain:
        if int(i)- 50 < 0:
            order.append(50-int(i))
        else:
            order.append(0)

    need_to_order=dict(zip(product,order))
    return need_to_order

def get_suplyer(file):
    tel=[]
    name=[]
    for i in file:
        info = i.split(";")    
        tel.append(info[0])
        name.append(info[1])
    suplyer_dict = dict(zip(tel,name))
    return suplyer_dict

def extract_info(products,suppliers,availability,onshelves4):
    
    production_dict = get_products(products)
    supplier_dict = get_suplyer(suppliers)
    need_to_order = count_to_order(onshelves4)
    availability_dict = get_availability(availability)
    draw(production_dict,supplier_dict,availability_dict,need_to_order)    


def draw(production_dict,supplier_dict, availability_dict,need_to_order):
    Highest_cost=[]
    valid_highest=[]
    total_cost=0
    print("+--------------+------------------+--------+----------------+----------+")
    print("| Product code | Product Name     |Quantity| Supplier       |Cost      |")
    for product_code in production_dict:
        product_name = production_dict[product_code][:16]
        quantity = need_to_order[product_code]
        quantity = int(quantity)
        star = '*' if quantity > 40 else ' '
        supplier_phone,price = availability_dict[product_code][0]
        cost =  quantity * float(price)
        Highest_cost.append([cost,supplier_phone])
        
        supplier_phone = f"({supplier_phone[0:3]}) {supplier_phone[3:6]} {supplier_phone[6:]}"
        total_cost += cost
        print(f"|  {product_code}   |{star}{product_name:<16} | {quantity:>6} | {supplier_phone:<14} | ${cost:>7.2f} |")

    valid_highest.append(max(Highest_cost))
    while max(Highest_cost)[0] == Highest_cost.pop(Highest_cost.index(max(Highest_cost))) :
        valid_highest.append(max(Highest_cost))

    print("{}".format(" "*44)) 
    print("+--------------+------------------+--------+----------------+----------+")
    print("| Total Cost |           $ {}|".format(total_cost))
    print("+--------------+---------------------------+")
    while len(valid_highest) > 0:
        print("Highest cost: {} ({}) {} {} [{}]".format(supplier_dict[valid_highest[-1][1]],valid_highest[-1][1][0:3],valid_highest[-1][1][3:6],valid_highest[-1][1][6:],valid_highest[-1][0]))
        valid_highest.pop(-1)

def main():
    products,suppliers,availability,onshelves = read_filles()
    extract_info(products,suppliers,availability,onshelves)

if __name__ == "__main__":
    main()