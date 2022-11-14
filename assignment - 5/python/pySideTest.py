import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import maya.cmds as cmds


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.cube = cmds.polyCube( sx=5, sy=5, sz=5 )
        self.sphere = cmds.polySphere(sx=10, sy=15, r=20)
        self.cone = cmds.polyCone( sx=10, sy=15, sz=5, r=20, h=10)
        self.cylinder = cmds.polyCylinder( sx=10, sy=15, sz=5, h=20)
        self.torus = cmds.polyTorus( sx=8, sy=16, r=10, sr=1 )

        
        self.model = [self.cube, self.sphere, self.cone, self.cylinder, self.torus]

        self.button = QtWidgets.QPushButton("Create Rando Polygon!")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.createPoly)

    @QtCore.Slot()
    def createPoly(self):
        self.random.choice(self.model)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())