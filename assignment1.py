def getProducts(filename):

	file_data = open(filename,'r').read().splitlines() #open the first file about all products sold in the store.
	products = {}
	for item in file_data:#read all the items in file
		productions = item.split(";")
		# print(productions)
		product_id,product_name = productions[0],productions[1]
		products[int(product_id)] = product_name

	return products

def getSuppliers(filename):

	file_data = open(filename,'r').read().splitlines() #open the second file about all products sold in the store.
	suppliers = {}
	for item in file_data:
		supplier_phone,supplier_name = item.split(';')[:2]
		suppliers[supplier_phone] = supplier_name

	return suppliers

def getAvailability(filename):

	file_data = open(filename,'r').read().splitlines() #open the third file about about what product the suppliers have and at what price
	availability = {} 
	for item in file_data:
		product_id, supplier_phone, price = item.split(',') 
		product_id = int(product_id) 
		if product_id in availability:
			availability[product_id].append((supplier_phone,float(price)))
		else:
			availability[product_id] = [(supplier_phone,float(price))]

	for product in availability:
		choices = availability[product]
		
	return availability

def getOnShelves(filename):

	file_data = open(filename,'r').read().splitlines() #open the last file about inventory for that day
	onShelves = {}
	for item in file_data: #read all the items
		product,amount = item.split("#")
		onShelves[int(product)] = int(amount)

	return onShelves

def generateReport(onShelves, products, suppliers, availability):
	new_f = open("orders.txt", "w")
	new_f.write("+--------------+------------------+--------+----------------+----------+" +'\n')
	new_f.write("| Product code | Product Name     |Quantity| Supplier       |Cost      |" +'\n')	
	new_f.write("+--------------+------------------+--------+----------------+----------+"+'\n')
	total_cost = 0
	orders = []
	for product_id in products:
		product_name = products[product_id][:16]
		quantity = 50 - onShelves[product_id]
		star = '*' if quantity > 40 else ' '#if quantity > 40, product_name with star(*)
		Dollar = '$'
		supplier_phone,price = availability[product_id][0]
		cost = quantity * price
		orders.append((supplier_phone,cost))
		supplier_phone = f"({supplier_phone[0:3]}) {supplier_phone[3:6]} {supplier_phone[6:]}"
		total_cost += cost
		new_f.write("|  {}   |{}{:<16} |  {:>6}|  {:<14}|{}{:>7.2f}  |".format(product_id,star,product_name,quantity,supplier_phone,Dollar,cost)+'\n')#
	new_f.write("+--------------+------------------+--------+----------------+----------+"+'\n')
	new_f.write("| Total Cost   |                 $  {}|".format(total_cost)+'\n')
	new_f.write("+--------------+---------------------------+"+'\n')
	highest_cost = max(orders, key = lambda x : x[1]) #find the max amount for cost(quantity * price), return the second item(price) to x
	for order in orders:
		if order[1] == highest_cost[1]:
			supplier_phone = order[0] #find the store's phone number when the product gets the highest cost
			supplier_name = suppliers[supplier_phone]#find the store's name
			cost = order[1]
			supplier_phone = f"({supplier_phone[0:3]}) {supplier_phone[3:6]} {supplier_phone[6:]}"
			new_f.write(f"Highest cost: {supplier_name} {supplier_phone} [${cost:.2f}]" +'\n')
def main():

	onShelves = getOnShelves('onshelves.txt')
	products = getProducts('products.txt')
	suppliers = getSuppliers('suppliers.txt')
	availability = getAvailability('availability.txt')
	generateReport(onShelves, products, suppliers, availability)

# def creat_file(assignment1):
	




main()