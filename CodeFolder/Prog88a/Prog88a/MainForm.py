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
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(372, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(170, 24)
		self._label1.TabIndex = 0
		self._label1.Text = "Input two Variables!"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(182, 37)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(170, 31)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(542, 37)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(170, 31)
		self._textBox2.TabIndex = 2
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkSalmon
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(229, 81)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(193, 28)
		self._label2.TabIndex = 3
		self._label2.Text = "Sum:			"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
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
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkSalmon
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(229, 120)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(193, 28)
		self._label3.TabIndex = 7
		self._label3.Text = "Difference:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkSalmon
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(229, 158)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(193, 28)
		self._label4.TabIndex = 8
		self._label4.Text = "Product:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkSalmon
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(229, 198)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(193, 28)
		self._label5.TabIndex = 11
		self._label5.Text = "Average:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DarkSalmon
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(229, 237)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(193, 28)
		self._label6.TabIndex = 10
		self._label6.Text = "Abs. Difference:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.DarkSalmon
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(229, 274)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(193, 28)
		self._label7.TabIndex = 9
		self._label7.Text = "Max:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.DarkSalmon
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(477, 198)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(193, 28)
		self._label8.TabIndex = 17
		self._label8.Text = " "
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.DarkSalmon
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(477, 237)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(193, 28)
		self._label9.TabIndex = 16
		self._label9.Text = " "
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.DarkSalmon
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(477, 274)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(193, 28)
		self._label10.TabIndex = 15
		self._label10.Text = " "
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.DarkSalmon
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(477, 158)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(193, 28)
		self._label11.TabIndex = 14
		self._label11.Text = " "
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.DarkSalmon
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(477, 120)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(193, 28)
		self._label12.TabIndex = 13
		self._label12.Text = " "
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.DarkSalmon
		self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(477, 81)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(193, 28)
		self._label13.TabIndex = 12
		self._label13.Text = " "
		self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.DarkSalmon
		self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.Location = System.Drawing.Point(228, 311)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(193, 28)
		self._label14.TabIndex = 18
		self._label14.Text = "Min:"
		self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.Color.DarkSalmon
		self._label15.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label15.Location = System.Drawing.Point(477, 311)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(193, 28)
		self._label15.TabIndex = 19
		self._label15.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
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
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(949, 439)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog88a"
		self.ResumeLayout(False)
		self.PerformLayout()
		


	def Button1Click(self, sender, e):
		if self._textBox1.Text == "" or self._textBox2.Text == "":
			self._label13.Text= "Not Enough Variables"
			self._label12.Text= "Not Enough Variables"
			self._label11.Text= "Not Enough Variables"
			self._label8.Text= "Not Enough Variables"
			self._label9.Text= "Not Enough Variables"
			self._label10.Text= "Not Enough Variables"
			self._label15.Text= "Not Enough Variables"
			self._label16.BackColor = System.Drawing.Color.Yellow
		else:
			Max = 0
			Min = 0
			Var1= int(self._textBox1.Text)
			Var2= int(self._textBox2.Text)
			if Var1 >= Var2:
				Max = Var1
				Min = Var2
			else:	
				Max = Var2
				Min = Var1
			
			Sum = Max + Min
			Diff = Var1 - Var2
			Prod = Var1 * Var2
			Avg = (Var1 + Var2)/2
			AbsDiff = abs(Diff)
			self._label13.Text= str(Sum)
			self._label12.Text= str(Diff)
			self._label11.Text= str(Prod)
			self._label8.Text= str(Avg)
			self._label9.Text= str(AbsDiff)
			self._label10.Text= str(Max)
			self._label15.Text= str(Min)
			self._label16.BackColor = System.Drawing.Color.Green
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text= ""
		self._textBox2.Text= ""
		self._label8.Text= ""
		self._label9.Text= ""
		self._label10.Text= ""
		self._label11.Text= ""
		self._label12.Text= ""
		self._label13.Text= ""
		self._label15.Text= ""
		self._label16.BackColor = System.Drawing.Color.Red
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

