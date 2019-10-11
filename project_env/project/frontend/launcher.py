# -*- coding: utf-8 -*-

"""
Name of the file : lacuncher.py
Description : The aim of this file is to launch the program
"""

__author__ = 'koeman'
__copyright__ = ''
__credits__ = ['']
__licence__ = ''
__version__ = '0.0.1'
__maintainer__ = ''
__email__ = ''
__status__ = ''

from tkinter import (Tk, Label, StringVar, OptionMenu, Entry, Button,
                     filedialog, Listbox, Scrollbar)
from frontend.scrollable_table import ScrollableTable
from tkinter.constants import *
import json
import os
import sys

LABEL_BOLD_FONT = 'Arial 10 italic bold'
HEADER_MSG_LABEL = 'Times 12 bold'
WIN = not sys.platform.startswith('lin')

with open('{folder_abs_path}{separator}file_properties.json'.format(
                folder_abs_path=os.path.dirname(os.path.realpath(__file__)),
                separator="\\" if WIN else "/"
        ), 'r') as f:
    FILE_PROPERTIES = json.loads(f.read())

FILE_INFO = {'path': ''}


def center_window(parent, w=None, h=None): # or w=1500, h =1200
    """ to center the main window on the screen """
    # get screen width and height
    ws = parent.winfo_screenwidth()
    hs = parent.winfo_screenheight()
    # calculate position x, y
    w = w or ws
    h = h or hs
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


def do_nothing():
    pass


def to_nb_chars(my_string, nb=20):
    return my_string[:nb - 3] + '...' if len(my_string) > nb else my_string


def open_file(load_file_label):
    filename = filedialog.askopenfilename(initialdir="/", title="Choisissez le fichier",
                                          filetypes=(("Tout type", "*.*"),))
    if filename:
        FILE_INFO['path'] = filename
        load_file_label['text'] = to_nb_chars(filename, nb=100)


def launch_app():
    """
    This function launch the program main frame
    """
    mainframe = Tk()
    mainframe.title("Log File Analyzer")
    # center_window(parent=mainframe)

    header_label = Label(mainframe, text="Bienvenue dans Log File Analyzer."
                                         "Pour commencer, sélectionnez votre fichier de log."
                                         "Ensuite, veuillez préciser le type de log choisi",
                         font=HEADER_MSG_LABEL)
    header_label.grid(row=0, columnspan=6, padx=20, pady=20)

    load_file_button = Button(mainframe, text='Sélectionner le fichier', command=lambda: open_file(load_file_label))
    load_file_button.grid(row=1, column=0, sticky=E, padx=20, pady=20)

    load_file_label = Label(mainframe, text=FILE_INFO['path'], font="Arial 10 italic")
    load_file_label.grid(row=1, column=1, columnspan=5, sticky=W, padx=20, pady=20)

    file_type = Label(mainframe, text="Type de fichier:", font=LABEL_BOLD_FONT)
    file_type.grid(row=2, sticky=E, padx=20, pady=20)

    tkvar = StringVar(mainframe)

    # Set with options
    choices = list(FILE_PROPERTIES.keys())
    tkvar.set(choices[0])  # set the default option

    popupmenu = OptionMenu(mainframe, tkvar, *choices)
    popupmenu.grid(row=2, column=1)

    # we change dropdown value
    def change_dropdown(*args):
        print(tkvar.get())

    # link function to change dropdown
    tkvar.trace('w', change_dropdown)

    file_name = Label(mainframe, text="Nom du fichier:", font=LABEL_BOLD_FONT)
    file_name.grid(row=3, sticky=E, padx=20, pady=20)

    nb_lines = Label(mainframe, text="Nombre de lignes:", font=LABEL_BOLD_FONT)
    nb_lines.grid(row=4, sticky=E, padx=20, pady=20)

    # first_date_time = Label(mainframe, text="Première date/heure:", font=LABEL_BOLD_FONT)
    # first_date_time.grid(row=5, sticky=E, padx=20, pady=20)

    # last_date_time = Label(mainframe, text="Dernière date/heure:", font=LABEL_BOLD_FONT)
    # last_date_time.grid(row=6, sticky=E, padx=20, pady=20)

    columns_names = FILE_PROPERTIES[tkvar.get()]
    searched_columns = {}
    searched_buttons = {}
    searched_result_listboxes = {}
    for column_index, column_value in enumerate(columns_names):
        new_search_label = Label(mainframe, text=columns_names[column_index], font=LABEL_BOLD_FONT)
        new_search_label.grid(row=column_index + 2, column=2, padx=20, pady=20, sticky=E)

        searched_columns[column_value] = StringVar()
        new_search_entry = Entry(mainframe, textvariable=searched_columns[column_value])
        new_search_entry.grid(row=column_index + 2, column=3, padx=20, pady=20, sticky=W)

        new_search_button = Button(mainframe, text='->', command=do_nothing)
        new_search_button.grid(row=column_index + 2, column=4, padx=20, pady=20, sticky=W + E)
        searched_buttons[column_value] = new_search_button

        new_listbox = Listbox(mainframe)
        new_listbox.grid(row=column_index + 2, column=5, padx=20, pady=20, sticky=W + E)
        new_scrollbar = Scrollbar(mainframe, orient=VERTICAL, command=new_listbox.yview, width=30)
        new_scrollbar.grid(row=column_index+2, column=6)
        new_listbox.config(height=5, width=40, yscrollcommand=new_scrollbar.set)
        searched_result_listboxes[column_value] = new_listbox

        new_listbox.delete(0, END)
        new_listbox.insert(0, *["Au", "Cameroun", "Berceau", "De", "Nos", "Ancetres", "Va", "Debout", "Et", "Jaloux", "De", "Ta", "Liberté"])

    search_button = Button(mainframe, text='Rechercher', command=do_nothing)
    search_button.grid(row=len(columns_names) + 2, column=3, sticky=W, padx=20, pady=20)

    table = ScrollableTable(mainframe, ['      Column %s      ' % i for i in range(10)])
    table.set_data([[f'Cellule {i}-{j}' for j in range(10)] for i in range(20)])
    table.grid(row=len(columns_names) + 3, columnspan=8, sticky=N + E + W + S, padx=20, pady=20)

    mainframe.mainloop()
