import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label2 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label2
		# 
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label2.Font = System.Drawing.Font("Yu Gothic", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ImageAlign = System.Drawing.ContentAlignment.TopLeft
		self._label2.Location = System.Drawing.Point(19, 93)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(925, 228)
		self._label2.TabIndex = 29
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.Color.Red
		self._label16.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label16.Location = System.Drawing.Point(921, 8)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(23, 23)
		self._label16.TabIndex = 28
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Orchid
		self._button3.Font = System.Drawing.Font("Palatino Linotype", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(671, 349)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(273, 77)
		self._button3.TabIndex = 27
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Orchid
		self._button2.Font = System.Drawing.Font("Palatino Linotype", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(339, 349)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(273, 77)
		self._button2.TabIndex = 26
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Orchid
		self._button1.Font = System.Drawing.Font("Palatino Linotype", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(19, 349)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(273, 77)
		self._button1.TabIndex = 25
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(383, 50)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(170, 31)
		self._textBox1.TabIndex = 24
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Lucida Handwriting", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(302, 23)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(332, 24)
		self._label1.TabIndex = 23
		self._label1.Text = "Input your Kilowatt Usage!"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightPink
		self.ClientSize = System.Drawing.Size(962, 435)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog93a"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		
		Kilow = int(self._textBox1.Text)
		Base = round(Kilow * 0.0475, 2)
		SurCh = round(Base * 0.10, 2)
		City = round(Base * 0.03, 2)
		Pay = Base + City + SurCh
		Late = (Base + SurCh + City) + (Base + SurCh + City) * 0.04
			
		self._label2.Text= "Base Rate:        " + str(Kilow) + " at a rate of $ 0.0475    = $ " + str(Base) + \
							"\n Surcharge:                                                   $ " + str(SurCh) + \
							"\n City Tax:                                                    $ " + str(City) + \
							"\n _______________________________________________________________" \
							"\n Payment Total:                                                 $ " + str(Pay) + \
							"\n\n Late Fee:                                                       $ " + str(round(Late, 2))
		
		self._label16.BackColor = System.Drawing.Color.Green
		
		
		if self._textBox1.Text == "":

			self._label16.BackColor = System.Drawing.Color.Yellow
			self._label2.Text = "Not enough Variables!"
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text= ""
		self._label2.Text= ""
		self._label16.BackColor = System.Drawing.Color.Red
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass