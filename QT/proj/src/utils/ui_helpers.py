# src/utils/ui_helpers.py

from PyQt5.QtWidgets import QComboBox

def create_combobox(items, on_filter_changed):
    combo_box = QComboBox()
    combo_box.addItems(items)
    combo_box.currentIndexChanged.connect(on_filter_changed)
    return combo_box
