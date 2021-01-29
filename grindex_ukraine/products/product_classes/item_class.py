from grindex_ukraine.products.product_classes.brand_class import Brand
import logging

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
            logging.info("Set CIP price for item successful. Value (eur) = "+str(value))
        else: self.__cip = None
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
        if value == 'True':
            self.__promo = 'PROMO'
        else: self.__promo = 'NON-PROMO'

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
            if item.promo == 'PROMO':
                print('****************')
                print(item)

