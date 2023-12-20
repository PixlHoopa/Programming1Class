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
		self._label2 = System.Windows.Forms.Label()
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
		self._label17 = System.Windows.Forms.Label()
		self._label18 = System.Windows.Forms.Label()
		self._label19 = System.Windows.Forms.Label()
		self._label20 = System.Windows.Forms.Label()
		self._label21 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(327, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(305, 74)
		self._button1.TabIndex = 0
		self._button1.Text = "Party Time!"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(9, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(125, 125)
		self._label1.TabIndex = 1
		self._label1.Text = "label1"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(140, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(125, 125)
		self._label2.TabIndex = 2
		self._label2.Text = "label2"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.CornflowerBlue
		self._label3.Location = System.Drawing.Point(9, 259)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(125, 125)
		self._label3.TabIndex = 4
		self._label3.Text = "label3"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(9, 134)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(125, 125)
		self._label4.TabIndex = 3
		self._label4.Text = "label4"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(769, 259)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(125, 125)
		self._label5.TabIndex = 8
		self._label5.Text = "label5"
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(638, 134)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(125, 125)
		self._label6.TabIndex = 7
		self._label6.Text = "label6"
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(769, 134)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(125, 125)
		self._label7.TabIndex = 6
		self._label7.Text = "label7"
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(638, 259)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(125, 125)
		self._label8.TabIndex = 5
		self._label8.Text = "label8"
		# 
		# label9
		# 
		self._label9.Location = System.Drawing.Point(507, 259)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(125, 125)
		self._label9.TabIndex = 12
		self._label9.Text = "label9"
		# 
		# label10
		# 
		self._label10.Location = System.Drawing.Point(402, 259)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(125, 125)
		self._label10.TabIndex = 11
		self._label10.Text = "label10"
		# 
		# label11
		# 
		self._label11.Location = System.Drawing.Point(507, 134)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(125, 125)
		self._label11.TabIndex = 10
		self._label11.Text = "label11"
		# 
		# label12
		# 
		self._label12.Location = System.Drawing.Point(402, 134)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(125, 125)
		self._label12.TabIndex = 9
		self._label12.Text = "label12"
		# 
		# label13
		# 
		self._label13.Location = System.Drawing.Point(271, 259)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(125, 125)
		self._label13.TabIndex = 16
		self._label13.Text = "label13"
		# 
		# label14
		# 
		self._label14.Location = System.Drawing.Point(140, 259)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(125, 125)
		self._label14.TabIndex = 15
		self._label14.Text = "label14"
		# 
		# label15
		# 
		self._label15.Location = System.Drawing.Point(271, 134)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(125, 125)
		self._label15.TabIndex = 14
		self._label15.Text = "label15"
		# 
		# label16
		# 
		self._label16.Location = System.Drawing.Point(140, 134)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(125, 125)
		self._label16.TabIndex = 13
		self._label16.Text = "label16"
		# 
		# label17
		# 
		self._label17.Location = System.Drawing.Point(658, 9)
		self._label17.Name = "label17"
		self._label17.Size = System.Drawing.Size(125, 125)
		self._label17.TabIndex = 17
		self._label17.Text = "label17"
		# 
		# label18
		# 
		self._label18.Location = System.Drawing.Point(789, 9)
		self._label18.Name = "label18"
		self._label18.Size = System.Drawing.Size(125, 125)
		self._label18.TabIndex = 18
		self._label18.Text = "label18"
		# 
		# label19
		# 
		self._label19.Location = System.Drawing.Point(864, 259)
		self._label19.Name = "label19"
		self._label19.Size = System.Drawing.Size(125, 125)
		self._label19.TabIndex = 19
		self._label19.Text = "label19"
		# 
		# label20
		# 
		self._label20.Location = System.Drawing.Point(864, 116)
		self._label20.Name = "label20"
		self._label20.Size = System.Drawing.Size(125, 125)
		self._label20.TabIndex = 20
		self._label20.Text = "label20"
		# 
		# label21
		# 
		self._label21.Location = System.Drawing.Point(251, 9)
		self._label21.Name = "label21"
		self._label21.Size = System.Drawing.Size(125, 125)
		self._label21.TabIndex = 21
		self._label21.Text = "label21"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Coral
		self.ClientSize = System.Drawing.Size(1001, 439)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label21)
		self.Controls.Add(self._label20)
		self.Controls.Add(self._label19)
		self.Controls.Add(self._label18)
		self.Controls.Add(self._label17)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "ProgParty"
		self.ResumeLayout(False)



	def Button1Click(self, sender, e):
		Seconds = round(time.time())
		List = [System.Drawing.Color.CornflowerBlue, System.Drawing.Color.Azure, System.Drawing.Color.Cornsilk, System.Drawing.Color.DarkSalmon, System.Drawing.Color.HotPink]
		while Seconds == Seconds + 1:
			self._label3.BackColor = randint(List)
		pass