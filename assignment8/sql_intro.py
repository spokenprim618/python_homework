import sqlite3

with sqlite3.connect("../db/magazines.db") as conn:
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
    CREATE TABLE IF NOT EXISTS subscribers (
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
        result = cursor.fetchall()
        if len(result) > 0:
            if result[0][1] == publisher_name:
                print(f"Publisher {publisher_name} already exists")
                return
        cursor.execute("INSERT INTO Publishers (publisher_name) VALUES (?)", (publisher_name,))

    def add_subscriber(cursor, subscriber_name, address):
        result = cursor.fetchall()
        if len(result) > 0:
            if result[0][1] == subscriber_name and result[0][2] == address:
                print(f"Subscriber {subscriber_name} already exists")
                return
        cursor.execute("INSERT INTO Subscribers (subscriber_name, address) VALUES (?,?)", (subscriber_name, address))

    def add_magazine(cursor, magazine_name, publisher_id):
        result = cursor.fetchall()
        if len(result) > 0:
            if result[0][1] == magazine_name and result[0][2] == publisher_id:
                print(f"Magazine {magazine_name} already exists")
                return
        cursor.execute("INSERT INTO Magazines (magazine_name, publisher_id) VALUES (?,?)", (magazine_name, publisher_id))

   

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
        cursor.execute("SELECT * FROM Subscribers WHERE subscriber_name = ?", (subscriber,))
        result = cursor.fetchall()
        if len(result) > 0:
            subscriber_id = result[0][0]
        else:
            print(f"Subscriber {subscriber} not found")
            return
        cursor.execute("SELECT * FROM Magazines WHERE magazine_name = ?", (magazine,))
        result = cursor.fetchall()
        if len(result) > 0:
            magazine_id = result[0][0]
        else:
            print(f"Magazine {magazine} not found")
            return
        cursor.execute("INSERT INTO Subscriptions (subscriber_id, magazine_id, subscription_date) VALUES (?,?,?)", (subscriber_id, magazine_id, subscription_date))
        result = cursor.fetchall()
        if len(result) > 0:
            print(f"Subscription added successfully for {subscriber} and {magazine}")
        else:
            print(f"Subscription failed for {subscriber} and {magazine}")
                
                
    add_subscription(cursor, 1, 1, "2021-01-01")
    add_subscription(cursor, 2, 2, "2021-01-02")
    add_subscription(cursor, 3, 3, "2021-01-03")
    cursor.commit()
    cursor.execute("SELECT * FROM Subscriptions")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute("SELECT * FROM Magazines ORDER BY magazine_name")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute("JOIN Publishers ON Magazines.publisher_id = 1")
    result = cursor.fetchall()
    for row in result:
        print(row)
        
    