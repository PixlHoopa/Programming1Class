import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.LightCoral
		self._listBox1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.ForestGreen
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 22
		self._listBox1.Location = System.Drawing.Point(12, 55)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(969, 290)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.IndianRed
		self._button1.Font = System.Drawing.Font("NSimSun", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.DarkGreen
		self._button1.Location = System.Drawing.Point(12, 383)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(177, 46)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.IndianRed
		self._textBox1.Location = System.Drawing.Point(428, 29)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 2
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.IndianRed
		self._button2.Font = System.Drawing.Font("NSimSun", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.DarkGreen
		self._button2.Location = System.Drawing.Point(376, 383)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(177, 46)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.IndianRed
		self._button3.Font = System.Drawing.Font("NSimSun", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.DarkGreen
		self._button3.Location = System.Drawing.Point(788, 383)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(177, 46)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Salmon
		self.ClientSize = System.Drawing.Size(993, 441)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog152b-REBOOT"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._listBox1.Items.Clear()
		heading = "Num:\t\tSum:"
		hangnail = 0
		CoolCat = 2
		self._listBox1.Items.Add(heading)
		if self._textBox1.Text == "":
			Cap = 0
		else:
			Cap = int(self._textBox1.Text)

		while (hangnail + CoolCat) <= Cap:
			hangnail = CoolCat + hangnail
			msg = str(CoolCat) + "\t\t" + str(hangnail)
			self._listBox1.Items.Add(msg)
			CoolCat = CoolCat + 2
		pass

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass