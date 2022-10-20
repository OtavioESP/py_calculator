import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

from components.button import Button


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
	{'text': '.', 'width': 125, 'height': 50, 'x': 0, 'y': 550},
	{'text': 'C', 'width': 250, 'height': 50, 'x': 0, 'y': 350},
	{'text': 'CC', 'width': 250, 'height': 50, 'x': 250, 'y': 350},
]

OPERATORS = ['+ ', '-', '/', '*']

class Calculator(QMainWindow):
	def __init__(self):
		super().__init__()
		self.value = ''
		self.historic = []
		self.setWindowTitle('Calculadora')
		[
			self._render_buttons(
			btn['text'],
			btn['width'],
			btn['height'],
			btn['x'],
			btn['y']) for btn in NUMERIC_BUTTONS
		]
		[
			self._render_buttons(
			btn['text'],
			btn['width'],
			btn['height'],
			btn['x'],
			btn['y']) for btn in FUNCTIONAL_BUTTONS
		]
		self.main_label = self._render_label('0', 50, 50)
		self.setFixedWidth(500)
		self.setFixedHeight(800)

	def add_value(self, text):
		if text == 'C':
			self.value[:-1]
			self.update_label(self.main_label, self.value)
			return
		
		elif text == 'CC':
			self.value = ''
			self.update_label(self.main_label, self.value)
			return

		elif text == '=':
			self.value = str(eval(self.value))
			self.historic.append(self.value)
			self.update_label(self.main_label, self.value)
			return

		elif text.isnumeric():
			self.value += text
			self.update_label(self.main_label, self.value)
			return

		else:
			self.value += f' {text} '
			self.update_label(self.main_label, self.value)
			return

	def update_label(self, component, value):
		component.setText(str(value))

	def _render_label(self, number, x, y):
		label = QLabel(f'{number}', self)
		label.move(x, y)
		return label

	def _render_buttons(self, text, width, height, x, y):
		button = QPushButton(text, self)
		button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
		# button.setToolTip('This is an example button')
		# setToolTip should only be returned if a flag its true
		button.setFixedWidth(width)
		button.setFixedHeight(height)
		button.move(x, y)
		button.clicked.connect(lambda: self.add_value(text))


app = QApplication(sys.argv)

window = Calculator()
window.show()

app.exec()