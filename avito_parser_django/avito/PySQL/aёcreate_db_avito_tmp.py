import sqlite3

def main():
    pass

def create_db_items():
    #При подключении к базе, автоматически создается realty.db
    connection = sqlite3.connect('realty_tmp.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE offers (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_item integer,
            category_name text,
            category_kod text,
            date text,
            time text,
            title_desk text,
            title_full text,
            img text,
            price integer,
            address text,
            coords text,
            url text,
            uri text,
            uri_mweb text,
            offer_id integer,
            area integer,
            rooms text,
            floor integer,
            total_floor
        )     
    """)
    connection.close()


if __name__ == '__main__':
    pass
    #create_db_items()
#    main()
'''
#   id_item
    category_name
    category_kod
#    time 
    title 
    images = ''
    price 
    address 
    coords 
    uri 
    uri_mweb 
'''