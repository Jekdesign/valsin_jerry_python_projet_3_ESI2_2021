# Script-type currency converter
#Author: jech

import sys
from PySide6 import *
import currencydevise

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = currencydevise.MyApp()
    widget.resize(600, 400)
    widget.show()

    sys.exit(app.exec_())
