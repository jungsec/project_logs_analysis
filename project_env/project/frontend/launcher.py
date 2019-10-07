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

from tkinter import (Tk, Label, Frame, StringVar, OptionMenu, Entry, Button,
                     filedialog)
from frontend.scrollable_table import ScrollableTable
from tkinter.constants import *

LABEL_BOLD_FONT = 'Arial 10 italic bold'
HEADER_MSG_LABEL = 'Times 12 bold'
file_info = {'path': ''}


def center_window(parent, w=1500, h=1300):
    """ to center the main window on the screen """
    # get screen width and height
    ws = parent.winfo_screenwidth()
    hs = parent.winfo_screenheight()
    # calculate position x, y
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
        file_info['path'] = filename
        load_file_label['text'] = to_nb_chars(filename, nb=70)


def launch_app():
    """
    This function launch the program main frame
    """
    mainframe = Tk()
    mainframe.title("Log File Analyzer")
    center_window(parent=mainframe)

    header_label = Label(mainframe, text="Bienvenue dans Log File Analyzer."
                                         "Pour commencer, sélectionnez votre fichier de log",
                         font=HEADER_MSG_LABEL)
    header_label.grid(row=0, columnspan=4, padx=20, pady=20)

    load_file_button = Button(mainframe, text='Sélectionner le fichier', command=lambda: open_file(load_file_label))
    load_file_button.grid(row=1, column=0, sticky=E, padx=20, pady=20)

    load_file_label = Label(mainframe, text=file_info['path'], font="Arial 10 italic")
    load_file_label.grid(row=1, column=1, columnspan=3, sticky=W, padx=20, pady=20)

    file_name = Label(mainframe, text="Nom du fichier:", font=LABEL_BOLD_FONT)
    file_name.grid(row=2, sticky=E, padx=20, pady=20)

    nb_lines = Label(mainframe, text="Nombre de lignes:", font=LABEL_BOLD_FONT)
    nb_lines.grid(row=3, sticky=E, padx=20, pady=20)

    first_date_time = Label(mainframe, text="Première date/heure:", font=LABEL_BOLD_FONT)
    first_date_time.grid(row=4, sticky=E, padx=20, pady=20)

    last_date_time = Label(mainframe, text="Dernière date/heure:", font=LABEL_BOLD_FONT)
    last_date_time.grid(row=5, sticky=E, padx=20, pady=20)

    file_type = Label(mainframe, text="Type de fichier:", font=LABEL_BOLD_FONT)
    file_type.grid(row=6, sticky=E, padx=20, pady=20)

    tkvar = StringVar(mainframe)

    # Dictionary with options
    choices = {'Apache Acces log', 'Nginx acces log', 'CVS file', 'Linux Syslog'}
    tkvar.set('Apache Acces log')  # set the default option

    popupmenu = OptionMenu(mainframe, tkvar, *choices)
    popupmenu.grid(row=6, column=1)

    # on change dropdown value
    def change_dropdown(*args):
        print(tkvar.get())

    # link function to change dropdown
    tkvar.trace('w', change_dropdown)

    columns_names = ['Adresse Ip', 'Date', 'Temps', 'email', 'Requête HTTP']
    searched_columns = []
    for column_index, _ in enumerate(columns_names):
        searched_columns.append(StringVar())
        new_label = Label(mainframe, text=columns_names[column_index], font=LABEL_BOLD_FONT)
        new_label.grid(row=column_index + 2, column=2, padx=20, pady=20, sticky=E)
        new_entry = Entry(mainframe, textvariable=searched_columns[column_index])
        new_entry.grid(row=column_index + 2, column=3, padx=20, pady=20, sticky=W)

    search_button = Button(mainframe, text='Rechercher', command=do_nothing)
    search_button.grid(row=len(columns_names) + 2, column=3, sticky=W, padx=20, pady=20)

    table = ScrollableTable(mainframe, ['Column %s' % i for i in range(10)])
    table.set_data([[f'Cellule {i}-{j}' for j in range(10)] for i in range(30)])
    table.grid(row=len(columns_names) + 3, columnspan=6, sticky=N + E + W + S, padx=20, pady=20)

    mainframe.mainloop()
