from PyQt5 import QtWidgets, QtCore
from db_tools import DataBase
from pd_tools import PdTools

class View(object):
    mainWindow = None
    db = None

    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow

    def draw(self):
        '''Запуск всех методов'''
        self.setupWindow()
        self.setWidget()
        self.mainWindow.show()

    def setupWindow(self):
        '''Метод отрисовки главного окна, передача главнх параметров'''
        self.mainWindow.setFixedSize(950, 600)
        self.mainWindow.setWindowTitle(
            'Тестовое задание на должность PyQt-разработчика')

    def setWidget(self):
        '''Метод отрисовки "холста", на котором расположены элементы окна'''
        widget = QtWidgets.QWidget()
        self.db = DataBase()
        ids, usernames = self.db.selectAllAccounts()
        self.mainWindow.setCentralWidget(widget)
        title = QtWidgets.QLabel(widget)
        title.setText('Тестовое задание на должность PyQt-разработчика')
        title.setGeometry(QtCore.QRect(320, 20, 400, 20))

        table = QtWidgets.QTableWidget(widget)
        table.setGeometry(QtCore.QRect(50, 60, 850, 500))
        table.setColumnCount(1)
        table.setColumnWidth(0, 300)
        table.setHorizontalHeaderLabels(['Имя пользователя'])
        table.setRowCount(len(ids))
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for i in range(len(usernames)):
            item = QtWidgets.QTableWidgetItem()
            table.setItem(i, 0, item)
            item = table.item(i, 0)
            item.setText(usernames[i])
        table.cellDoubleClicked.connect(
            lambda: self.view_data(ids[table.currentRow()]))

    def view_data(self, id_acc):
        ''' метод отрисовки окна индивидуально аккаунта с детализацией '''
        widget = QtWidgets.QWidget()
        self.mainWindow.setCentralWidget(widget)

        btnBack = QtWidgets.QPushButton(widget)
        btnBack.setGeometry(QtCore.QRect(20, 20, 100, 30))
        btnBack.setText('Назад')
        btnBack.clicked.connect(lambda: self.setWidget())

        result = self.db.selectBets(id_acc)
        label = QtWidgets.QLabel(widget)
        if result == []:
            label = QtWidgets.QLabel(widget)
            label.setText('Нет данных о ставках данного пользователя')
            label.setGeometry(QtCore.QRect(300, 150, 500, 30))
        else:
            pdt = PdTools()
            data = pdt.get_data(result)
            label.setText(f'Данные о первых поступлениях\n{data}')
            label.setGeometry(QtCore.QRect(250, 100, 500, 300))


