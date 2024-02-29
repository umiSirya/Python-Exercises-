weight=4.8
pgs=125

#Ground shipping table
#price is total price of package
#pgs is premium ground shipping
if weight <= 2:
  price=(1.50* weight)+20.00
  print('Price of ground shipping is: ', price)
elif weight <=6:
    price=(3.00*weight)+20.00
    print('Price of ground shipping is: ', price)
elif weight <=10:
    price=(4.00*weight)+20.00
    print('Price of ground shipping is: ', price)
else:
    price=(4.75*weight)+20.00
    print('Price of ground shipping is: ', price)
  
print('Premium ground ground shipping: $', pgs)

#Drone shipping
if weight<=2:
  price_of_droneshipping=4.50*weight
  print('Price of drone shipping: ', price_of_droneshipping)
elif weight<=6:
  price_of_droneshipping=9.00*weight
  print('Price of drone shipping: ', price_of_droneshipping)
elif weight<=10:
  price_of_droneshipping=12.00*weight
  print('Price of drone shipping: ', price_of_droneshipping)
else: 
  price_of_droneshipping=14.25*weight
  print('Price of drone shipping: ', price_of_droneshipping)
  