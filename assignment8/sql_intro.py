import sqlite3

with sqlite3.connect(".\db\magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    try:
        cursor = conn.cursor()
        
    except Exception as e:
        print(e)
    finally:
        conn.commit()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Publishers (
        publisher_id INTEGER PRIMARY KEY,
        publisher_name TEXT NOT NULL UNIQUE
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        subscriber_name TEXT NOT NULL UNIQUE,
        address TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Magazines (
        magazine_id INTEGER PRIMARY KEY,
        magazine_name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER,
        FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)
    )
    """)
    

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        subscriber_id INTEGER,
        magazine_id INTEGER,
        subscription_date TEXT NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id)
    )
    """)
    
    def add_publisher(cursor, publisher_name):
        try: 
            cursor.execute("INSERT INTO Publishers (publisher_name) VALUES (?)", (publisher_name,))

        except sqlite3.IntegrityError:
            print(f"{publisher_name} is already in the database.")        

    def add_subscriber(cursor, subscriber_name, address):
        try:
            cursor.execute("INSERT INTO Subscribers (subscriber_name, address) VALUES (?,?)", (subscriber_name, address))
        except sqlite3.IntegrityError:
            print(f"{subscriber_name} is already in the database.")    

    def add_magazine(cursor, magazine_name, publisher_id):
        try:
            
            cursor.execute("INSERT INTO Magazines (magazine_name, publisher_id) VALUES (?,?)", (magazine_name, publisher_id))
        except sqlite3.IntegrityError:
            print(f"{magazine_name} is already in the database.")    

   

    add_publisher(cursor, "Publisher 1")
    add_publisher(cursor, "Publisher 2")
    add_publisher(cursor, "Publisher 3")
    add_subscriber(cursor, "Subscriber 1", "Address 1")
    add_subscriber(cursor, "Subscriber 2", "Address 2")
    add_subscriber(cursor, "Subscriber 3", "Address 3")
    add_magazine(cursor, "Magazine 1", 1)
    add_magazine(cursor, "Magazine 2", 2)
    add_magazine(cursor, "Magazine 3", 3)
    
    conn.commit()
    def add_subscription(cursor, subscriber, magazine, subscription_date):
        cursor.execute("SELECT * FROM Subscribers WHERE subscriber_id = ?", (subscriber,))
        result = cursor.fetchall()
        try:
            subscriber_id = result[0][0]
        except Exception as e:
            print(f"Subscriber {subscriber} not found")
            print(e)
            return
        cursor.execute("SELECT * FROM Magazines WHERE magazine_id = ?", (magazine,))
        result = cursor.fetchall()
        try:
            magazine_id = result[0][0]
        except Exception as e:
            print(f"Magazine {magazine} not found")
            print(e)

            return
        try:
            cursor.execute("INSERT INTO Subscriptions (subscriber_id, magazine_id, subscription_date) VALUES (?,?,?)", (subscriber_id, magazine_id, subscription_date))
        except Exception as e:
            print(f"Subscription failed for {subscriber} and {magazine}")
            print(e)
    add_subscription(cursor, 1, 1, "2021-01-01")
    add_subscription(cursor, 2, 2, "2021-01-02")
    add_subscription(cursor, 3, 3, "2021-01-03")
    conn.commit()
    cursor.execute("SELECT * FROM Subscriptions")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute("SELECT * FROM Magazines ORDER BY magazine_name")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute("SELECT Magazines.publisher_id,Magazines.magazine_name FROM Magazines JOIN Publishers ON Magazines.publisher_id = Publishers.publisher_id WHERE Publishers.publisher_id=1")
    result = cursor.fetchall()
    for row in result:
        print(row)
        
    conn.commit()
print("Done")