import sys
from PyQt5.QtWidgets import QPushButton

class Button:


	def generate_button(self):
		button = QPushButton()
		button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
		button.setText(self.text)
		button.move(self.x, self.y)
		button.setFixedWidth(self.x)
		button.setFixedHeight(self.y)

		button = QPushButton('PyQt5 button', self)
		button.setToolTip('This is an example button')
		button.move(100,70)

		return button
