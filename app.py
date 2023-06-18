import tkinter as tk
from controller import ControllerAirports
from model import AirportSearcher
from gui import Interface
from database_reader import database_connector


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Airports')

        """
        set database connection        
        """
        db = database_connector()
        """
        set the model
        """
        model = AirportSearcher()
        model.set_db(db)

        """
        set the interface
        """
        GUI = Interface(self)
        GUI.grid(row=0, column=0, padx=10, pady=10)

        """
        set the controller
        """
        controller = ControllerAirports(model, GUI)

        """
        connect the controller to the view
        """
        GUI.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()