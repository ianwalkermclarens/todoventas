import os
from PyQt6.QtGui import QIcon,QFont,QKeySequence
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QWidget, QMainWindow,QToolBar,QHBoxLayout,QToolButton
from gui.interfaces.uix_mainWindow import Ui_MainWindow
from gui.information_company import information_company
from file_sources import file_sources
from librery.confirm import confirms


basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,nombre_usuario,idkey_tipo_usuarios):
        super().__init__()
        self.setupUi(self)
        self.actionSalir.setShortcut(QKeySequence("Ctrl+X"))
        self.actionSalir.triggered.connect(self.exitApp)

        self.setStyleSheet("color: black;"
"background-color: white;font-size:15px;");
        sources = file_sources()
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        toolbar.setIconSize(QSize(64,64))
        toolbar.setStyleSheet("color: black;"
"background-color: white;font-size:15px;border:1px solid white;");

        layout = QHBoxLayout()
        layout.addStretch()        

        button_action = QToolButton()
        button_action.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        button_action.setStyleSheet("color: black;""background-color: white;font-size:15px;")
        button_action.setFont(QFont(sources.families, 25))
        button_action.setText("Ventas")
        button_action.setIcon(QIcon(os.path.join(sources.dirname_img,"ventas.png")))
        button_action.setIconSize(QSize(48,48))
        button_action.setStatusTip("Ventas")
        button_action.clicked.connect(self.pro1)
        

        button_action1 = QToolButton()
        button_action1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        button_action1.setStyleSheet("color: black;""background-color: white;font-size:15px;")
        button_action1.setFont(QFont(sources.families, 25))
        button_action1.setText("Operaciones")
        button_action1.setIcon(QIcon(os.path.join(sources.dirname_img,"operaciones.png")))
        button_action1.setIconSize(QSize(48,48))
        button_action1.setStatusTip("Operaciones")
        button_action1.clicked.connect(self.onMyToolBarButtonClick)


        button_action2 = QToolButton()
        button_action2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        button_action2.setStyleSheet("color: black;""background-color: white;font-size:15px;")
        button_action2.setFont(QFont(sources.families, 25))
        button_action2.setText("Almacen")
        button_action2.setIcon(QIcon(os.path.join(sources.dirname_img,"almacen.png")))
        button_action2.setIconSize(QSize(48,48))
        button_action2.setStatusTip("Almacen")
        button_action2.clicked.connect(self.onMyToolBarButtonClick)


        button_action3 = QToolButton()
        button_action3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        button_action3.setStyleSheet("color: black;""background-color: white;font-size:15px;")
        button_action3.setFont(QFont(sources.families, 25))
        button_action3.setText("Reportes")
        button_action3.setIcon(QIcon(os.path.join(sources.dirname_img,"reportes.png")))
        button_action3.setIconSize(QSize(48,48))
        button_action3.setStatusTip("Reportes")
        button_action3.clicked.connect(self.onMyToolBarButtonClick)


        layout.addWidget(button_action)
        layout.addWidget(button_action1)
        layout.addWidget(button_action2)                
        layout.addWidget(button_action3)        
        layout.addStretch()
        widget = QWidget()
        widget.setLayout(layout)


        toolbar.addWidget(widget)
        self.addToolBar(toolbar)

        """
        button_action = QAction(QIcon(os.path.join(sources.dirname_img,"operaciones.png")),"Operaciones",self)
        button_action.setStatusTip("operaciones")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        #button_action.setCheckable(True)
        toolbar.addAction(button_action)
        toolbar.addSeparator()


        button_action1 = QAction(QIcon(os.path.join(sources.dirname_img,"ventas.png")),"Ventas",self)
        button_action1.setStatusTip("Ventas")
        button_action1.triggered.connect(self.onMyToolBarButtonClick)
        #button_action1.setCheckable(True)
        toolbar.addAction(button_action1)
        toolbar.addSeparator()


        button_action2 = QAction(QIcon(os.path.join(sources.dirname_img,"almacen.png")),"Almacen",self)
        button_action2.setStatusTip("Almacen")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        #button_action2.setCheckable(True)
        toolbar.addAction(button_action2)
        toolbar.addSeparator()
        """



        self.showMaximized()



    def pro1(self,s):
        self.informacion_empresa = information_company()

    
    def exitApp(self,s):
        resultado = confirms("Esta seguro en salir de la aplicacion")
        if (resultado.getResult()==1):
            self.close()

    def onMyToolBarButtonClick(self,s):
        print("Click",s)



        



        



