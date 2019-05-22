''' 
	mbb11d_hw3.py
	Marcus Barnes
	Python CIS4930-002 FALL '18
	Turn in you file FSUID hw3.py or FSUID hw3.tar on Canvas

	References:
	http://pyqt.sourceforge.net/Docs/PyQt4/qpainter.html
	http://pyqt.sourceforge.net/Docs/PyQt4/index.html 
	https://stackoverflow.com/questions/30229024/pyqt5-button-to-run-function-and-update-lcd?rq=1
	'''

import sys, pickle
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QRect, QRectF


class Homework3(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Homework 3 (Marcus Barnes)')
		self.direction = 0
		self.qp = QtGui.QPainter()
		self.image = DrawImage(self.qp)
		self.setup()

	def init_button(self):
		u_btn = QPushButton('Up', self)
		u_btn.clicked.connect(self.up_click)
		u_btn.resize(400, 100)
		u_btn.move(100,0)

		r_btn = QPushButton('Right', self)
		r_btn.clicked.connect(self.right_click)
		r_btn.resize(100, 400)
		r_btn.move(500,100)

		d_btn = QPushButton('Down', self)
		d_btn.clicked.connect(self.down_click)
		d_btn.resize(400, 100)
		d_btn.move(100,500)

		l_btn = QPushButton('Left', self)
		l_btn.clicked.connect(self.left_click)
		l_btn.resize(100, 400)
		l_btn.move(0,100)


	def set_direction(self, direction):
		self.direction = direction
		self.update()
	def up_click(self):
		self.set_direction(0)

	def right_click(self):
		self.set_direction(1)

	def down_click(self):
		self.set_direction(2)

	def left_click(self):
		self.set_direction(3)

	def paintEvent(self, event):
		self.qp.begin(self)
		self.image.draw(event, self.direction)

	def setup(self):
		self.setGeometry(400,400,600,600)
		self.init_button()
		self.show()

'''
Color Templates:
	White: (255,255,255)
	Black: (0,0,0)
	Gold: (255, 215, 0)
	QtCore.Qt.transparent
	pen.setColor(QtCore.Qt.transparent)
'''

class DrawImage(QtWidgets.QWidget):

	def __init__(self, qp):
		QtWidgets.QWidget.__init__(self)
		self.setFixedSize(700, 460)
		self.orientation = {
			0: (300, 180),
			1: (420, 300),
			2: (300, 420),
			3: (180, 300)
			}
		self.qp = qp


	def paintEvent(self, event):
		self.qp.begin(self)
		self.image.draw(event, self.direction)



	def draw_background(self, event):
		self.qp.setBrush(QColor(255 ,255 ,255))
		self.qp.drawRect(event.rect())

	def direction_setter(self, direction):
		self.direction = direction
		if self.direction == 0:
			self.draw_head_up1()
			self.draw_head_up2()
			self.draw_line_up()
		elif self.direction == 1:
			self.draw_head_right1()
			self.draw_head_right2()
			self.draw_line_right()
		elif self.direction == 2:
			self.draw_head_down1()
			self.draw_head_down2()
			self.draw_line_down()			
		elif self.direction == 3:
			self.draw_head_left1()
			self.draw_head_left2()
			self.draw_line_left()			
		else:
			return


	def draw_line_up(self):
		center= QPoint(QPoint(*self.orientation[0]))
		self.qp.setPen(QPen(QColor(0, 0, 0), 5))
		self.qp.drawLine(240, 180, 360, 180)

	def draw_head_up1(self):
		center= QPoint(QPoint(*self.orientation[0]))
		self.qp.setPen(QPen(QColor(0, 0, 0), 2))
		self.qp.setBrush(QColor(255, 255, 255))
		#self.qp.drawPie(200, 200, 75, 75, 0, 180 * 16)
		self.qp.drawEllipse(center, 60, -80)

	def draw_head_up2(self):
		center= QPoint(QPoint(*self.orientation[0]))
		self.qp.setPen(QPen(QColor(0, 0, 0), 2))
		self.qp.setBrush(QColor(255, 69, 0))
		#self.qp.drawPie(200, 200, 75, 75, 0, 180 * 16)
		self.qp.drawEllipse(center, 30, -40)

	def draw_line_right(self):
		self.qp.setPen(QPen(QColor(0, 0, 0), 5))
		self.qp.drawLine(430, 240, 430, 360)

	def draw_head_right1(self):

		center= QPoint(QPoint(*self.orientation[1]))
		self.qp.setPen(QPen(QColor(0, 0, 0), 2))
		self.qp.setBrush(QColor(255, 255, 255))
		#self.qp.drawPie(200, 200, 75, 75, 0, 180 * 16)
		self.qp.drawEllipse(center, 80, 60)

	def draw_head_right2(self):
		center= QPoint(QPoint(*self.orientation[1]))
		self.qp.setPen(QPen(QColor(0, 0, 0), 2))
		self.qp.setBrush(QColor(255, 69, 0))
		#self.qp.drawPie(200, 200, 75, 75, 0, 180 * 16)
		self.qp.drawEllipse(center, 40, 30)

	def draw_line_down(self):
		center= QPoint(QPoint(*self.orientation[0]))
		self.qp.setPen(QPen(QColor(0, 0, 0), 5))
		self.qp.drawLine(240, 430, 360, 430)

	def draw_head_down1(self):
		center= QPoint(QPoint(*self.orientation[2]))
		self.qp.setPen(QPen(QColor(0, 0, 0), 2))
		self.qp.setBrush(QColor(255, 255, 255))
		#self.qp.drawPie(200, 200, 75, 75, 0, 180 * 16)
		self.qp.drawEllipse(center, 60, 80)

	def draw_head_down2(self):
		center= QPoint(QPoint(*self.orientation[2]))
		self.qp.setPen(QPen(QColor(0, 0, 0), 2))
		self.qp.setBrush(QColor(255, 69, 0))
		#self.qp.drawPie(200, 200, 75, 75, 0, 180 * 16)
		self.qp.drawEllipse(center, 30, 40)

	def draw_line_left(self):
		self.qp.setPen(QPen(QColor(0, 0, 0), 5))
		self.qp.drawLine(180, 240, 180, 360)

	def draw_head_left1(self):
		center= QPoint(QPoint(*self.orientation[3]))
		self.qp.setPen(QPen(QColor(0, 0, 0), 2))
		self.qp.setBrush(QColor(255, 255, 255))
		#self.qp.drawPie(200, 200, 75, 75, 0, 180 * 16)
		self.qp.drawEllipse(center, 80, -60)

	def draw_head_left2(self):
		center= QPoint(QPoint(*self.orientation[3]))
		self.qp.setPen(QPen(QColor(0, 0, 0), 2))
		self.qp.setBrush(QColor(255, 69, 0))
		#self.qp.drawPie(200, 200, 75, 75, 0, 180 * 16)
		self.qp.drawEllipse(center, 40, -30)

	def draw_circle1(self):
		center = QPoint(300, 300)
		self.qp.setPen(QPen(QColor(255, 255, 255), 2))
		self.qp.setBrush(QColor(255, 255, 255))
		self.qp.drawEllipse(center, 25, 25)

	def draw_circle2(self):
		center = QPoint(300, 300)
		self.qp.setPen(QPen(QColor(255, 255, 255), 2))
		self.qp.setBrush(QColor(255, 69, 0))
		self.qp.drawEllipse(center, 75, 75)

	def draw_circle3(self):
		center = QPoint(300, 300)
		self.qp.setPen(QPen(QColor(0, 0, 0), 3))
		self.qp.setBrush(QColor(255, 255, 255))
		self.qp.drawEllipse(center, 125, 125)


	def cover_center(self):
		self.qp.setPen(QColor(255,255,255))
		self.qp.setBrush(QColor(255,255,255))
		self.qp.drawRect(QRectF(180, 180, 250, 250))

	def draw(self,event, direction):
		self.qp.setRenderHint(QPainter.Antialiasing)
		self.draw_background(event)
		self.direction_setter(direction)
		self.cover_center()
		self.draw_circle3()
		self.draw_circle2()
		self.draw_circle1()

		self.qp.end()



if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	homework = Homework3()
	sys.exit(app.exec_())


