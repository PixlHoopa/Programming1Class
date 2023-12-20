import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.CornflowerBlue
		self._button1.Font = System.Drawing.Font("MS Gothic", 10)
		self._button1.Location = System.Drawing.Point(12, 388)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(29, 29)
		self._button1.TabIndex = 0
		self._button1.Text = "Go"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("MS Gothic", 14)
		self._label1.Location = System.Drawing.Point(44, 24)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(862, 235)
		self._label1.TabIndex = 1
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self.ClientSize = System.Drawing.Size(949, 428)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog777CA"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "Thank you for all of your help with my college research and planning, Mr.Szelogowski!" \
		"\nIt has helped me immensely in preparing myself for college, but unfortunately, I must disappoint you." \
		"\nRather than using class time to work on programs, I have decided to write this code." \
		"\nOf course, I wouldn't do anything pointless in this class if it wasn't for a good reason." \
		"\nTherefore, I am proud to say that I have been admitted into UW-Whitewater and UW-Milwaukee!" \
		"\nI know that this program is nothing fancy, but I thought it would be fun to write." \
		"\nOnce again, thank you. :)"
		self._button1.Size = System.Drawing.Size(0,0)
		self.BackColor = System.Drawing.Color.MediumPurple
		pass