from database_reader import database_connector
from tkinter import *
from tkinter import ttk


class Interface(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)
        """
        set the controller
        """
        self.controller = None
        self.data_extractor = database_connector()

        self.frame1 = ttk.Frame(self)

        self.add(self.frame1, text="Airport locator")
        self.grid()

        """
        input field
        """
        self.lat_min_entry = ttk.Entry(self.frame1, width=25)
        self.lat_min_entry.insert(0, "0")
        self.lat_max_entry = ttk.Entry(self.frame1, width=25)
        self.lat_max_entry.insert(0, "0")
        self.lon_min_entry = ttk.Entry(self.frame1, width=25)
        self.lon_min_entry.insert(0, "0")
        self.lon_max_entry = ttk.Entry(self.frame1, width=25)
        self.lon_max_entry.insert(0, "0")

        """
        Labels
        """
        self.lat_min_label = ttk.Label(self.frame1, text="Min latitude:")
        self.lat_max_label = ttk.Label(self.frame1, text="Max latitude:")
        self.lon_min_label = ttk.Label(self.frame1, text="Min longitude:")
        self.lon_max_label = ttk.Label(self.frame1, text="Max longitude:")

        """
        Table
        """
        self.tree = ttk.Treeview(self.frame1, columns=("country", "city", "airport", "latitude", "longitude"),
                                 show="headings", height=40)
        self.tree.heading("city", text="city", anchor=W)
        self.tree.heading("country", text="country", anchor=W)
        self.tree.heading("airport", text="airport", anchor=W)
        self.tree.heading("latitude", text="latitude", anchor=W)
        self.tree.heading("longitude", text="longitude", anchor=W)
        self.tree.column("#1", stretch=NO, width=100)
        self.tree.column("#2", stretch=NO, width=120)
        self.tree.column("#3", stretch=NO, width=300)
        self.tree.column("#4", stretch=NO, width=140)
        self.tree.column("#5", stretch=NO, width=140)

 
        """
        Buttons
        """
        self.search_airports_btn = ttk.Button(self.frame1, text="Search airports", width=15,
                                              command=self.clicked_show_airports)
        self.clear_btn = ttk.Button(self.frame1, text="Clear forms", width=15, command=self.clicked_clear_form)

        """
        Grid template Airport locator
        """
        self.lat_min_label.grid(row=0, column=0)
        self.lat_max_label.grid(row=0, column=2)
        self.lon_min_label.grid(row=1, column=0)
        self.lon_max_label.grid(row=1, column=2)
        self.lat_min_entry.grid(row=0, column=1)
        self.lat_max_entry.grid(row=0, column=3)
        self.lon_min_entry.grid(row=1, column=1)
        self.lon_max_entry.grid(row=1, column=3)
        self.search_airports_btn.grid(row=0, column=4)
        self.clear_btn.grid(row=1, column=4)
        self.tree.grid(row=2, column=0, columnspan=5)


    def set_controller(self, controller):
        """
        set controller
        """
        self.controller = controller

    def clicked_show_airports(self):
        """
        airports show
        """
        if self.controller:
            self.controller.get_airports(self.lat_min_entry.get(),
                                         self.lat_max_entry.get(),
                                         self.lon_min_entry.get(),
                                         self.lon_max_entry.get())


    def clicked_clear_form(self):
        """
        clear form
        """
        self.tree.delete(*self.tree.get_children())
        self.lat_min_entry.delete(0, END)
        self.lat_min_entry.insert(0, "0")
        self.lat_max_entry.delete(0, END)
        self.lat_max_entry.insert(0, "0")
        self.lon_min_entry.delete(0, END)
        self.lon_min_entry.insert(0, "0")
        self.lon_max_entry.delete(0, END)
        self.lon_max_entry.insert(0, "0")

    def show_airports(self, airports):
        """
        the table of airports
        """
        self.tree.delete(*self.tree.get_children())
        for airport in airports:
            self.tree.insert("", END, values=airport)
