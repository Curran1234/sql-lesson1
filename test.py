import sqlite3

def search_food(keyword):
    sql = f"select * from food where description like '%{keyword}%';"
    return execute_sql(sql)

def get_nutrients(fdc_id):
    sql = f"select name, amount, unit_name from food_nutrient,nutrient where food_nutrient.nutrient_id = nutrient.id and food_nutrient.fdc_id = {fdc_id};"

    return execute_sql(sql)

def get_branded_food(keyword):
    sql = f"Select food.fdc_id, brand_name from branded_food,food where branded_food.fdc_id = food.fdc_id and brand_owner like '%{keyword}%';"
    return execute_sql(sql)

def get_measure_units(id):
    sql = f"select name from measure_unit where id = {id};"
    return execute_sql(sql)

def get_food_categories():
    sql = f"select id,description from food_category;"
    return execute_sql(sql)

def get_food_by_category(category_id):
    sql = f"select * from food where food_category_id = {category_id};"
    return execute_sql(sql)





def execute_sql(sql):
    try:
        # Connect to the database (or create it if it doesn't exist)
        connection = sqlite3.connect('data/usda_food_data.db')
        cursor = connection.cursor()
        print("Database connection successful!")

        # Execute a simple query
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    except sqlite3.Error as error:
        print(f"Error occurred: {error}")

    finally:
        if connection:
            connection.close()
        print("SQLite connection closed.")

#print(search_food("red bull"))
#print(get_nutrients(2578053))
#print(get_branded_food('red bull'))
#print(get_measure_units(1004))
print(get_food_by_category(9))