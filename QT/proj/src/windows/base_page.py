from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QScrollArea, QFrame, QComboBox
from PyQt5.QtCore import Qt
from src.utils.product_data import get_product_data

class BasePage(QWidget):
    def __init__(self, title):
        super().__init__()

        self.layout = QVBoxLayout()

        # Только сетка с товарами и фильтрация
        self.filter_combobox = QComboBox()
        self.filter_combobox.addItems(["По возрастанию цены", "По убыванию цены"])
        self.filter_combobox.setVisible(False)  # скрыта, т.к. используется основная в MainWindow

        # Продукты и прокрутка
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_content = QWidget()
        self.product_grid = QGridLayout()
        self.product_grid.setSpacing(10)

        self.product_data = get_product_data(title)
        self.update_product_display()

        self.filter_combobox.currentIndexChanged.connect(self.update_product_display)

        self.scroll_area_content.setLayout(self.product_grid)
        self.scroll_area.setWidget(self.scroll_area_content)

        self.layout.addWidget(self.scroll_area)
        self.setLayout(self.layout)

    def update_product_display(self):
        for i in reversed(range(self.product_grid.count())):
            widget = self.product_grid.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        filter_text = self.filter_combobox.currentText()
        if filter_text == "По возрастанию цены":
            sorted_data = sorted(self.product_data, key=lambda x: x["price"])
        else:
            sorted_data = sorted(self.product_data, key=lambda x: x["price"], reverse=True)

        for i, data in enumerate(sorted_data):
            product_widget = QWidget()
            product_layout = QVBoxLayout()
            product_layout.setAlignment(Qt.AlignCenter)

            image = QLabel()
            image.setFixedSize(200, 200)
            image.setStyleSheet("background-color: lightgrey;")
            product_layout.addWidget(image)

            name = QLabel(data["name"])
            name.setAlignment(Qt.AlignCenter)
            product_layout.addWidget(name)

            price = QLabel(f"{data['price']} ₽")
            price.setAlignment(Qt.AlignCenter)
            product_layout.addWidget(price)

            product_widget.setLayout(product_layout)
            self.product_grid.addWidget(product_widget, i // 4, i % 4)
