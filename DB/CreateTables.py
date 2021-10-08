import psycopg2 as psy
from config import database, user, port, host, password

def createTables():
    try:
        connect = psy.connect(
            database = database, 
            user = user,
            port = port,
            host = host,
            password = password
        )
        connect.autocommit = True
        cursor = connect.cursor()
        print("Connected to DB...")

    except Exception as e:
        print("ERROR: Cannot connect to DB")
        print(e)


    # Equipment
    cursor.execute('''
        CREATE TABLE Equipment (
            tool_name TEXT NOT NULL,
            measurement_type TEXT,
            PRIMARY KEY (tool_name)
        );

        CREATE TABLE Ingredient (
            ingredient_name TEXT NOT NULL,
            ingredient_id INTEGER,
            PRIMARY KEY(ingredient_id)
        );

        CREATE TABLE Recipe (
            recipe_id INTEGER NOT NULL,
            healthy BOOLEAN,
            image TEXT,
            category TEXT,
            recipe_name TEXT,
            directions TEXT,
            difficulty INTEGER,
            prep_time INTEGER,
            PRIMARY KEY (recipe_id)
        );

        CREATE TABLE Rating (
            recipe_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            score INTEGER,
            PRIMARY KEY (recipe_id, user_id)
        );

        CREATE TABLE User_Profile (
            user_id INTEGER NOT NULL,
            username TEXT,
            password TEXT,
            PRIMARY KEY (user_id)
        );

        CREATE TABLE Creates (
            recipe_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            PRIMARY KEY (recipe_id),
            FOREIGN KEY (recipe_id) REFERENCES Recipe,
            FOREIGN KEY (user_id) REFERENCES User_Profile
        );

        CREATE TABLE Have (
            recipe_id INTEGER NOT NULL,
            ingredient_id INTEGER NOT NULL,
            PRIMARY KEY (recipe_id, ingredient_id),
            FOREIGN KEY (recipe_id) REFERENCES Recipe,
            FOREIGN KEY (ingredient_id) REFERENCES Ingredient
        );

        CREATE TABLE Require(
            tool_name TEXT NOT NULL,
            recipe_id INTEGER NOT NULL,
            PRIMARY KEY (tool_name, recipe_id),
            FOREIGN KEY (tool_name) REFERENCES Equipment,
            FOREIGN KEY (recipe_id) REFERENCES Recipe
        );
    ''')

    cursor.close()
    connect.close()
    print("Closed DB connection...")

createTables()