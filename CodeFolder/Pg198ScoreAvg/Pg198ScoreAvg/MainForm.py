import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._body2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._Ready = System.Windows.Forms.TextBox()
		self._Set = System.Windows.Forms.TextBox()
		self._Go = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._Zombie = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# body2
		# 
		self._body2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._body2.Location = System.Drawing.Point(12, 9)
		self._body2.Name = "body2"
		self._body2.Size = System.Drawing.Size(287, 193)
		self._body2.TabIndex = 5
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(24, 3)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(125, 17)
		self._label1.TabIndex = 6
		self._label1.Text = "Enter Three Test Scores"
		# 
		# Ready
		# 
		self._Ready.Location = System.Drawing.Point(132, 57)
		self._Ready.Name = "Ready"
		self._Ready.Size = System.Drawing.Size(100, 20)
		self._Ready.TabIndex = 7
		# 
		# Set
		# 
		self._Set.Location = System.Drawing.Point(132, 84)
		self._Set.Name = "Set"
		self._Set.Size = System.Drawing.Size(100, 20)
		self._Set.TabIndex = 8
		# 
		# Go
		# 
		self._Go.Location = System.Drawing.Point(132, 109)
		self._Go.Name = "Go"
		self._Go.Size = System.Drawing.Size(100, 20)
		self._Go.TabIndex = 9
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(36, 239)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(151, 64)
		self._button1.TabIndex = 10
		self._button1.Text = "Calculate Average"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(191, 239)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(83, 32)
		self._button2.TabIndex = 11
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(191, 271)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(83, 32)
		self._button3.TabIndex = 12
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(12, 209)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(287, 23)
		self._label2.TabIndex = 13
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# Zombie
		# 
		self._Zombie.Location = System.Drawing.Point(132, 153)
		self._Zombie.Name = "Zombie"
		self._Zombie.ReadOnly = True
		self._Zombie.Size = System.Drawing.Size(100, 20)
		self._Zombie.TabIndex = 14
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(74, 57)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(52, 20)
		self._label3.TabIndex = 15
		self._label3.Text = "Score 1:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(74, 83)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(52, 20)
		self._label4.TabIndex = 16
		self._label4.Text = "Score 2:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(74, 109)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(52, 20)
		self._label5.TabIndex = 17
		self._label5.Text = "Score 3:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(74, 153)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(52, 20)
		self._label6.TabIndex = 18
		self._label6.Text = "Average:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(311, 328)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._Zombie)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._Go)
		self.Controls.Add(self._Set)
		self.Controls.Add(self._Ready)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._body2)
		self.Name = "MainForm"
		self.Text = "Pg198ScoreAvg"
		self.ResumeLayout(False)
		self.PerformLayout()
		
		
		

	def Button1Click(self, sender, e):
		nimble = int(self._Ready.Text)
		nomble = int(self._Set.Text)
		numble = int(self._Go.Text)
		zuma = round((nimble + nomble + numble)/3.0, 2)
		self._Zombie.Text = str(zuma)
		if zuma >= 95.0:
			self._label2.Text = "Congratulations! You're doing great!"
		pass

	def Button2Click(self, sender, e):
		self._Ready.Text = ""
		self._Set.Text = ""
		self._Go.Text = ""
		self._label2.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass