import csv
import tkinter
from tkinter import Tk, Menu, font, END, messagebox

from dateutil.utils import today
import mysql.connector as mySql
import pyodbc



from grindex_ukraine.products.product_classes.item_class import SKU, SKUworkout


def get_items_from_csv():
    with open("items.csv", "r", encoding="UTF", newline="") as file:
        reader = csv.reader(file, delimiter=';')
        list_sku = []
        for row in reader:
            row[5+int(today().month)] = row[5+int(today().month)].replace(',', '.')
            item = SKU(row[0], row[1], row[2], row[3], row[4], row[5],
                       row[5+int(today().month)])  # row 6 is a current CIP price/ correct in file
            list_sku.append(item)
            # print(row[0], row[1],row[2],row[3],row[4],row[5],row[6])
        list_sku_main = list_sku[1:]
    return list_sku_main

list_items = get_items_from_csv()
from tkinter import Tk, BOTH, Listbox, StringVar, END
from tkinter.ttk import Frame, Label

sku_ = SKUworkout(list_items)
list_ = sku_.get_and_save_list_promo_RX()
dict = sku_.get_dictionary_item_actual_cip()
list_e = []
for item in list_:
    list_e.append(item)

class Items_cip_GUI(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title( "ITEMS` CIP PRICE")
        self.pack(fill=BOTH, expand=1)
        self.button_frame = tkinter.Frame(self.master)


        acts = list_e
        self.ok_button = tkinter.Button(self.button_frame, text='Show info', command=self.onclick)
        self.ok_button.pack(side='left')
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.master.destroy)
        self.quit_button.pack(side='left')
        self.button_frame.pack()
        lb = Listbox(self,width='70',height='15')

        for i in acts:
            lb.insert(END, i)

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
        x = dict[value]
        self.info_var.set(value)
        self.var.set(str('CIP price is ' + str(x) + ' euro'))

    def onclick(self):

        for i in list_items:
            if i.item == self.info_var.get():
                tkinter.messagebox.showinfo('INFO:', i.__str__())
            else: pass
#if __name__ == '__main__':
