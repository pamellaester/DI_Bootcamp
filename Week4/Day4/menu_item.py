import psycopg2

# 1. Connect to the database

DB_NAME = "Restaurant_Menu_Manager"
USER = "postgres" 
PASSWORD = "postgres" 
HOST = "localhost"
PORT = "5433"

# 3. Write an SQL query
class MenuItems:

    def __init__(self,name,price):
        self.name = name
        self.price = price 
        self.table_name = "Menu_Items"


    def save_item(self):

        query = f'''
        insert into {self.table_name} (item_name,item_price)
        values
        ({self.name},{self.price})
        '''
        cursor.execute(query) # execute the query
        connection.commit() # make changes in the database

    def delete_item(self): 
        query = f'''
            select id from {self.table_name} where name_item = '{self.name}'
        '''
        cursor.execute(query)
        output = cursor.fetchall()[0][0]
        query = f'''
           delete from {self.table_name} where id = {output}
        );
        '''
        cursor.execute(query) # execute the query
        connection.commit() # make changes in the database
        return output


    def update_item(self,new_name,new_price):

        query = f'''
        update {self.table_name}
        set name_item = '{new_name}', price_item = '{new_price}'
        where name_item = '{self.name}'
        ;
        '''
    
        cursor.execute(query)
        connection.commit()
       
    



if __name__ == '__main__':

    try:
        connection = psycopg2.connect(
            dbname = DB_NAME,
            user = USER,
            password = PASSWORD,
            host = HOST,
            port = PORT
        )
    except Exception as e:
        print(f"Error: {e}")

    # 2. Create a cursor object
    cursor = connection.cursor()

    table_name = 'Menu_Items'



    item = MenuItems('Burger', 35)
    item.save_item()
    item.delete_item()
    item.update_item('Veggie Burger', 37)
    # item2 = MenuManager.get_by_name('Beef Stew')
    # items = MenuManager.all()

    # 4. Close database connection

    connection.close()