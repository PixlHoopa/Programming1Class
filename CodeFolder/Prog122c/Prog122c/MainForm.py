import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Aquamarine
		self._button1.Font = System.Drawing.Font("Trebuchet MS", 15.75, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(760, 70)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(156, 50)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Aquamarine
		self._button2.Font = System.Drawing.Font("Trebuchet MS", 15.75, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(760, 209)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(156, 50)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Aquamarine
		self._button3.Font = System.Drawing.Font("Trebuchet MS", 15.75, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(760, 339)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(156, 50)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.LightCyan
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(713, 420)
		self._listBox1.TabIndex = 3
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MediumAquamarine
		self.ClientSize = System.Drawing.Size(952, 439)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog122c"
		self.ResumeLayout(False)

	def Button1Click(self, sender, e):
		heading = "Number\t\tAdd One\t\tTimes Two\t\tSquared"
		# 
		self._listBox1.Items.Add(heading)
		for num in range(1,50+1):
			numone = num + 1
			numbytwo = num * 2
			nsquared = num ** 2
			msg = str(num) +  \
			"\t\t" + str(numone) + \
			"\t\t" + str(numbytwo) + \
			"\t\t" + str(nsquared)
			self._listBox1.Items.Add(msg)
		pass
	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass