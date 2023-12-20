import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Honeydew
		self._button3.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(828, 296)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 39)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Honeydew
		self._button2.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(828, 178)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 39)
		self._button2.TabIndex = 6
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Honeydew
		self._button1.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(828, 61)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 39)
		self._button1.TabIndex = 5
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._listBox1.Font = System.Drawing.Font("Verdana", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 29
		self._listBox1.Location = System.Drawing.Point(34, 14)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(773, 410)
		self._listBox1.TabIndex = 4
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(937, 439)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog122b"
		self.ResumeLayout(False)
		
	def Button1Click(self, sender, e):
		heading = "Hours\t\tPay\tRate Of Pay is $4/h"
		self._listBox1.Items.Add(heading)
		for num in range(1,40 + 1):
			Money = num * 4
			msg = str(num) + "\t\t $" + str(Money)
			self._listBox1.Items.Add(msg)
		pass

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass
