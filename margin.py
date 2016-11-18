import sys

print "Num. of Contract, Strike price, Current price"

c_price = input("Current Price: ")
c_price = float(c_price)
st_price = input("Strike Price: ")
st_price = float(st_price)
op_price = input("Primium: ")
op_price = float(op_price)
num_cont = input("Num. of contracts: ")
num_cont = float(num_cont)

if c_price < st_price: 
	otm = st_price-c_price
else: 
	otm = 0

cal1 = ( 0.25 * c_price - otm + op_price ) * num_cont * 100;
cal1_up = ( 0.25 * c_price - otm + op_price*0.2+op_price ) * num_cont * 100;
cal2 = ( 0.15 * st_price + op_price) * num_cont * 100;
cal2_up = ( 0.15 * st_price + op_price*0.2+op_price) * num_cont * 100;

if cal1 > cal2: 
	margin = cal1 
elif cal1 < cal2: 
	margin = cal2 
else: 
	margin = cal1

if cal1_up > cal2_up: 
	margin_up = cal1_up 
elif cal1_up < cal2_up: 
	margin_up = cal2_up 
else: 
	margin_up = cal1_up

print "The margin requirement is $%.2f"% margin 
print ('If premium increases 20%%, the premium:  ${0:.2f} and margin:  ${1:.2f}'.  format(op_price*0.2+op_price, margin_up))