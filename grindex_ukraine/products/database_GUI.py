import sqlite3

import mysql.connector as mySql


class Items:
    def __init__(self, brand, name_translit, promotion, classification, cip, name_sales_report, name_domestic, item_id):
        self.item_id = item_id
        self.name_domestic = name_domestic
        self.name_sales_report = name_sales_report
        self.cip = cip
        self.classification = classification
        self.promotion = promotion
        self.name_translit = name_translit
        self.brand = brand

    def __str__(self):
        return f"Brand: {self.brand}\nItem: {self.name_translit}\nPromotion: {self.promotion}\nClassification: {self.classification}\nCip: {self.cip}\nID: {self.item_id}"

    def __repr__(self):
        return f"({self.brand}, {self.name_translit}, {self.promotion}, {self.classification}, {self.cip})"


class CItemsDAO:
    def insert_item(conn, items: Items):
        with sqlite3.connect("items.db") as conn:
            cursor = conn.cursor()
            # cursor.execute("INSERT INTO Items VALUES (276,'Djamala');")
            # cursor.execute(f"INSERT INTO Items VALUES (?,?)",(artist.item,f'{artist.brand}'))
            cursor.execute(f"INSERT INTO items VALUES (?,?,?,?,?,?,?,?)", (f'({items.item_id}',(f'{items.promotion}'), (f'{items.classification}'), (f'{items.name_domestic}'), (f'{items.name_sales_report}'),(f'{items.name_translit}'),(f'{items.brand}'),(f'{items.cip}')))

            conn.commit()

    def update_item(conn,items: Items):
        with mySql.connect(
                host="localhost",
                user="root",
                password="root",
                database="chinook"
        ) as conn:
            cursor = conn.cursor()
            # cursor.execute("UPDATE Items SET Name = 'TNMK' WHERE ArtistId = 276;")
            cursor.execute(f"UPDATE Items SET Name = '{items.brand}' WHERE ItemsId = {items.item};")
            conn.commit()

    def delete_item(conn):
        with sqlite3.connect("items.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM items WHERE items.item_id = '(90'")
            #cursor.execute(f"DELETE FROM Items WHERE ItemsId = {items.item}")
            conn.commit()

    def read_item(conn):
        with sqlite3.connect("items.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT items.brand, items.name_translit, items.promotion, items.classification, items.cip, items.name_sales_report, items.name_domestic, items.item_id  FROM items")
            results = cursor.fetchall()
            artists = []
            for entry in results:
                artists.append(
                    Items(brand=entry[0], name_translit=entry[1],  promotion=entry[2], classification=entry[3], cip=entry[4],name_sales_report=entry[5], name_domestic=entry[6], item_id=entry[7])
                )
            return artists


if __name__ == '__main__':
    conn = sqlite3.connect("items.db")
        # ArtistsDAO.delete_artist(Items(276,"Kazka"))
        # item = int(input("item ="))
        # brand = input("brand =")
    #item_id = 90
    #brand = 'AAA'
    #name_translit = 'BBB'
    #promotion = 'NNN'
    #classification = 'NNN'
    #name_domestic = "fff"
    #name_sales_report = "ffgg"
    #cip = 3.33336
    #item_ = Items(brand, name_translit, promotion, classification, cip,name_sales_report,name_domestic,item_id)
    #ItemsDAO.insert_item(conn,item_)
    CItemsDAO.delete_item(conn)
    items = CItemsDAO.read_item(conn)
    for i in items:
        print(i.__str__())
        print('*'*11)
