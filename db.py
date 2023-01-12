import sys, time, os
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QTableView

db = QSqlDatabase.addDatabase('QMYSQL')
db.setHostName('localhost')
db.setDatabaseName('mydatabase')
db.setUserName('user')
db.setPassword('password')

# Otwórz połączenie z bazą danych
if not db.open():
    sys.exit(1)

# Utwórz obiekt QSqlTableModel reprezentujący tabelę z bazy danych
model = QSqlTableModel()
model.setTable('users')
model.setEditStrategy(QSqlTableModel.OnFieldChange)
model.select()

# Utwórz widok tabeli i powiąż go z modelem
view = QTableView()
view.setModel(model)
view.show()