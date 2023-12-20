import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 226)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(103, 226)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(197, 226)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(148, 21)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(148, 47)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(148, 124)
		self._textBox3.Name = "textBox3"
		self._textBox3.ReadOnly = True
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 5
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(148, 150)
		self._textBox4.Name = "textBox4"
		self._textBox4.ReadOnly = True
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 6
		# 
		# textBox5
		# 
		self._textBox5.Location = System.Drawing.Point(148, 176)
		self._textBox5.Name = "textBox5"
		self._textBox5.ReadOnly = True
		self._textBox5.Size = System.Drawing.Size(100, 20)
		self._textBox5.TabIndex = 7
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 24)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(130, 17)
		self._label1.TabIndex = 8
		self._label1.Text = "Sales for the month:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(12, 50)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(130, 17)
		self._label2.TabIndex = 9
		self._label2.Text = "Advance pay awarded:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(12, 127)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(130, 17)
		self._label3.TabIndex = 10
		self._label3.Text = "Commission Rate:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(12, 153)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(130, 17)
		self._label4.TabIndex = 11
		self._label4.Text = "Commission:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(12, 179)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(130, 17)
		self._label5.TabIndex = 12
		self._label5.Text = "Net Pay:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox5)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg240Comm"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Box1 = int(self._textBox1.Text)
		Box2 = int(self._textBox2.Text)
		Box3 = self._textBox3.Text
		Box4 = self._textBox4.Text
		Box5 = self._textBox5.Text
		
		bubble = 0
		ifspot = ""
		returned = 0

		if Box1 < 10000:
			bubble = 0.05
		elif Box1 < 15000:
			bubble = 0.1
		elif Box1 < 18000:
			bubble = 0.12
		elif Box1 < 22000:
			bubble = 0.14
		else:
			bubble = 0.16

		self._textBox3.Text = str(bubble * 100.00) + "0%"
		self._textBox4.Text = "$" + str(Box1 * bubble)
#		bob = int(self._textBox4.Text)
#		returned = Box3 - Box2
#		if returned < 0:
#			ifspot = "-"
#		self._textBox5.Text = str(ifspot) + "$" + str(returned)
		pass

	def Button2Click(self, sender, e):
		Box1 = self._textBox1
		Box2 = self._textBox2
		Box3 = self._textBox3
		Box4 = self._textBox4
		Box5 = self._textBox5
		Box1.Text = ""
		Box2.Text = ""
		Box3.Text = ""
		Box4.Text = ""
		Box5.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass