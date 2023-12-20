import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label16 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._textBox3 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(345, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(193, 24)
		self._label1.TabIndex = 0
		self._label1.Text = "Input three Variables!"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(144, 61)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(170, 31)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(368, 61)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(170, 31)
		self._textBox2.TabIndex = 2
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 350)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(273, 77)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(332, 350)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(273, 77)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(664, 350)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(273, 77)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.Color.Red
		self._label16.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label16.Location = System.Drawing.Point(899, 48)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(23, 23)
		self._label16.TabIndex = 20
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Yu Gothic", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(262, 162)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(365, 53)
		self._label2.TabIndex = 21
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Yu Gothic", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(48, 95)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(365, 53)
		self._label3.TabIndex = 22
		self._label3.Text = "Pounds"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Yu Gothic", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(262, 95)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(365, 53)
		self._label4.TabIndex = 23
		self._label4.Text = "Shillings"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Yu Gothic", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(505, 95)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(365, 53)
		self._label5.TabIndex = 24
		self._label5.Text = "Pence"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(589, 61)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(170, 31)
		self._textBox3.TabIndex = 25
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(949, 439)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog65h"
		self.ResumeLayout(False)
		self.PerformLayout()
		


	def Button1Click(self, sender, e):
		if self._textBox1.Text == "" or self._textBox2.Text == "" or self._textBox3.Text == "":

			self._label16.BackColor = System.Drawing.Color.Yellow
		else:
			Pound = int(self._textBox1.Text)
			Shil = int(self._textBox2.Text)
			Pence = int(self._textBox3.Text)
			PenShil =  Shil + (Pence/12.0)
			PoundPenShil = Pound + (PenShil/20.0)
			RoundPound = round(PoundPenShil, 2)
			
			self._label2.Text= "Pounds £: " + str(RoundPound)
			
			self._label16.BackColor = System.Drawing.Color.Green
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text= ""
		self._textBox2.Text= ""
		self._textBox3.Text= ""
		self._label2.Text= ""
		self._label16.BackColor = System.Drawing.Color.Red
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass
