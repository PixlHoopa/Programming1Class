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
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label16 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(366, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(174, 24)
		self._label1.TabIndex = 0
		self._label1.Text = "Input two Variables!"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(281, 48)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(170, 31)
		self._textBox1.TabIndex = 1
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
		self._label16.Location = System.Drawing.Point(914, 9)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(23, 23)
		self._label16.TabIndex = 20
		# 
		# label2
		# 
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label2.Font = System.Drawing.Font("Yu Gothic", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(245, 115)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(429, 170)
		self._label2.TabIndex = 21
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(468, 48)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(170, 31)
		self._textBox2.TabIndex = 22
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(277, 82)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(174, 24)
		self._label3.TabIndex = 23
		self._label3.Text = "Miles per Hour"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(464, 82)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(174, 24)
		self._label4.TabIndex = 24
		self._label4.Text = "Speed Limit"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(949, 439)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog82a"
		self.ResumeLayout(False)
		self.PerformLayout()
		


	def Button1Click(self, sender, e):
		
		PerHour = int(self._textBox1.Text)
		Limit = int(self._textBox2.Text)
		Fine = 20.00 + ((PerHour - Limit) * 5.00)
		
		self._label2.Text = "Total Price of Fine: $" + str(Fine)
		
		self._label16.BackColor = System.Drawing.Color.Green
		
		
		if self._textBox1.Text == "" or self._textBox2.Text == "":

			self._label16.BackColor = System.Drawing.Color.Yellow
			self._label2.Text = "Not enough Variables!"
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label2.Text = ""
		self._label16.BackColor = System.Drawing.Color.Red
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass