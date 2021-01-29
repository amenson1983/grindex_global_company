import csv

from grindex_ukraine.products.product_classes.brand_class import Brand
from grindex_ukraine.products.product_classes.item_class import SKU, SKUworkout

if __name__ == '__main__':
    sku = SKU('AC Grindeks', 'AC Grindeks Ukraine','OTC','APILAK', True,'Апилак №25',5)

    with open("Планы на 2021.csv", "r", encoding="UTF", newline="") as file:
        reader = csv.reader(file,delimiter=';')
        list_sku = []
        for row in reader:
            row[6] = row[6].replace(',','.')
            item = SKU(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) #row 6 is a current CIP price/ correct in file
            list_sku.append(item)
            #print(row[0], row[1],row[2],row[3],row[4],row[5],row[6])
        list_sku_main = list_sku[0:]
        #print(list_sku_main)
        list_sku = SKUworkout(list_sku_main)
        #list_sku.print_promo()
        print('List of PROMO SKU:')
        print('********************')
        list_sku.print_promo_names()
        print('List of PROMO OTC SKU:')
        print('********************')
        list_sku.print_promo_OTC()
        print('List of PROMO RX SKU:')
        print('********************')
        list_sku.print_promo_RX()
        print('List of NON-PROMO SKU:')
        print('********************')
        list_sku.print_non_promo_names()
        print('List of NON-PROMO OTC SKU:')
        print('********************')
        list_sku.print_non_promo_OTC()
        print('List of NON-PROMO RX SKU:')
        print('********************')
        list_sku.print_non_promo_RX()