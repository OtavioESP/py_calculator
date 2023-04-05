import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QSizePolicy

from components.button_sheetset import NUMERIC_BUTTONS, FUNCTIONAL_BUTTONS


OPERATORS = ['+ ', '-', '/', '*']

class Calculator(QMainWindow):
	def __init__(self):
		super().__init__()
		self.value = ''
		self.historic = []
		self.setWindowTitle('Calculadora')
		self.setStyleSheet("background-color: #2e2e2e; color: white")
		[
			self._render_buttons(
			btn['text'],
			btn['width'],
			btn['height'],
			btn['x'],
			btn['y'],
			btn['style_type']) for btn in NUMERIC_BUTTONS
		]
		[
			self._render_buttons(
			btn['text'],
			btn['width'],
			btn['height'],
			btn['x'],
			btn['y'],
			btn['style_type']) for btn in FUNCTIONAL_BUTTONS
		]
		self.main_label = self._render_label('0', 70, 70)
		self.main_label.setFont(QFont('Helvetica', 15))
		self.setFixedWidth(325)
		self.setFixedHeight(600)

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
			try:
				self.value = str(eval(self.value))
				self.historic.append(self.value)
				self.update_label(self.main_label, self.value)
				return
			except:
				self.historic.append('Error')
				self.update_label(self.main_label, 'Error')


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
		label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
		label.resize(600, 200)
		label.move(x, y)
		return label

	def _render_buttons(self, text, width, height, x, y, style_type):
		button = QPushButton(text, self)
		button.setStyleSheet(
			self.select_stylesheet(style_type)
		)
		# button.setToolTip('This is an example button')
		# setToolTip should only be returned if a flag its true
		button.setFixedWidth(width)
		button.setFixedHeight(height)
		button.move(x, y)
		button.clicked.connect(lambda: self.add_value(text))

	def select_stylesheet(self, style_type):
		style = {
			'numeric': 'QPushButton {background-color: #e0e0e0; color: black; border-radius: 25px; font: bold 14px;} QPushButton:pressed {background-color: #f2f2f2; border-style: inset;}',
			'operator': 'QPushButton {background-color: #e89e27; color: white; border-radius: 25px; font: bold 14px;} QPushButton:pressed {background-color: #f5dc1d; border-style: inset;}',
			'equals': 'QPushButton {background-color: #55e848; color: white; border-radius: 25px; font: bold 14px;} QPushButton:pressed {background-color: #99fc90; border-style: inset;}',
		}
		return style[style_type]


app = QApplication(sys.argv)

window = Calculator()
window.show()

app.exec()