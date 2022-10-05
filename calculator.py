import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

from components.button import Button

positions = {
	'left': {'x': 0, 'y': 400},
 	'center':{'x': 0, 'y': 400},
  	'right':{'x': 0, 'y': 400},
    'operation_side':{'x': 0, 'y': 400}
   }

NUMERIC_BUTTONS = [
	{'text': '1', 'width': 125, 'height': 50, 'x': 0, 'y': 400},
	{'text': '2', 'width': 125, 'height': 50, 'x': 125, 'y': 400},
	{'text': '3', 'width': 125, 'height': 50, 'x': 250, 'y': 400},
	{'text': '4', 'width': 125, 'height': 50, 'x': 0, 'y': 450},
	{'text': '5', 'width': 125, 'height': 50, 'x': 125, 'y': 450},
	{'text': '6', 'width': 125, 'height': 50, 'x': 250, 'y': 450},
	{'text': '7', 'width': 125, 'height': 50, 'x': 0, 'y': 500},
	{'text': '8', 'width': 125, 'height': 50, 'x': 125, 'y': 500},
	{'text': '9', 'width': 125, 'height': 50, 'x': 250, 'y': 500},
	{'text': '0', 'width': 125, 'height': 50, 'x': 125, 'y': 550},
]

FUNCTIONAL_BUTTONS = [
	{'text': '+', 'width': 125, 'height': 50, 'x': 375, 'y': 400},
	{'text': '-', 'width': 125, 'height': 50, 'x': 375, 'y': 450},
	{'text': '/', 'width': 125, 'height': 50, 'x': 375, 'y': 500},
	{'text': '*', 'width': 125, 'height': 50, 'x': 375, 'y': 550},
	{'text': '=', 'width': 125, 'height': 50, 'x': 250, 'y': 550},
	# {'text': '.', 'width': 125, 'height': 50, 'x': 0, 'y': 550},
]

class Calculator(QMainWindow):
	def __init__(self):
		super().__init__()
		self.first_number = 0
		self.second_number = 0
		self.current_number = ''
		self.setWindowTitle('Calculadora')
		[
			self.render_numeric_buttons(
			btn['text'],
			btn['width'],
			btn['height'],
			btn['x'],
			btn['y']) for btn in NUMERIC_BUTTONS
		]
		# [
		# 	self.render_functional_buttons(btn['text'] ,
		# 	btn['width'],
		# 	btn['height'],
		# 	btn['x'],
		# 	btn['y']) for btn in FUNCTIONAL_BUTTONS
		# ]
		self.main_label = self.render_label('0', 50, 50)
		self.second_label = self.render_label('', 20, 50)
		self.setFixedWidth(500)
		self.setFixedHeight(800)


	def button_clicked(self, text):
		if text.isnumeric():
			self.current_number += text
			self.main_label.setText(self.current_number)
			self.update(self.main_label)
		elif text == '=':
			self.first_number = self.current_number
			


	def update(self, component):
		component.adjustSize()

	def render_label(self, number, x, y):
		label = QLabel(f'{number}', self)
		label.move(x, y)
		return label

	def render_numeric_buttons(self, text, width, height, x, y):
		button = QPushButton(text, self)
		button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
		# button.setToolTip('This is an example button')
		# setToolTip should only be returned if a flag its true
		button.setFixedWidth(width)
		button.setFixedHeight(height)
		button.move(x, y)
		button.clicked.connect(lambda: self.button_clicked(text))

	def render_functional_buttons(self, text, width, height, x, y):
		button = QPushButton(text, self)
		button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
		# button.setToolTip('This is an example button')
		# setToolTip should only be returned if a flag its true
		button.setFixedWidth(width)
		button.setFixedHeight(height)
		button.move(x, y)
		button.clicked.connect(lambda: self.button_clicked(text))


app = QApplication(sys.argv)

window = Calculator()
window.show()

app.exec()