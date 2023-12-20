import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.Num1 = 0
		self.Num2 = 0
		self.Num3 = 0
		
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		resources = System.Resources.ResourceManager("SlotMachine.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._pictureBox2 = System.Windows.Forms.PictureBox()
		self._pictureBox3 = System.Windows.Forms.PictureBox()
		self._Lever = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._progressBar1 = System.Windows.Forms.ProgressBar()
		self._pictureBox4 = System.Windows.Forms.PictureBox()
		self._pictureBox5 = System.Windows.Forms.PictureBox()
		self._pictureBox6 = System.Windows.Forms.PictureBox()
		self._pictureBox7 = System.Windows.Forms.PictureBox()
		self._pictureBox8 = System.Windows.Forms.PictureBox()
		self._pictureBox9 = System.Windows.Forms.PictureBox()
		self._LeverOn = System.Windows.Forms.PictureBox()
		self._LeverOff = System.Windows.Forms.PictureBox()
		self._timer1 = System.Windows.Forms.Timer(self._components)
		self._pictureBox1.BeginInit()
		self._pictureBox2.BeginInit()
		self._pictureBox3.BeginInit()
		self._pictureBox4.BeginInit()
		self._pictureBox5.BeginInit()
		self._pictureBox6.BeginInit()
		self._pictureBox7.BeginInit()
		self._pictureBox8.BeginInit()
		self._pictureBox9.BeginInit()
		self._LeverOn.BeginInit()
		self._LeverOff.BeginInit()
		self.SuspendLayout()
		# 
		# pictureBox1
		# 
		self._pictureBox1.BackColor = System.Drawing.Color.White
		self._pictureBox1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox1.Location = System.Drawing.Point(12, 12)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(179, 229)
		self._pictureBox1.TabIndex = 0
		self._pictureBox1.TabStop = False
		# 
		# pictureBox2
		# 
		self._pictureBox2.BackColor = System.Drawing.Color.White
		self._pictureBox2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox2.Location = System.Drawing.Point(197, 12)
		self._pictureBox2.Name = "pictureBox2"
		self._pictureBox2.Size = System.Drawing.Size(187, 229)
		self._pictureBox2.TabIndex = 1
		self._pictureBox2.TabStop = False
		# 
		# pictureBox3
		# 
		self._pictureBox3.BackColor = System.Drawing.Color.White
		self._pictureBox3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox3.Location = System.Drawing.Point(390, 12)
		self._pictureBox3.Name = "pictureBox3"
		self._pictureBox3.Size = System.Drawing.Size(183, 229)
		self._pictureBox3.TabIndex = 2
		self._pictureBox3.TabStop = False
		# 
		# Lever
		# 
		self._Lever.BackgroundImage = resources.GetObject("Lever.BackgroundImage")
		self._Lever.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._Lever.Location = System.Drawing.Point(579, 11)
		self._Lever.Name = "Lever"
		self._Lever.Size = System.Drawing.Size(244, 288)
		self._Lever.TabIndex = 3
		self._Lever.UseVisualStyleBackColor = True
		self._Lever.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(639, 305)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(141, 30)
		self._button2.TabIndex = 4
		self._button2.Text = "Pickpocket"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(579, 338)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(76, 23)
		self._label1.TabIndex = 5
		self._label1.Text = "Bet:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(661, 341)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(109, 20)
		self._textBox1.TabIndex = 6
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(579, 370)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(76, 35)
		self._label2.TabIndex = 7
		self._label2.Text = "Cash:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(661, 370)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(162, 35)
		self._label3.TabIndex = 8
		self._label3.Text = "100"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# progressBar1
		# 
		self._progressBar1.Location = System.Drawing.Point(579, 408)
		self._progressBar1.Maximum = 15000
		self._progressBar1.Name = "progressBar1"
		self._progressBar1.Size = System.Drawing.Size(244, 22)
		self._progressBar1.TabIndex = 9
		# 
		# pictureBox4
		# 
		self._pictureBox4.BackColor = System.Drawing.Color.White
		self._pictureBox4.BackgroundImage = resources.GetObject("pictureBox4.BackgroundImage")
		self._pictureBox4.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom
		self._pictureBox4.Image = resources.GetObject("pictureBox4.Image")
		self._pictureBox4.Location = System.Drawing.Point(12, 247)
		self._pictureBox4.Name = "pictureBox4"
		self._pictureBox4.Size = System.Drawing.Size(561, 183)
		self._pictureBox4.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage
		self._pictureBox4.TabIndex = 10
		self._pictureBox4.TabStop = False
		self._pictureBox4.Visible = False
		# 
		# pictureBox5
		# 
		self._pictureBox5.BackColor = System.Drawing.Color.White
		self._pictureBox5.BackgroundImage = resources.GetObject("pictureBox5.BackgroundImage")
		self._pictureBox5.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox5.Location = System.Drawing.Point(26, 258)
		self._pictureBox5.Name = "pictureBox5"
		self._pictureBox5.Size = System.Drawing.Size(53, 50)
		self._pictureBox5.TabIndex = 11
		self._pictureBox5.TabStop = False
		self._pictureBox5.Visible = False
		# 
		# pictureBox6
		# 
		self._pictureBox6.BackColor = System.Drawing.Color.White
		self._pictureBox6.BackgroundImage = resources.GetObject("pictureBox6.BackgroundImage")
		self._pictureBox6.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox6.Location = System.Drawing.Point(79, 258)
		self._pictureBox6.Name = "pictureBox6"
		self._pictureBox6.Size = System.Drawing.Size(53, 50)
		self._pictureBox6.TabIndex = 12
		self._pictureBox6.TabStop = False
		self._pictureBox6.Visible = False
		# 
		# pictureBox7
		# 
		self._pictureBox7.BackColor = System.Drawing.Color.White
		self._pictureBox7.BackgroundImage = resources.GetObject("pictureBox7.BackgroundImage")
		self._pictureBox7.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox7.Location = System.Drawing.Point(132, 258)
		self._pictureBox7.Name = "pictureBox7"
		self._pictureBox7.Size = System.Drawing.Size(53, 50)
		self._pictureBox7.TabIndex = 13
		self._pictureBox7.TabStop = False
		self._pictureBox7.Visible = False
		# 
		# pictureBox8
		# 
		self._pictureBox8.BackColor = System.Drawing.Color.White
		self._pictureBox8.BackgroundImage = resources.GetObject("pictureBox8.BackgroundImage")
		self._pictureBox8.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox8.Location = System.Drawing.Point(185, 258)
		self._pictureBox8.Name = "pictureBox8"
		self._pictureBox8.Size = System.Drawing.Size(53, 50)
		self._pictureBox8.TabIndex = 14
		self._pictureBox8.TabStop = False
		self._pictureBox8.Visible = False
		# 
		# pictureBox9
		# 
		self._pictureBox9.BackColor = System.Drawing.Color.White
		self._pictureBox9.BackgroundImage = resources.GetObject("pictureBox9.BackgroundImage")
		self._pictureBox9.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox9.Location = System.Drawing.Point(238, 258)
		self._pictureBox9.Name = "pictureBox9"
		self._pictureBox9.Size = System.Drawing.Size(53, 50)
		self._pictureBox9.TabIndex = 15
		self._pictureBox9.TabStop = False
		self._pictureBox9.Visible = False
		# 
		# LeverOn
		# 
		self._LeverOn.BackgroundImage = resources.GetObject("LeverOn.BackgroundImage")
		self._LeverOn.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._LeverOn.Location = System.Drawing.Point(26, 370)
		self._LeverOn.Name = "LeverOn"
		self._LeverOn.Size = System.Drawing.Size(53, 50)
		self._LeverOn.TabIndex = 16
		self._LeverOn.TabStop = False
		self._LeverOn.Visible = False
		# 
		# LeverOff
		# 
		self._LeverOff.BackgroundImage = resources.GetObject("LeverOff.BackgroundImage")
		self._LeverOff.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._LeverOff.Location = System.Drawing.Point(79, 370)
		self._LeverOff.Name = "LeverOff"
		self._LeverOff.Size = System.Drawing.Size(53, 50)
		self._LeverOff.TabIndex = 17
		self._LeverOff.TabStop = False
		self._LeverOff.Visible = False
		# 
		# timer1
		# 
		self._timer1.Tick += self.Timer1Tick
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(831, 442)
		self.Controls.Add(self._LeverOff)
		self.Controls.Add(self._LeverOn)
		self.Controls.Add(self._pictureBox9)
		self.Controls.Add(self._pictureBox8)
		self.Controls.Add(self._pictureBox7)
		self.Controls.Add(self._pictureBox6)
		self.Controls.Add(self._pictureBox5)
		self.Controls.Add(self._pictureBox4)
		self.Controls.Add(self._progressBar1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._Lever)
		self.Controls.Add(self._pictureBox3)
		self.Controls.Add(self._pictureBox2)
		self.Controls.Add(self._pictureBox1)
		self.Name = "MainForm"
		self.Text = "SlotMachine"
		self._pictureBox1.EndInit()
		self._pictureBox2.EndInit()
		self._pictureBox3.EndInit()
		self._pictureBox4.EndInit()
		self._pictureBox5.EndInit()
		self._pictureBox6.EndInit()
		self._pictureBox7.EndInit()
		self._pictureBox8.EndInit()
		self._pictureBox9.EndInit()
		self._LeverOn.EndInit()
		self._LeverOff.EndInit()
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		rnd = System.Random()
		money = rnd.Next(1,51)
		if money > 25:
			MessageBox.Show("You failed to steal money!")
		else:
			cmoney = float(self._label3.Text)
			self._label3.Text = str(round(cmoney + money, 2))
		pass

	def Button1Click(self, sender, e):
		im1 = self._pictureBox5.BackgroundImage
		im2 = self._pictureBox6.BackgroundImage
		im3 = self._pictureBox7.BackgroundImage
		im4 = self._pictureBox8.BackgroundImage
		im5 = self._pictureBox9.BackgroundImage
		levOff = self._LeverOff.BackgroundImage
		levOn = self._LeverOn.BackgroundImage
		rnd = System.Random()
		num1 = 0
		num2 = 0
		num3 = 0
		#copy these into timerTick
		if self._textBox1.Text == "":
			MessageBox.Show("You must enter an amount to bet first!")
			return
		money = float(self._label3.Text)
		bet = float(self._textBox1.Text)
		money2 = money - bet
		
		if money == 0:
			MessageBox.Show("You have no money!")
		elif bet < 1:
			MessageBox.Show("You must bet at least one dollar!")
		elif bet > money and bet > money2:
			MessageBox.Show("You must have enough money to bet that!")
		else:
			self._Lever.BackgroundImage = levOn
			self._pictureBox4.Visible = True
			self._timer1.Enabled = True
			self._label3.Text = str(round(money2, 2))
			self._progressBar1.Value = 0
			num1 = self.Num1
			num2 = self.Num2
			num3 = self.Num3
			
			if num1 == 1 and num2 == 1 and num3 == 1:
				money2 += bet * 2
			if num1 == 2 and num2 == 2 and num3 == 2:
				money2 += bet * 2
			if num1 == 3 and num2 == 3 and num3 == 3:
				money2 += bet * 3
			if num1 == 4 and num2 == 4 and num3 == 4:
				money2 += bet * 4
			if num1 == 5 and num2 == 5 and num3 == 5:
				money2 += bet * 5
			if num1 < num2 and num2 < num3 and num3 == 5:
				money2 += bet * 1.5
			
			self.Num1 = 0
			self.Num2 = 0
			self.Num3 = 0
			self._label3.Text = str(round(money2, 2))
			
			if money2 <= 0:
				MessageBox.Show("You ran out of cash!")
		pass

	def Timer1Tick(self, sender, e):
		im1 = self._pictureBox5.BackgroundImage
		im2 = self._pictureBox6.BackgroundImage
		im3 = self._pictureBox7.BackgroundImage
		im4 = self._pictureBox8.BackgroundImage
		im5 = self._pictureBox9.BackgroundImage
		levOff = self._LeverOff.BackgroundImage
		levOn = self._LeverOn.BackgroundImage
		rnd = System.Random()
		num1 = 0
		num2 = 0
		num3 = 0
		
		pb1 = self._pictureBox1
		pb2 = self._pictureBox2
		pb3 = self._pictureBox3
		
		for lcv in range(0, 1000):
			num1 = rnd.Next(1, 6)
			num2 = rnd.Next(1, 6)
			num3 = rnd.Next(1, 6)
			
			self.Num1 = num1
			self.Num2 = num2
			self.Num3 = num3
			# copy and paste this for num2/pb2 and num3/pb3
			if num1 == 1:
				pb1.BackgroundImage = im1
			elif num1 == 2:
				pb1.BackgroundImage = im2
			elif num1 == 3:
				pb1.BackgroundImage = im3
			elif num1 == 4:
				pb1.BackgroundImage = im4
			elif num1 == 5:
				pb1.BackgroundImage = im5
				# num one cut off
			if num2 == 1:
				pb2.BackgroundImage = im1
			elif num2 == 2:
				pb2.BackgroundImage = im2
			elif num2 == 3:
				pb2.BackgroundImage = im3
			elif num2 == 4:
				pb2.BackgroundImage = im4
			elif num2 == 5:
				pb2.BackgroundImage = im5
				# num 2 cut off
			if num3 == 1:
				pb3.BackgroundImage = im1
			elif num3 == 2:
				pb3.BackgroundImage = im2
			elif num3 == 3:
				pb3.BackgroundImage = im3
			elif num3 == 4:
				pb3.BackgroundImage = im4
			elif num3 == 5:
				pb3.BackgroundImage = im5
				# num 3 cut off
			
			self._progressBar1.Increment(1)
			if self._progressBar1.Value == self._progressBar1.Maximum:
				self._timer1.Enabled = False
				self._pictureBox4.Visible = False
				self._Lever.BackgroundImage = levOff
		pass