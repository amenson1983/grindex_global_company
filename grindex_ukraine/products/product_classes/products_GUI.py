import csv
import logging
import json
import tkinter
import tkinter.font
import tkinter.messagebox

from dateutil.utils import today

from grindex_ukraine.products.product_classes.item_class import SKU

file_rx_non_promo = "rx_non_promo_list.txt"
file_otc_non_promo = "otc_non_promo_list.txt"
file_rx_promo = "rx_promo_list.txt"
file_otc_promo = "otc_promo_list.txt"
file_all_promo = "all_promo_list.txt"
item_cip = "item_act_cip_dictionary.csv"
csv_file = "../products/items.csv"

def get_items_from_csv_():
    with open(csv_file, "r", encoding="UTF", newline="") as file:
        reader = csv.reader(file, delimiter=';')
        list_sku = []
        for row in reader:
            row[5 + int(today().month)] = row[5 + int(today().month)].replace(',', '.')
            item = SKU(row[0], row[1], row[2], row[3], row[4], row[5],
                       row[5 + int(today().month)])  # row 6 is a current CIP price/ correct in file
            list_sku.append(item)
            # print(row[0], row[1],row[2],row[3],row[4],row[5],row[6])
        list_sku_main = list_sku[0:]
    return list_sku_main

logging.basicConfig(filename='product.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class ITEMException(Exception):
    def __init__(self, str_err):
        Exception.__init__(self,str_err)


class SKUworkoutGUI():
    def __init__(self, list_items):
        self.list_items = list_items
        self.main_window = tkinter.Tk()
        my_font = tkinter.font.Font(family='Arial', size=12)
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        tkinter.mainloop()

    def print_promo(self):
        for item in self.list_items:
            if item.promo == 'PROMO':
                print('****************')
                print(item)
    def get_and_save_all_promo_names(self):
        list_ = []
        with open(file_all_promo, "w", encoding="UTF", newline="") as file_write:
            for item in self.list_items:
                if item.promo == 'PROMO':
                    file_write.write(item.item)
                    list_.append(item.item)
                    file_write.write('\n')
        logging.info("Writing all the PROMO items to a file " + str(file_all_promo) + " is successful!")
        return list_

    def get_and_save_list_promo_OTC(self):
        list_ = []
        with open(file_otc_promo, "w", encoding="UTF", newline="") as file_write:
            for item in self.list_items:
                if item.promo == 'PROMO' and item.sales_method == 'ОТС':
                    file_write.write(item.item)
                    list_.append(item.item)
                    file_write.write('\n')
        logging.info("Writing PROMO OTC items to a file " + str(file_rx_promo) + " is successful!")
        return list_


    def get_and_save_list_promo_RX(self):
        list_ = []
        with open(file_rx_promo, "w", encoding="UTF", newline="") as file_write:
            for item in self.list_items:
                if item.promo == 'PROMO' and item.sales_method == 'RX':
                    file_write.write(item.item)
                    list_.append(item.item)
                    file_write.write('\n')
        logging.info("Writing PROMO RX items to a file " + str(file_rx_promo) + " is successful!")
        return list_


    def print_non_promo_names(self):
        for item in self.list_items:
            if item.promo == 'NON-PROMO':
                print(item.item)
    def get_and_save_list_non_promo_OTC(self):
        list_ = []
        with open(file_otc_non_promo, "w", encoding="UTF", newline="") as file_write:
            for item in self.list_items:
                if item.promo == 'NON-PROMO' and item.sales_method == 'ОТС':
                    file_write.write(item.item)
                    list_.append(item.item)
                    file_write.write('\n')
        logging.info("Writing NON-PROMO OTC items to a file " + str(file_otc_non_promo) + " is successful!")
        return list_

    def get_and_save_list_non_promo_RX(self):
        list_ = []
        with open(file_rx_non_promo, "w", encoding="UTF", newline="") as file_write:
            for item in self.list_items:
                if item.promo == 'NON-PROMO' and item.sales_method == 'RX':
                    file_write.write(item.item)
                    list_.append(item.item)
                    file_write.write('\n')
        logging.info("Writing NON-PROMO RX items to a file " + str(file_rx_non_promo) + " is successful!")
        return list_

    def get_dictionary_item_actual_cip(self):
        dict_= {}
        for item in self.list_items:
            entry = {item.item:item.cip}
            dict_.update(entry)
        strData = json.dumps(dict_)
        with open("item_cip_dictionary.json", "w") as file:
            file.write(strData)
            #with open(item_cip, "w", newline="") as file:
                #columns = ["SKU","CIP"]
                #writer = csv.DictWriter(file, fieldnames=columns)
                #writer.writeheader()

                # запись нескольких строк
                #writer.writerows(dict_)
        return dict_

