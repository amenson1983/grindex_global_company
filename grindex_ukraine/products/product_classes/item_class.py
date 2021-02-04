
import logging
import json
import tkinter
import tkinter.font
import tkinter.messagebox
from grindex_ukraine.products.product_classes.brand_class import Brand

file_rx_non_promo = "rx_non_promo_list.txt"
file_otc_non_promo = "otc_non_promo_list.txt"
file_rx_promo = "rx_promo_list.txt"
file_otc_promo = "otc_promo_list.txt"
file_all_promo = "all_promo_list.txt"
item_cip = "item_act_cip_dictionary.csv"
file_all = "all_sku_list.txt"

logging.basicConfig(filename='product.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
class ITEMException(Exception):
    def __init__(self, str_err):
        Exception.__init__(self,str_err)

class SKU(Brand):
    def __init__(self,company_name,repres_office,sales_method,brand,promo,item,cip):
        Brand.__init__(self,company_name,repres_office,brand)
        self.sales_method = sales_method
        self.cip = cip
        self.item = item
        self.promo = promo

    @property
    def cip(self):
        return self.__cip

    @cip.setter
    def cip(self, value):
        if float(value)>0.001:
            self.__cip = float(value)
        else: self.__cip = None
        logging.info("Set CIP price for item successful. Value (eur) = " + str(value))
    @property
    def sales_method(self):
        return self.__sales_method

    @sales_method.setter
    def sales_method(self, value):
        self.__sales_method = value



    @property
    def promo(self):
        return self.__promo

    @promo.setter
    def promo(self, value):
        self.__promo = value

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, value):
        self.__item = value

    def __str__(self):
        return f"{Brand.__str__(self)} \nSales method: {self.sales_method} \nPROMO: {self.promo} \nSKU: {self.item} \nCIP: {self.cip}"
    def __repr__(self):
        return f"{Brand.__repr__(self)},{self.sales_method},{self.promo},{self.item},{self.cip}"
class SKUworkout():
    def __init__(self, list_items):
        self.list_items = list_items


    def print_promo(self):
        for item in self.list_items:
            if item.promo == 'True':
                print('****************')
                print(item)
    def get_and_save_all_promo_names(self):
        list_ = []
        with open(file_all_promo, "w", encoding="UTF", newline="") as file_write:
            for item in self.list_items:
                if item.promo == 'True':
                    file_write.write(item.item)
                    list_.append(item.item)
                    file_write.write('\n')
        logging.info("Writing all the PROMO items to a file " + str(file_all_promo) + " is successful!")
        return list_

    def get_and_save_all_sku(self):
        list_ = []
        with open(file_all_promo, "w", encoding="UTF", newline="") as file_write:
            for item in self.list_items:
                    file_write.write(item.item)
                    list_.append(item.item)
                    file_write.write('\n')
        logging.info("Writing all the items to a file " + str(file_all_promo) + " is successful!")
        return list_

    def get_and_save_list_promo_OTC(self):
        list_ = []
        with open(file_otc_promo, "w", encoding="UTF", newline="") as file_write:
            for item in self.list_items:
                if item.promo == 'True' and item.sales_method == 'ОТС':
                    file_write.write(item.item)
                    list_.append(item.item)
                    file_write.write('\n')
        logging.info("Writing PROMO OTC items to a file " + str(file_rx_promo) + " is successful!")
        return list_


    def get_and_save_list_promo_RX(self):
        list_ = []
        with open(file_rx_promo, "w", encoding="UTF", newline="") as file_write:
            for item in self.list_items:
                if item.promo == 'True' and item.sales_method == 'RX':
                    file_write.write(item.item)
                    list_.append(item.item)
                    file_write.write('\n')
        logging.info("Writing PROMO RX items to a file " + str(file_rx_promo) + " is successful!")
        return list_


    def print_non_promo_names(self):
        for item in self.list_items:
            if item.promo == 'False':
                print(item.item)
    def get_and_save_list_non_promo_OTC(self):
        list_ = []
        with open(file_otc_non_promo, "w", encoding="UTF", newline="") as file_write:
            for item in self.list_items:
                if item.promo == 'False' and item.sales_method == 'ОТС':
                    file_write.write(item.item)
                    list_.append(item.item)
                    file_write.write('\n')
        logging.info("Writing NON-PROMO OTC items to a file " + str(file_otc_non_promo) + " is successful!")
        return list_

    def get_and_save_list_non_promo_RX(self):
        list_ = []
        with open(file_rx_non_promo, "w", encoding="UTF", newline="") as file_write:
            for item in self.list_items:
                if item.promo == 'False' and item.sales_method == 'RX':
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




