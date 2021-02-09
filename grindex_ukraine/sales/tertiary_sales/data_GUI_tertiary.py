import sqlite3
import tkinter
from tkinter import Tk, BOTH, Listbox, StringVar, END, messagebox
from tkinter.ttk import Frame, Label
import mysql.connector as mySql


class Tertiary_sales:
    def __init__(self, year, month, item, brand, weight_penetration, weight_sro, quantity, volume_euro):
        self.brand = brand
        self.item = item
        self.volume_euro = volume_euro
        self.quantity = quantity
        self.weight_sro = weight_sro
        self.weight_penetration = weight_penetration
        self.month = month
        self.year = year

    def __str__(self):
        return f"Year: {self.year}\nMonth: {self.month}\nItem: {self.item}\nBrand: {self.brand}\nWeighted penetration: {self.weight_penetration}\nWeighted SRO: {self.weight_sro}\nQuantity_pcs: {self.quantity}\nAmount_euro: {self.volume_euro}"

    def __repr__(self):
        return f"({self.year},{self.month},{self.item}, {self.brand}, {self.weight_penetration},{self.weight_sro},{self.quantity},{self.volume_euro})"


class CItemsDAO:
    def insert_item(conn, sales: Tertiary_sales):
        with sqlite3.connect("tertiary_sales_database.db") as conn:
            cursor = conn.cursor()
            # cursor.execute("INSERT INTO Tertiary_sales VALUES (276,'Djamala');")
            # cursor.execute(f"INSERT INTO Tertiary_sales VALUES (?,?)",(artist.item,f'{artist.brand}'))
            cursor.execute(f"INSERT INTO sales VALUES (?,?,?,?,?,?,?,?)", (f'({sales.year}', (f'{sales.month}'), (f'{sales.item}'), (f'{sales.weight_penetration}'), (f'{sales.weight_sro}'), (f'{sales.quantity}'), (f'{sales.volume_euro}')))

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
                "SELECT ymm.Year, ymm.Месяц, items.Itemcube, items.ITEMSBRAND, tertiary_sales.WeightPenetration, tertiary_sales.WeightSRO , tertiary_sales.Quantity, tertiary_sales.Volume from tertiary_sales join ymm on tertiary_sales.Period = ymm.Year_monnum JOIN items on tertiary_sales.Fullmedicationname = items.Fullmedicationname where tertiary_sales.MarketOrg = 'Grindeks  (Latvia)'")
            results = cursor.fetchall()
            artists = []
            for entry in results:
                artists.append(
                    Tertiary_sales(year=entry[0], month=entry[1], item=entry[2], brand=entry[3], weight_penetration=entry[4], weight_sro=entry[5], quantity=entry[6], volume_euro=entry[7])
                )
            return artists
conn = sqlite3.connect("tertiary_sales_database.db")
items = CItemsDAO.read_item(conn)
class Data_GUI(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title( "ITEMS` CIP PRICE")
        self.pack(fill=BOTH, expand=1)
        self.button_frame = tkinter.Frame(self.master)


        acts = items
        self.ok_button = tkinter.Button(self.button_frame, text='Show info', command=self.onclick)
        self.ok_button.pack(side='left')
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.master.destroy)
        self.quit_button.pack(side='left')
        self.button_frame.pack()
        lb = Listbox(self,width='70',height='15')

        for i in acts:
            lb.insert(END, i.item)

        lb.bind("<<ListboxSelect>>", self.onSelect)

        lb.pack(pady=15)

        self.var = StringVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.pack()
        self.info_var = StringVar()
        self.info_label = Label(self, text=0, textvariable=self.info_var)
        self.info_label.pack()

    def onSelect(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)
        x = value
        self.info_var.set(value)


    def onclick(self):

        for i in items:
            if i.item == self.info_var.get() and i.year == 2020:
                tkinter.messagebox.showinfo('INFO',f'Year:{i.year}, {i.month} Penetration: {i.weight_penetration} %' )
            else: pass

def list_work():
    root = Tk()
    ex = Data_GUI()
    root.geometry("500x550")
    root.mainloop()

if __name__ == '__main__':
    list_work()
#if __name__ == '__main__':
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

    #for i in items:
        #if i.year == 2020:
            #print(i.__str__())
            #print('*'*11)
