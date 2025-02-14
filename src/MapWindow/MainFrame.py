from PyQt6.QtWidgets import QWidget, QVBoxLayout,QHBoxLayout,QGridLayout,QPushButton, QComboBox, QGraphicsView, QGraphicsScene,QGraphicsItem,QGraphicsRectItem
from resources import *
from MapWindow.MapView import MapView

maps = {
    "DeSalle" : resource_path("assets/img/maps/DeSalle.svg"),
    "Lawson Delta" : resource_path("assets/img/maps/Lawson.svg"),
    "Stillwater Bayou" : resource_path("assets/img/maps/Stillwater.svg")
}

class MainFrame(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.SelectMap = QComboBox()
        self.SelectMap.view().setSpacing(4)

        self.SelectMap.activated.connect(self.update)

        for name in maps.keys():
            self.SelectMap.addItem(name,maps[name])

        self.current = list(maps.keys())[0]

        self.layout.addWidget(self.SelectMap)

        self.mapView = MapView()
        self.initButtons()
        self.layout.addWidget(self.mapView)
        self.layout.addStretch()
        self.rulerMode = False

    def initButtons(self):
        self.buttons = QWidget()
        self.buttons.layout = QGridLayout()
        self.buttons.setLayout(self.buttons.layout)
        self.buttons.spawns = QPushButton("Toggle Player Spawns")
        self.buttons.spawns.clicked.connect(self.mapView.ToggleSpawnPoints)
        self.buttons.beetles = QPushButton("Toggle Beetle Spawns")
        self.buttons.beetles.clicked.connect(self.mapView.ToggleBeetles)
        self.buttons.names = QPushButton("Toggle Compound Names")
        self.buttons.names.clicked.connect(self.mapView.ToggleCompoundNames)
        self.buttons.borders = QPushButton("Toggle Compound Borders")
        self.buttons.borders.clicked.connect(self.mapView.ToggleCompoundBorders)
        self.buttons.ruler = QPushButton("Ruler....")
        self.buttons.ruler.clicked.connect(self.mapView.toggleRuler)
        self.buttons.layout.addWidget(self.buttons.spawns,0,0)
        self.buttons.layout.addWidget(self.buttons.beetles,0,1)
        self.buttons.layout.addWidget(self.buttons.names,1,0)
        self.buttons.layout.addWidget(self.buttons.borders,1,1)
        self.buttons.layout.addWidget(self.buttons.ruler,0,2)
        for i in range(self.buttons.layout.count()):
            if type(self.buttons.layout.itemAt(i)) == QWidget:
                self.buttons.layout.itemAt(i).setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
        self.layout.addWidget(self.buttons)


    def update(self):
        self.current = self.SelectMap.currentText()
        self.mapView.setMap(self.current)