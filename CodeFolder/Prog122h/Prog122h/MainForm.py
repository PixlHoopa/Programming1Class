import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Moccasin
		self._button1.Font = System.Drawing.Font("Lucida Fax", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 380)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(172, 41)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.SandyBrown
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(12, 6)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(924, 368)
		self._listBox1.TabIndex = 1
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Moccasin
		self._button2.Font = System.Drawing.Font("Lucida Fax", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(360, 380)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(172, 41)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Moccasin
		self._button3.Font = System.Drawing.Font("Lucida Fax", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(764, 380)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(172, 41)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.NavajoWhite
		self.ClientSize = System.Drawing.Size(948, 433)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog122h"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		supertext = "Number\t\t\tSquare\t\t\tSquare Root\t\t\tCube\t\t\t4th Root"
		self._listBox1.Items.Add(supertext)
		for num in range(1, 20+1, 1):
			Square = num ** 2
			Root = math.sqrt(num)
			# ADDED FUNCTION IF STATEMENT IS FOR EXTRA TABS
			Tab = "\t\t\t"
			if (Root - Root//1) > 0:
				Tab = "\t\t\t"
			else:
				Tab = "\t\t\t\t"
			Cube = num ** 3
			FouRoot = math.sqrt(math.sqrt(num))
			Numbers = str(num) + "\t\t\t" + str(Square) + "\t\t\t" + str(Root) \
			+ str(Tab) + str(Cube) + "\t\t\t" + str(FouRoot)
			self._listBox1.Items.Add(Numbers) 
		pass

	def Button2Click(self, sender, e):
		blank = ""
		self._listBox1.Items.Clear()
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass