import csv

from dateutil.utils import today

from grindex_ukraine.products.product_classes.item_class import SKU
from grindex_ukraine.products.product_classes.products_GUI import SKUworkoutGUI, get_items_from_csv_

if __name__ == '__main__':
    list_items = get_items_from_csv_()
    sku_workout = SKUworkoutGUI(list_items)