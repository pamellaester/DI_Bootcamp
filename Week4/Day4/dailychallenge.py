import requests
from random import sample
import psycopg2

url = 'https://restcountries.com/v3.1/all'

def random_countries():
    try:
        response = requests.get(url)
        data = response.json()
        random_countries = sample(data, 10)
        return random_countries
    except Exception as e:
        print("Error fetching data from the API:", e)
        return []
    
def insert_countries(countries):
    DB_NAME = "dcw4d4"
    USER = "postgres"
    PASSWORD = "postgres"
    HOST = "localhost"
    PORT = "5433"

    try:
        connection = psycopg2.connect(
            dbname = DB_NAME,
            user = USER,
            password = PASSWORD,
            host = HOST,
            port = PORT
        )

        cursor = connection.cursor()
            
        for country in countries:
            name = country.get('name').get('common')
            capital = country.get('capital')[0]
            flag = country.get('flags').get('png')
            subregion = country.get('subregion')
            population = country.get('population')
            
            query = '''
                insert into countries(name, capital, flag, subregion, population)
                values (%s, %s, %s, %s, %s)
            '''
            cursor.execute(query, (name, capital, flag, subregion, population))
        connection.commit()
        print("Countries inserted into the database successfully.")
        
    except Exception as e:
        print("Error inserting data into the database:", e)
        
    finally:
        cursor.close()
        connection.close()
        
if __name__ == "__main__":
    random_countries = random_countries()
    if random_countries:
        insert_countries(random_countries)