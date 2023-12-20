import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._checker = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(205, 47)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(612, 47)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Location = System.Drawing.Point(12, 70)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(942, 268)
		self._label1.TabIndex = 2
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.SaddleBrown
		self._button1.Font = System.Drawing.Font("Palatino Linotype", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 341)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(293, 70)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# checker
		# 
		self._checker.BackColor = System.Drawing.Color.Red
		self._checker.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._checker.Location = System.Drawing.Point(934, 9)
		self._checker.Name = "checker"
		self._checker.Size = System.Drawing.Size(20, 19)
		self._checker.TabIndex = 4
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.SaddleBrown
		self._button2.Font = System.Drawing.Font("Palatino Linotype", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(338, 341)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(293, 70)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.SaddleBrown
		self._button3.Font = System.Drawing.Font("Palatino Linotype", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(661, 341)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(293, 70)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Sienna
		self.ClientSize = System.Drawing.Size(966, 423)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._checker)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Prog162h"
		self.ResumeLayout(False)
		self.PerformLayout()
		

	def factorial(self, n):
		Light = n # This will be the returned
		Balloon = n # This will be the counter
		while Balloon > 1:
			Balloon = Balloon - 1
			Light = Light * Balloon
		return Light
		pass
	
	def Button1Click(self, sender, e):
		if self._textBox1.Text == "" or self._textBox2.Text == "":

			self._checker.BackColor = System.Drawing.Color.Yellow
			self._label1.Text = "Not enough Variables!"
			return
		WineGlass = abs(int(self._textBox1.Text) - int(self._textBox2.Text))
		Wine      = int(self._textBox1.Text)
		Olive     = int(self._textBox2.Text)
		Gouda     = 1
		Salad     = WineGlass
		Dressing  = WineGlass

		while Olive < Wine:
			Olive = Olive + 1
			Gouda = Olive * Gouda
		if Olive == Wine:
			while Dressing > 1:
				Dressing = Dressing - 1
				Salad = Salad * Dressing
			Feta = 5
			DinnerPlate = (math.factorial(Wine))/(math.factorial(WineGlass))
		self._label1.Text = "Ways to arrange the guests: " + str(DinnerPlate) + "\n\nGuests left to stand: " + str(WineGlass)

		self._checker.BackColor = System.Drawing.Color.Green
		
		

		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label1.Text   = ""
		self._checker.BackColor = System.Drawing.Color.Red
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass