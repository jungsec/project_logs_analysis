# -*- coding: utf-8 -*-

"""
Name of the file : result_modal.py
Description : The modal dialog which displays search results in a table
"""

__author__ = 'koeman'
__copyright__ = ''
__credits__ = ['']
__licence__ = ''
__version__ = '0.0.1'
__maintainer__ = ''
__email__ = ''
__status__ = ''

from tkinter import Toplevel, Button, Label, filedialog, messagebox
from tkinter.constants import *
from frontend.scrollable_table import ScrollableTable
import datetime

ROWS_PER_PAGE = 20
PAGINATION_INFO = {'page_nb': 1}


def fill_with_space_to_nb_chars(my_string, nb=50):
    nb_space_before_string = (nb - len(my_string)) // 2 if len(my_string) < nb else 0
    nb_space_after_string = max(nb, len(my_string)) - len(my_string) - nb_space_before_string
    return f'{" " * nb_space_before_string}{my_string}{" " * nb_space_after_string}'


def get_page(page_nb=1, all_results=[], rows_per_page=ROWS_PER_PAGE):  # page_nb start by 1
    return all_results[(page_nb - 1) * rows_per_page: page_nb * rows_per_page]


def previous_page(table, pagination_label, all_data, previous_button, next_button):
    PAGINATION_INFO['page_nb'] -= 1
    pagination_label.config(text=f"page {PAGINATION_INFO['page_nb']} / {PAGINATION_INFO['page_count']}")
    if PAGINATION_INFO['page_nb'] == 1:
        previous_button.config(state=DISABLED)
    if next_button['state'] != NORMAL:
        next_button.config(state=NORMAL)
    table.set_data(get_page(page_nb=PAGINATION_INFO['page_nb'], all_results=all_data))


def next_page(table, pagination_label, all_data, previous_button, next_button):
    PAGINATION_INFO['page_nb'] += 1
    pagination_label.config(text=f"page {PAGINATION_INFO['page_nb']} / {PAGINATION_INFO['page_count']}")
    if PAGINATION_INFO['page_nb'] >= PAGINATION_INFO['page_count']:
        next_button.config(state=DISABLED)
    if previous_button['state'] != NORMAL:
        previous_button.config(state=NORMAL)
    table.set_data(get_page(page_nb=PAGINATION_INFO['page_nb'], all_results=all_data))


def export_to_csv(all_data):
    from frontend.launcher import FILE_INFO, WIN
    directory = filedialog.askdirectory(initialdir="/", title='Choisissez le repertoire de destination')
    if directory:
        dest_file_name = f"{str(datetime.datetime.now()).replace(' ', '_')}_{FILE_INFO['file_name']}"
        dest_file_name = directory + ('\\' if WIN else '/') + dest_file_name
        with open(dest_file_name, 'w+') as dest_file:
            for data_line in all_data:
                dest_file.write(f"{';'.join(data_line)}\r\n")
        messagebox.showinfo("Infos Export", f"Exportation csv terminée vers {dest_file_name}")


class ResultDialog(Toplevel):
    def __init__(self, parent, column_names, all_data):
        super().__init__(parent)
        self.title("Résultats de la recherche")

        pagination_label = Label(self,
                                 text=f"page {PAGINATION_INFO['page_nb']} / {PAGINATION_INFO['page_count']}",
                                 font="Arial 10 bold")
        pagination_label.grid(row=0, column=1, sticky=W + E, padx=20, pady=20)

        table = ScrollableTable(self, column_names)
        table.set_data(get_page(page_nb=PAGINATION_INFO['page_nb'], all_results=all_data))
        table.grid(row=1, columnspan=3, sticky=N + E + W + S, padx=20, pady=20)

        previous_button = Button(self, text='<-- précédent', state=DISABLED,
                                 command=lambda: previous_page(
                                     table, pagination_label, all_data, previous_button, next_button)
                                 )
        previous_button.grid(row=2, column=0, sticky=W, padx=20, pady=20)

        csv_button = Button(self, text='Exporter CSV', command=lambda: export_to_csv(all_data))
        csv_button.grid(row=2, column=1, sticky=W + E, padx=20, pady=20)

        next_button = Button(self, text='suivant -->', state=DISABLED if PAGINATION_INFO['page_nb'
                                                                         ] >= PAGINATION_INFO['page_count'] else NORMAL,
                             command=lambda: next_page(
                                 table, pagination_label, all_data, previous_button, next_button)
                             )
        next_button.grid(row=2, column=2, sticky=E, padx=20, pady=20)


def show_result_modal(mainframe, log_type_var, local_searched_columns, file_path,
                      FILE_PROPERTIES):
    """ Open the modal window """
    if not file_path: return

    all_data = [[f"Cellule {i} - {j}" for j in range(len(FILE_PROPERTIES[log_type_var.get()]))
                 ] for i in range(200)]  # TODO (Kyle) Change this with the method to get filtered results
    PAGINATION_INFO['page_nb'] = 1 if len(all_data) else 0
    PAGINATION_INFO['page_count'] = (len(all_data) + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE

    result = ResultDialog(mainframe, column_names=[
        fill_with_space_to_nb_chars(column) for column in
        FILE_PROPERTIES[log_type_var.get()]], all_data=all_data)

    result.transient(mainframe)
    result.grab_set()
    mainframe.wait_window(result)
