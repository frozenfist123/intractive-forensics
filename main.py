import tkinter as tk
from tkinter import ttk, NO, CENTER
from enum import Enum


class Tags(Enum):
    exection = "exection"
    file_creation = "file_creation"


class Columns(Enum):
    columns_id = "id"
    name = "Artifact_Name"
    decription = "Decruotion"
    columns_type = "type"


DATA_BASE = {0: {"extra data": "hello world!"}, 1: {"secret text and data": "secrets", "artifect": "me?"}}


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1000x1000')
        self.tree = ttk.Treeview()
        self.tree.pack()

        self.data_box = ttk.Treeview()
        self.data_box.pack()

        self._set_table()
        self._set_data_box()

        self.count = 0
        self.count_data_box = 0
        self._set_tags_colors()

        data = [
            [1, "Jack", "gold", Tags.exection.value],
            [2, "Tom", "Bronze", Tags.file_creation.value]

        ]
        self._insert_data(data)

        self.tree.bind("<Double-1>", self.OnDoubleClick)
        self.root.mainloop()

    def OnDoubleClick(self, event):
        item = self.tree.selection()[0]
        index = self.tree.item(item, "text")
        print("you clicked on", self.tree.item(item, "text"))
        print(DATA_BASE[int(index)])
        self._insert_data_box(DATA_BASE[int(index)])

    def _set_table(self):
        self.tree['columns'] = (
        Columns.columns_id.value, Columns.name.value, Columns.decription.value, Columns.columns_type.value)
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column(Columns.columns_id.value, anchor=CENTER, width=200)
        self.tree.column(Columns.name.value, anchor=CENTER, width=200)
        self.tree.column(Columns.decription.value, anchor=CENTER, width=200)
        self.tree.column(Columns.columns_type.value, anchor=CENTER, width=200)

        self.tree.heading("#0", text="", anchor=CENTER)
        self.tree.heading(Columns.columns_id.value, text=Columns.columns_id.value, anchor=CENTER)
        self.tree.heading(Columns.name.value, text=Columns.name.value, anchor=CENTER)
        self.tree.heading(Columns.decription.value, text=Columns.decription.value, anchor=CENTER)
        self.tree.heading(Columns.columns_type.value, text=Columns.columns_type.value, anchor=CENTER)

    def _set_data_box(self):
        self.data_box['columns'] = ("field", "values")
        self.data_box.column("#0", width=0, stretch=NO)
        self.data_box.column("field", anchor=CENTER, width=200)
        self.data_box.column("values", anchor=CENTER, width=200)

        self.data_box.heading("#0", text="", anchor=CENTER)
        self.data_box.heading("field", text="field", anchor=CENTER)
        self.data_box.heading("values", text="values", anchor=CENTER)

    def _set_tags_colors(self):
        self.tree.tag_configure(Tags.exection.value, background="blue")
        self.tree.tag_configure(Tags.file_creation.value, background="#ff0000")

    def _insert_collum(self, record):
        self.tree.insert(parent='', index='end', iid=self.count, text=str(self.count),
                         values=(record[0], record[1], record[2], record[3]), tag=record[3])
        self.count += 1

    def _insert_data_box(self, record):
        self._clear_data_box()
        for key, value in record.items():
            self.data_box.insert(parent='', index='end', iid=self.count_data_box, text=str(self.count_data_box),
                                 values=(key, value))
            self.count_data_box += 1

    def _insert_data(self, data):
        for record in data:
            self._insert_collum(record)

    def _clear_data_box(self):
        for i in self.data_box.get_children():
            self.data_box.delete(i)


if __name__ == "__main__":
    app = App()