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
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Lucida Sans", 13)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(467, 44)
		self._label1.TabIndex = 0
		self._label1.Text = "Give me a number, and I'll give you the Factorial!"
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(123, 51)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(242, 20)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightSeaGreen
		self._label2.ForeColor = System.Drawing.Color.Azure
		self._label2.Location = System.Drawing.Point(12, 74)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(467, 173)
		self._label2.TabIndex = 2
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkCyan
		self._button1.ForeColor = System.Drawing.Color.Black
		self._button1.Location = System.Drawing.Point(12, 291)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(115, 115)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkCyan
		self._button2.ForeColor = System.Drawing.Color.Black
		self._button2.Location = System.Drawing.Point(182, 291)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(115, 115)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkCyan
		self._button3.ForeColor = System.Drawing.Color.Black
		self._button3.Location = System.Drawing.Point(364, 291)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(115, 115)
		self._button3.TabIndex = 5
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(489, 418)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog162a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Cheese = int(self._textBox1.Text)
		Pickle = 1
		Ketchup = 1
		while Pickle < Cheese:
			Pickle = Pickle + 1
			Ketchup = Pickle * Ketchup
		if Pickle == Cheese:
			self._label2.Text = str(Cheese) + "!  =  " + str(Ketchup)
		pass

	def Button2Click(self, sender, e):
		self._label2.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass