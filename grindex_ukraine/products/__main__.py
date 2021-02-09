from tkinter import Tk

from grindex_ukraine.products.product_classes.item_class import SKUworkout
from grindex_ukraine.products.product_classes.items_GUI import Items_cip_GUI, list_items


def list_work():
    root = Tk()
    ex = Items_cip_GUI()
    root.geometry("450x350")
    root.mainloop()

if __name__ == '__main__':
    list_work()

