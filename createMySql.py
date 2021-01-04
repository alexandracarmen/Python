import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    user = "database",
    password = "database"
)

my_cursor = my_db.cursor()

my_cursor.execute("CREATE DATABASE StockBuster")

my_cursor.execute("USE StockBuster")

my_cursor.execute(
    "CREATE TABLE inventory ( product_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, produs VARCHAR(100) NOT NULL, nr_de_produse INT NOT NULL)")
my_cursor.execute(
    "CREATE TABLE sales_history(product_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, produs VARCHAR(100) NOT NULL, nr_de_produse INT NOT NULL, sale_date DATE)")
