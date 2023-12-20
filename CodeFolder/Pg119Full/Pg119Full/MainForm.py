import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 226)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Show Name"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(151, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(121, 20)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(151, 70)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(121, 20)
		self._textBox2.TabIndex = 2
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(133, 17)
		self._label1.TabIndex = 3
		self._label1.Text = "Enter Your First Name:"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(12, 73)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(133, 17)
		self._label2.TabIndex = 4
		self._label2.Text = "Enter Your Last Name:"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(12, 140)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(128, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "This is your full name:"
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(151, 137)
		self._textBox3.Multiline = True
		self._textBox3.Name = "textBox3"
		self._textBox3.ReadOnly = True
		self._textBox3.Size = System.Drawing.Size(121, 26)
		self._textBox3.TabIndex = 6
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(129, 226)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear Text"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(249, 226)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit App"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(328, 254)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg119Full"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		FName = str(self._textBox1.Text)
		LName = str(self._textBox2.Text)
		self._textBox3.Text = FName + " " + LName
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass