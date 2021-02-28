# Script-type currency converter
#Author: jech

# import sys
# import random
from PySide6 import *
from currency_converter import CurrencyConverter


class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Currency Converter")
        self.setStyleSheet("background: none;")
        self.c = CurrencyConverter()
        self.setup_ui()
        self.set_default_values()
        self.setup_connections()

    def setup_ui(self):
        # widgets
        self.layout = QtWidgets.QHBoxLayout(self)
        self.devise1 = QtWidgets.QComboBox()
        self.devise2 = QtWidgets.QComboBox()
        #self.label1 = QtWidgets.QLineEdit("")
        #self.label2 = QtWidgets.QLineEdit("")
        self.label1 = QtWidgets.QDoubleSpinBox()
        self.label2 = QtWidgets.QDoubleSpinBox()

        self.button = QtWidgets.QPushButton("Inverser devises")

        # layout
        self.layout.addWidget(self.devise1)
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.devise2)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.button)

    def set_default_values(self):
        # box
        allCurrencies = self.c.currencies
        self.devise1.addItems(sorted(list(allCurrencies)))
        self.devise2.addItems(sorted(list(allCurrencies)))
        self.devise1.setCurrentText("EUR")
        self.devise2.setCurrentText("USD")

        # labels
        # self.label1.setPlaceholderText("#")
        # self.label2.setPlaceholderText("#")
        self.label1.setRange(1, 1000000)
        self.label2.setRange(1, 1000000)
        self.label1.setValue(100)
        self.label2.setValue(121.08)

    def setup_connections(self):
        self.devise1.activated.connect(self.compute)
        self.devise2.activated.connect(self.compute)
        self.label1.valueChanged.connect(self.compute)

        self.button.clicked.connect(self.inverser_devise)

    def compute(self):
        montant = self.label1.value()
        devise_from = self.devise1.currentText()
        devise_to = self.devise2.currentText()
        try:
            resultat = self.c.convert(montant, devise_from, devise_to)
        except currency_converter.currency_converter.RateNotFoundError:
            print("The conversion didn't work")
        else:
            self.label2.setValue(resultat)

    def inverser_devise(self):
        devise_from = self.devise1.currentText()
        devise_to = self.devise2.currentText()
        self.devise1.setCurrentText(devise_to)
        self.devise2.setCurrentText(devise_from)
        self.compute()


# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])

#     widget = MyApp()
#     widget.resize(600, 400)
#     widget.show()

#     sys.exit(app.exec_())
