import pathlib
from tkinter import *
from tkinter import messagebox

import customtkinter as ctk
import openpyxl
import xlrd
from openpyxl import Workbook

# Appearance settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ClientManagementSystem(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configure_layout()
        self.configure_appearance()

    def configure_layout(self):
        self.title("Customer Management System")
        self.geometry("700x500")
    
    def configure_appearance(self):
        self.label_theme = ctk.CTkLabel(
            self, text="Theme", bg_color="transparent", text_color=["#000000", "#FFFFFF"]
        ).place(x=50, y=430)

        self.theme_option = ctk.CTkOptionMenu(
            self, values=["Light", "Dark", "System"], command=self.change_appearance
        ).place(x=50, y=460)

    def change_appearance(self, new_appearance):
        ctk.set_appearance_mode(new_appearance)

if __name__ == "__main__":
    app = ClientManagementSystem()
    app.mainloop()
