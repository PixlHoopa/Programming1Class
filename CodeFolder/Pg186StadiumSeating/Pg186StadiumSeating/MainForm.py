import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._body1 = System.Windows.Forms.Label()
		self._title1 = System.Windows.Forms.Label()
		self._title2 = System.Windows.Forms.Label()
		self._body2 = System.Windows.Forms.Label()
		self._ketchup = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._mustard = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._ranch = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._LostInTheSauce = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._Curd = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._Fry = System.Windows.Forms.TextBox()
		self._label7 = System.Windows.Forms.Label()
		self._French = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# body1
		# 
		self._body1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._body1.Location = System.Drawing.Point(12, 9)
		self._body1.Name = "body1"
		self._body1.Size = System.Drawing.Size(251, 192)
		self._body1.TabIndex = 0
		self._body1.Text = """
     Enter the number of tickets sold for
     each class of seats"""
		# 
		# title1
		# 
		self._title1.Location = System.Drawing.Point(13, 4)
		self._title1.Name = "title1"
		self._title1.Size = System.Drawing.Size(68, 18)
		self._title1.TabIndex = 2
		self._title1.Text = "Tickets Sold"
		# 
		# title2
		# 
		self._title2.Location = System.Drawing.Point(270, 4)
		self._title2.Name = "title2"
		self._title2.Size = System.Drawing.Size(118, 18)
		self._title2.TabIndex = 3
		self._title2.Text = "Revenue Generated"
		# 
		# body2
		# 
		self._body2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._body2.Location = System.Drawing.Point(269, 9)
		self._body2.Name = "body2"
		self._body2.Size = System.Drawing.Size(251, 192)
		self._body2.TabIndex = 4
		# 
		# ketchup
		# 
		self._ketchup.Location = System.Drawing.Point(380, 54)
		self._ketchup.Name = "ketchup"
		self._ketchup.ReadOnly = True
		self._ketchup.Size = System.Drawing.Size(100, 20)
		self._ketchup.TabIndex = 5
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(329, 54)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(47, 26)
		self._label1.TabIndex = 6
		self._label1.Text = "Class A:"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(329, 80)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(47, 20)
		self._label2.TabIndex = 8
		self._label2.Text = "Class B:"
		# 
		# mustard
		# 
		self._mustard.Location = System.Drawing.Point(380, 80)
		self._mustard.Name = "mustard"
		self._mustard.ReadOnly = True
		self._mustard.Size = System.Drawing.Size(100, 20)
		self._mustard.TabIndex = 7
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(329, 106)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(47, 20)
		self._label3.TabIndex = 10
		self._label3.Text = "Class C:"
		# 
		# ranch
		# 
		self._ranch.Location = System.Drawing.Point(380, 106)
		self._ranch.Name = "ranch"
		self._ranch.ReadOnly = True
		self._ranch.Size = System.Drawing.Size(100, 20)
		self._ranch.TabIndex = 9
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(295, 148)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(81, 20)
		self._label4.TabIndex = 12
		self._label4.Text = "Total Revenue:"
		# 
		# LostInTheSauce
		# 
		self._LostInTheSauce.Location = System.Drawing.Point(380, 148)
		self._LostInTheSauce.Name = "LostInTheSauce"
		self._LostInTheSauce.ReadOnly = True
		self._LostInTheSauce.Size = System.Drawing.Size(100, 20)
		self._LostInTheSauce.TabIndex = 11
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(43, 142)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(47, 20)
		self._label5.TabIndex = 18
		self._label5.Text = "Class C:"
		# 
		# Curd
		# 
		self._Curd.Location = System.Drawing.Point(94, 142)
		self._Curd.Name = "Curd"
		self._Curd.Size = System.Drawing.Size(100, 20)
		self._Curd.TabIndex = 17
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(43, 116)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(47, 20)
		self._label6.TabIndex = 16
		self._label6.Text = "Class B:"
		# 
		# Fry
		# 
		self._Fry.Location = System.Drawing.Point(94, 116)
		self._Fry.Name = "Fry"
		self._Fry.Size = System.Drawing.Size(100, 20)
		self._Fry.TabIndex = 15
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(43, 90)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(47, 26)
		self._label7.TabIndex = 14
		self._label7.Text = "Class A:"
		# 
		# French
		# 
		self._French.Location = System.Drawing.Point(94, 90)
		self._French.Name = "French"
		self._French.Size = System.Drawing.Size(100, 20)
		self._French.TabIndex = 13
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(60, 214)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(134, 35)
		self._button1.TabIndex = 19
		self._button1.Text = "Calculate Revenue"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(200, 214)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(134, 35)
		self._button2.TabIndex = 20
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(340, 214)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(134, 35)
		self._button3.TabIndex = 21
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(530, 261)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._Curd)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._Fry)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._French)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._LostInTheSauce)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._ranch)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._mustard)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._ketchup)
		self.Controls.Add(self._title2)
		self.Controls.Add(self._body2)
		self.Controls.Add(self._title1)
		self.Controls.Add(self._body1)
		self.Name = "MainForm"
		self.Text = "Pg186StadiumSeating"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		amoney = 15
		bmoney = 12
		cmoney = 9
		French = float(self._French.Text)
		Fry = float(self._Fry.Text)
		Curd = float(self._Curd.Text)
		KT = self._ketchup
		MT = self._mustard
		RN = self._ranch
		# A is French / ketchup
		# B is Fry / mustard
		# C is Curd / ranch
		ClassSeat1 = round(French * 15, 2)
		ClassSeat2 = round(Fry * 12, 2)
		ClassSeat3 = round(Curd * 9, 2)
		KT.Text = "$" + str(ClassSeat1)
		MT.Text = "$" + str(ClassSeat2)
		RN.Text = "$" + str(ClassSeat3)
		self._LostInTheSauce.Text = "$" + str(ClassSeat1 + ClassSeat2 + ClassSeat3)
		pass

	def Button2Click(self, sender, e):
		French = (self._French.Text)
		Fry = (self._Fry.Text)
		Curd = (self._Curd.Text)
		KT = self._ketchup.Text
		MT = self._mustard.Text
		RN = self._ranch.Text
		
		French = ""
		Fry = ""
		Curd = ""
		KT = ""
		MT = ""
		RN = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass