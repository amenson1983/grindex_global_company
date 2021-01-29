import csv
import json
from dateutil.utils import today

from grindex_ukraine.products.product_classes.brand_class import Brand
from grindex_ukraine.products.product_classes.item_class import SKU, SKUworkout


def get_dict_from_file(filename):
    with open(filename, "r", encoding="UTF") as myfile:
        user_str = myfile.read()
    user_dict = json.loads(user_str)
    return user_dict

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
        list_sku_main = list_sku[0:]
    return list_sku_main

if __name__ == '__main__':
    list_sku_main = get_items_from_csv()
    list_sku = SKUworkout(list_sku_main)

    y = list_sku.get_dictionary_item_actual_cip()
    for i in y.keys():
        print(i, y[i])



    #us_dict = get_dict_from_file('item_cip_dictionary.json')
    #print(us_dict)
    #for i in us_dict:
        #print('SKU: ',i[0:len(i)],'\nCIP: ', us_dict[i[0:len(i)]])

    #list_sku.get_and_save_all_promo_names()
    #print('Save List of PROMO all the SKU`s to file is successfully completed!')
    #list_sku.get_and_save_list_promo_OTC()
    #print('Save List of PROMO OTC SKU to file is successfully completed!')
    #list_sku.get_and_save_list_promo_RX()
    #print('Save List of PROMO RX SKU to file is successfully completed!')


    #list_sku.get_and_save_list_non_promo_OTC()
    #print('Save List of NON-PROMO OTC SKU to file is successfully completed!')
    #list_sku.get_and_save_list_non_promo_RX()
    #print('Save List of NON-PROMO RX SKU to file is successfully completed!')

