import sys
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

tablecont = [[1, "foo"],
             [3121, "bar"],
             [3, "xdd"]]
app = QApplication(sys.argv)

table = QTableWidget()
table.setRowCount(len(tablecont))
table.setColumnCount(len(tablecont[0]))
table.setHorizontalHeaderLabels(["int", "name"])

for i, [code, name] in enumerate(tablecont):
    item_code = QTableWidgetItem(code)
    item_name = QTableWidgetItem(name)
    table.setItem(i, 0, item_code)
    table.setItem(i, 1, item_name)

table.show()
sys.exit(app.exec())
