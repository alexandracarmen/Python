import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="database",
    password="database",
    database="StocKBuster"
)

my_cursor = my_db.cursor()


def stock_update():
    global ar_history
    ar_history = []
    my_cursor.execute(
        "SELECT product, ROUND(AVG(nr_of_products)) avg_products_daily FROM sales_history group by product;")
    my_result = my_cursor.fetchall()
    for x in my_result:
        ar_history.append(x)
    
    global nr_of_days, ar_inventory
    ar_inventory = []
    my_cursor.execute(
        "SELECT product, nr_of_products FROM inventory;")
    my_result = my_cursor.fetchall()
    for x in my_result:
        ar_inventory.append(x) 
     
    for x in ar_history[1]:
        x = x * nr_of_days
           
    ar_new_inventory = []
    for history_item in ar_history:
        ar_new_inventory.append ((history_item[0], int(history_item[1])))
    for inventory_item in ar_inventory:
        names = [item[0] for item in ar_new_inventory]
        if inventory_item[0] in  names:
           
            if inventory_item[1] > ar_new_inventory[names.index(inventory_item[0])][1]:
                ar_new_inventory[names.index(inventory_item[0])] = (inventory_item[0], 0)
            else:
                ar_new_inventory[names.index(inventory_item[0])] = (inventory_item[0], ar_new_inventory[names.index(inventory_item[0])][1] - inventory_item[1])
                
    return ar_new_inventory

if __name__ == "__main__":
    try:
        nr_of_days = int(input("Dati nr de zile pentru care trebuie calculat inventarul:"))
    except:
        print("Input invalid!")
    else:
        result = stock_update()
        print(f"Inventarul curent:{ar_inventory}")
        print(f"Produse din istoricul comenzilor: {ar_history}")
        print(f"Comanda urmatoare:{result}")
  
