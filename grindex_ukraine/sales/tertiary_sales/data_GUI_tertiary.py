import sqlite3

import mysql.connector as mySql


class Tertiary_sales:
    def __init__(self, year, month, weight_penetration, weight_sro, quantity, volume_euro):
        self.volume_euro = volume_euro
        self.quantity = quantity
        self.weight_sro = weight_sro
        self.weight_penetration = weight_penetration
        self.month = month
        self.year = year

    def __str__(self):
        return f"Year: {self.year}\nMonth: {self.month}\nWeighted penetration: {self.weight_penetration}\nWeighted SRO: {self.weight_sro}\nQuantity_pcs: {self.quantity}\nAmount_euro: {self.volume_euro}"

    def __repr__(self):
        return f"({self.year},{self.month},{self.weight_penetration},{self.weight_sro},{self.quantity},{self.volume_euro})"


class CItemsDAO:
    def insert_item(conn, sales: Tertiary_sales):
        with sqlite3.connect("tertiary_sales_database.db") as conn:
            cursor = conn.cursor()
            # cursor.execute("INSERT INTO Tertiary_sales VALUES (276,'Djamala');")
            # cursor.execute(f"INSERT INTO Tertiary_sales VALUES (?,?)",(artist.item,f'{artist.brand}'))
            cursor.execute(f"INSERT INTO sales VALUES (?,?,?,?,?,?,?,?)", (f'({sales.year}', (f'{sales.month}'), (f'{sales.weight_penetration}'), (f'{sales.weight_sro}'), (f'{sales.quantity}'), (f'{sales.volume_euro}')))

            conn.commit()

    def update_item(conn, sales: Tertiary_sales):
        pass
        with mySql.connect(
                host="localhost",
                user="root",
                password="root",
                database="chinook"
        ) as conn:
            cursor = conn.cursor()
            # cursor.execute("UPDATE Tertiary_sales SET Name = 'TNMK' WHERE ArtistId = 276;")
            cursor.execute(f"UPDATE Tertiary_sales SET Name = '{items.brand}' WHERE ItemsId = {items.item};")
            conn.commit()

    def delete_item(conn):
        with sqlite3.connect("tertiary_sales_database.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM sales WHERE sales.item_id = '(90'")
            #cursor.execute(f"DELETE FROM Tertiary_sales WHERE ItemsId = {sales.item}")
            conn.commit()

    def read_item(conn):
        with sqlite3.connect("tertiary_sales_database.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT ymm.Year, ymm.Месяц, tertiary_sales.WeightPenetration, tertiary_sales.WeightSRO , tertiary_sales.Quantity, tertiary_sales.Volume from tertiary_sales join ymm on tertiary_sales.Period = ymm.Year_monnum where tertiary_sales.MarketOrg = 'Grindeks  (Latvia)'")
            results = cursor.fetchall()
            artists = []
            for entry in results:
                artists.append(
                    Tertiary_sales(year=entry[0], month=entry[1], weight_penetration=entry[2], weight_sro=entry[3], quantity=entry[4], volume_euro=entry[5])
                )
            return artists


if __name__ == '__main__':
    conn = sqlite3.connect("tertiary_sales_database.db")
        # ArtistsDAO.delete_artist(Tertiary_sales(276,"Kazka"))
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
    #item_ = Tertiary_sales(brand, name_translit, promotion, classification, cip,name_sales_report,name_domestic,item_id)
    #ItemsDAO.insert_item(conn,item_)
    #CItemsDAO.delete_item(conn)
    items = CItemsDAO.read_item(conn)
    for i in items:
        print(i.__str__())
        print('*'*11)