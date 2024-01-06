import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMenu, QMenuBar, QAction, QFileDialog
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush, QIcon, QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.triangle = False
        self.trianglePoints = []

        self.eraser = False
        top = 400
        left = 400
        height = 600
        width = 800

        icon = 'pain.png'

        self.setWindowTitle('Painter')
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon(icon))

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black

        self.lastPoint = QPoint()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        brushMenu = mainMenu.addMenu('Brush Size')
        brushColor = mainMenu.addMenu('Brush Color')
        filling = mainMenu.addMenu('Filling')
        shape = mainMenu.addMenu('Triangle')

        saveAction = QAction(QIcon('save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+S')
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        triangleAction = QAction(QIcon(), 'Triangle', self)
        triangleAction.setShortcut('Ctrl+R')
        shape.addAction(triangleAction)
        triangleAction.triggered.connect(self.toggleTriangle)

        eraserAction = QAction(QIcon('earaser.jpg'), 'Eraser', self)
        eraserAction.setShortcut('Ctrl+E')
        filling.addAction(eraserAction)
        eraserAction.triggered.connect(self.toggleEraser)

        clearAction = QAction(QIcon('clear.png'), 'Clear', self)
        clearAction.setShortcut('Ctrl+C')
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        green_fillingAction = QAction(QIcon('green.png'), 'Green', self)
        green_fillingAction.setShortcut('Ctrl+P')
        filling.addAction(green_fillingAction)
        green_fillingAction.triggered.connect(self.filling_green)

        red_fillingAction = QAction(QIcon('red.jpg'), 'Red', self)
        red_fillingAction.setShortcut('Ctrl+K')
        filling.addAction(red_fillingAction)
        red_fillingAction.triggered.connect(self.filling_red)

        yellow_fillingAction = QAction(QIcon('yellow.png'), 'Yellow', self)
        yellow_fillingAction.setShortcut('Ctrl+O')
        filling.addAction(yellow_fillingAction)
        yellow_fillingAction.triggered.connect(self.filling_yellow)

        black_fillingAction = QAction(QIcon('black.png'), 'Black', self)
        black_fillingAction.setShortcut('Ctrl+E')
        filling.addAction(black_fillingAction)
        black_fillingAction.triggered.connect(self.filling_black)

        threepxAction = QAction(QIcon('threepx.png'), '3px', self)
        threepxAction.setShortcut('Ctrl+T')
        brushMenu.addAction(threepxAction)
        threepxAction.triggered.connect(self.threepx)

        fivepxAction = QAction(QIcon('fivepx.png'), '5px', self)
        fivepxAction.setShortcut('Ctrl+F')
        brushMenu.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivepx)

        sevenpxAction = QAction(QIcon('sevenpx.png'), '7px', self)
        sevenpxAction.setShortcut('Ctrl+1')
        brushMenu.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenpx)

        ninepxAction = QAction(QIcon('ninepx.png'), '9px', self)
        ninepxAction.setShortcut('Ctrl+N')
        brushMenu.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninepx)

        blackAction = QAction(QIcon('black.png'), 'Black', self)
        blackAction.setShortcut('Ctrl+B')
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackColor)

        redAction = QAction(QIcon('red.jpg'), 'Red', self)
        redAction.setShortcut('Ctrl+W')
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.redColor)

        greenAction = QAction(QIcon('green.png'), 'Green', self)
        greenAction.setShortcut('Ctrl+G')
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.greenColor)

        yellowAction = QAction(QIcon('yellow.png'), 'Yellow', self)
        yellowAction.setShortcut('Ctrl+M')
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowColor)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
        if event.button() == Qt.LeftButton:
            if self.triangle:
                self.trianglePoints.append(event.pos())
                if len(self.trianglePoints) == 3:
                    self.drawTriangle()
                    self.triangle = True
            else:
                self.drawing = True
                self.lastPoint = event.pos()

    def drawTriangle(self):
        painter = QPainter(self.image)
        if self.eraser:
            painter.setPen(QPen(Qt.white, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        else:
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(self.trianglePoints[0], self.trianglePoints[1])
        painter.drawLine(self.trianglePoints[1], self.trianglePoints[2])
        painter.drawLine(self.trianglePoints[2], self.trianglePoints[0])
        self.update()
        self.triangle = True

    def toggleTriangle(self):
        self.triangle = not self.triangle
        if self.triangle:
            self.brushSize = 1

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton & self.drawing:
            painter = QPainter(self.image)
            if self.eraser:
                painter.setPen(QPen(Qt.white, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            else:
                painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()


    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False
            self.update()

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
        if self.triangle:
            painter = QPainter(self)
            if self.eraser:
                painter.setPen(QPen(Qt.white, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            else:
                painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            if len(self.trianglePoints) == 2:
                painter.drawLine(self.trianglePoints[0], self.trianglePoints[1])
            elif len(self.trianglePoints) == 3:
                painter.drawLine(self.trianglePoints[0], self.trianglePoints[1])
                painter.drawLine(self.trianglePoints[1], self.trianglePoints[2])
                painter.drawLine(self.trianglePoints[2], self.trianglePoints[0])

    def save(self):
        filepath = QFileDialog.getSaveFileName(self, 'Save image', '',
                                               'PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)')
        if filepath == '':
            return
        self.image.save(filepath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def toggleEraser(self):
        self.eraser = not self.eraser
        if self.eraser:
            self.brushColor = Qt.white
        else:
            self.brushColor = Qt.black

    def filling_green(self):
        self.image.fill(Qt.green)
        self.update()

    def filling_red(self):
        self.image.fill(Qt.red)
        self.update()

    def filling_yellow(self):
        self.image.fill(Qt.yellow)
        self.update()

    def filling_black(self):
        self.image.fill(Qt.black)
        self.update()

    def threepx(self):
        self.brushSize = 3

    def fivepx(self):
        self.brushSize = 5

    def sevenpx(self):
        self.brushSize = 7

    def ninepx(self):
        self.brushSize = 9

    def blackColor(self):
        self.brushColor = Qt.black

    def yellowColor(self):
        self.brushColor = Qt.yellow

    def redColor(self):
        self.brushColor = Qt.red

    def greenColor(self):
        self.brushColor = Qt.green


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())





