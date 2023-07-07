import mysql.connector

def connect():
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

    return retaildb, cursor




def customer_signup():
    # customer_id = input("Enter id: ")
    cust_name = input("Enter customer name: ")
    cust_mobile_no = input("Enter customer mobile number: ")
    cust_email = input("Enter customer email id: ")
    cust_password = input("Enter customer password: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    pincode = input("Enter pincode: ")

    sql = "INSERT INTO customer (customer_name, mobile_no, email, customer_password, address, city, state, pincode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (cust_name, cust_mobile_no, cust_email, cust_password, address, city, state, pincode)

    db, cursor = connect()

    cursor.execute(sql, val)
    db.commit()

    print(cursor.rowcount, "record inserted.")



def customerLogin():
    email = input("Email: ")
    passwd = input("Password")

    sql  = "SELECT * FROM customer WHERE email = %s AND customer_password = %s"
    val  = (email, passwd)
    db, cursor = connect()

    cursor.execute(sql, val)

    r = cursor.fetchone()

    if r:
        print("Login Successful")
        print("1. Add products to Cart")
        print("2. View Cart")
        print("3. CheckOut Cart")
        print("4. Add money to wallet")

        a = int(input())

        if(a==1):
            query = "select * from product"
            cursor.execute(query)
            for c in cursor:
                print(c)

            p_id = int(input("Enter product id to add: "))
            q = int(input("Enter quantity: "))

            sql2 = "Insert into cart_item(cart_id, product_id, quantity) values (%s, %s, %s)"
            v = (1, p_id, q)

            cursor.execute(sql2, v)
            db.commit()

            print(cursor.rowcount, "record inserted.")



    else:
        print("Invalid email or password")




def admin_signup():
    admin_name = input("Enter admin name: ")
    # admin_id = input("Enter admin ID: ")
    admin_email = input("Enter admin email: ")
    admin_password = input("Enter admin password: ")

    sql = "INSERT INTO admin (admin_name,admin_email, admin_password) VALUES (%s, %s, %s)"
    val = (admin_name, admin_email, admin_password)

    retaildb, cursor = connect()
    cursor.execute(sql, val)
    retaildb.commit()

    print(cursor.rowcount, "record inserted.")


def adminLogin():
    admin_email = input("Enter Email: ")
    admin_password  = input("Enter Password: ")

    sql = "SELECT * FROM admin WHERE admin_email = %s AND admin_password = %s"

    val  = (admin_email,admin_password)

    retaildb, cursor = connect()
    cursor.execute(sql, val)
    r = cursor.fetchone()

    if r:
        print("Login Successful")
    else:
        print("Invalid email or password")


def sellerSignup():
    email = input("Enter email")

def sellerLogin():
    email = input("Enter ")


def admin():
    print("1. Sign Up")
    print("2. Login")

    a = int(input())
    if(a==1):
        admin_signup()
    if(a==2):
        adminLogin()


def customer():
    print("1. Sign Up")
    print("2. Login")

    a = int(input())
    if(a==1):
        customer_signup()
    if(a==2):
        customerLogin()

def seller():
    print("1. Sign Up")
    print("2. Login")

    a = int(input())
    if(a==1):
        sellerSignup()
    if(a==2):
        sellerLogin()


def Retail():

    while True:
        print('''1. Enter as Admin\n2. Enter as Customer ''')
        ch = int(input())
        if(ch==1):
            admin()
        elif(ch==2):
            customer()
        elif(ch==3):
            seller()
        else:
            print("Exited !!")
            break

Retail()