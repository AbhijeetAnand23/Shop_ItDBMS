import mysql.connector

retaildb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password',
    database = 'retail2'
)


cursor = retaildb.cursor()


if retaildb.is_connected():
    print("Connected")
else:
    print("Not connected")


query1 = ("select d.d_name as delievery_boy_name, c.customer_name as customer_name, crt.order_date from delievery_boy d join cart crt on crt.d_id = d.d_id join customer c on c.customer_id = crt.customer_id ;")

cursor.execute(query1)
for c in cursor:
    print(c)


print("\n********************************************************************************************************\n")

query2 = ("select product.product_id, product.product_name, sum(cart_item.quantity) as Total from product inner join cart_item group by product_id order by sum(cart_item.quantity) desc limit 1;")
cursor.execute(query2)
for p in cursor:
    print(p)