import System.Drawing
import System.Windows.Forms
import System.Random
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.R = System.Random()
		self.ballup = 0
		self.balld = 0
		self.flagleft = False
		self.flagright = False
		self.BLUE = 0
		self.queerio = 0


	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._lbltitle = System.Windows.Forms.Label()
		self._leftscore = System.Windows.Forms.Label()
		self._rightscore = System.Windows.Forms.Label()
		self._lblright = System.Windows.Forms.Label()
		self._lblleft = System.Windows.Forms.Label()
		self._lblBall = System.Windows.Forms.Label()
		self._timerright = System.Windows.Forms.Timer(self._components)
		self._timerleft = System.Windows.Forms.Timer(self._components)
		self._timerball = System.Windows.Forms.Timer(self._components)
		self._timermulti = System.Windows.Forms.Timer(self._components)
		self._timerdummy = System.Windows.Forms.Timer(self._components)
		self._timerboolean = System.Windows.Forms.Timer(self._components)
		self.SuspendLayout()
		# 
		# lbltitle
		# 
		self._lbltitle.BackColor = System.Drawing.Color.Transparent
		self._lbltitle.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lbltitle.ForeColor = System.Drawing.Color.Snow
		self._lbltitle.Location = System.Drawing.Point(12, 25)
		self._lbltitle.Name = "lbltitle"
		self._lbltitle.Size = System.Drawing.Size(958, 52)
		self._lbltitle.TabIndex = 0
		self._lbltitle.Text = "Press Enter to Start or M to start Multiplayer"
		self._lbltitle.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# leftscore
		# 
		self._leftscore.BackColor = System.Drawing.Color.Transparent
		self._leftscore.Font = System.Drawing.Font("Courier New", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._leftscore.ForeColor = System.Drawing.Color.Snow
		self._leftscore.Location = System.Drawing.Point(39, 96)
		self._leftscore.Name = "leftscore"
		self._leftscore.Size = System.Drawing.Size(166, 69)
		self._leftscore.TabIndex = 1
		self._leftscore.Text = "0"
		self._leftscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# rightscore
		# 
		self._rightscore.BackColor = System.Drawing.Color.Transparent
		self._rightscore.Font = System.Drawing.Font("Courier New", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._rightscore.ForeColor = System.Drawing.Color.Snow
		self._rightscore.Location = System.Drawing.Point(771, 96)
		self._rightscore.Name = "rightscore"
		self._rightscore.Size = System.Drawing.Size(166, 69)
		self._rightscore.TabIndex = 2
		self._rightscore.Text = "0"
		self._rightscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# lblright
		# 
		self._lblright.BackColor = System.Drawing.Color.White
		self._lblright.Location = System.Drawing.Point(950, 246)
		self._lblright.Name = "lblright"
		self._lblright.Size = System.Drawing.Size(20, 100)
		self._lblright.TabIndex = 3
		# 
		# lblleft
		# 
		self._lblleft.BackColor = System.Drawing.Color.White
		self._lblleft.Location = System.Drawing.Point(12, 246)
		self._lblleft.Name = "lblleft"
		self._lblleft.Size = System.Drawing.Size(20, 100)
		self._lblleft.TabIndex = 4
		# 
		# lblBall
		# 
		self._lblBall.BackColor = System.Drawing.Color.White
		self._lblBall.Location = System.Drawing.Point(479, 304)
		self._lblBall.Name = "lblBall"
		self._lblBall.Size = System.Drawing.Size(20, 20)
		self._lblBall.TabIndex = 5
		self._lblBall.Click += self.lblBallClick
		# 
		# timerright
		# 
		self._timerright.Interval = 20
		self._timerright.Tick += self.TimerrightTick
		# 
		# timerleft
		# 
		self._timerleft.Interval = 20
		self._timerleft.Tick += self.TimerleftTick
		# 
		# timerball
		# 
		self._timerball.Interval = 20
		self._timerball.Tick += self.TimerballTick
		# 
		# timermulti
		# 
		self._timermulti.Interval = 20
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(988, 607)
		self.Controls.Add(self._lblBall)
		self.Controls.Add(self._lblleft)
		self.Controls.Add(self._lblright)
		self.Controls.Add(self._rightscore)
		self.Controls.Add(self._leftscore)
		self.Controls.Add(self._lbltitle)
		self.Name = "MainForm"
		self.Text = "Pong"
		self.Load += self.MainFormLoad
		self.SizeChanged += self.MainFormSizeChanged
		self.KeyDown += self.MainFormKeyDown
		self.ResumeLayout(False)

	def TimerballTick(self, sender, e):
		ball = self._lblBall
		leftPad = self._lblleft
		rightPad = self._lblright
		rscone = int(self._rightscore.Text)
		lscone = int(self._leftscore.Text)
		ball.Top += self.ballup
		ball.Left += 8 * self.balld
		Queer = self.queerio
		Rainbow = randrange(
		if Queer == 3:
			
		if ball.Right >= rightPad.Left and ball.Bottom >= rightPad.Top and ball.Top <= rightPad.Bottom:
			self.balld = -1
			self.ballup = self.R.Next(-4, 5)
		elif ball.Left <= leftPad.Right and ball.Bottom >= leftPad.Top and ball.Top <= leftPad.Bottom:
			self.balld = 1
			self.ballup = self.R.Next(-4, 5)
		
		if ball.Top <= 0:
			self.balld = -1
			ball.Top += 5 * self.balld
		if ball.Bottom >= self.Height:
			self.balld = 1
			ball.Top += 5 * -self.balld
		
		if ball.Location.X <= 0 or \
			(ball.Location.X < leftPad.Left + 20 and ball.Location.Y < leftPad.Top):
			rscone += 1
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self._rightscore.Text = str(rscone)
		if ball.Location.X >= self.Width or \
			(ball.Location.X > rightPad.Right - 20 and ball.Location.Y > rightPad.Top):
			lscone += 1
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self._leftscore.Text = str(lscone)			
		pass
		
		if lscone == 10: # Left win condition
			self._timerball.Enabled = False
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self.ballup = 0
			self.balld = 0
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Left Player Wins! Press R to Restart"
		if rscone == 10: # Right win condition
			self._timerball.Enabled = False
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self.ballup = 0
			self.balld = 0
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Right Player Wins! Press R to Restart"
		
			
		if ball.Top <= 10:
			self.ballup *= -1
		elif ball.Bottom >= self.Height:
			self.ballup *= -1
        
		if ball.Top <= self.Top:
			self.ballup = 1
		elif ball.Bottom >= self.Height - 40:
			self.ballup = -1
			
			# To do: AI
		if self._timerboolean.Enabled == True:
			if self.Width // 2 <= ball.Left:
				return
			if self.Width // 2 > ball.Left:
				if (ball.Left - leftPad.Right) < 0:
					Speed = 0
				elif (ball.Left - leftPad.Right) < (self.Width // 4):
					Speed = 3.5
				elif (ball.Left - leftPad.Right) < (self.Width // 3):
					Speed = 3
				elif (ball.Left - leftPad.Right) < (self.Width // 2):
					Speed = 2.5
				if leftPad.Top != ball.Top - 20:
					if leftPad.Top < ball.Top - 20:
							leftPad.Top += Speed
					if leftPad.Top > ball.Top - 20:
 						leftPad.Top -= Speed
#			leftPad.Top = ball.Top - 20
	
	def MainFormKeyDown(self, sender, e):
		tball = self._timerball
		tdum = self._timerdummy
		tbool = self._timerboolean
		tmulti = self._timermulti
		tleft = self._timerleft
		tright = self._timerright
		bl = self._lblBall
		lblf = self._lblleft
		lblrt = self._lblright
		BLUE = self.BLUE
		Queer = self.queerio
		def Deactivated():
			tball.Enabled = False
			tdum.Enabled = False
			tbool.Enabled = False
			tmulti.Enabled = False
			tright.Enabled = False
			tleft.Enabled = False
		def Activated():
			tball.Enabled = True
			tdum.Enabled = True
			tbool.Enabled = True
			tmulti.Enabled = True
			tright.Enabled = True
			tleft.Enabled = True		
		def reset():
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Press Enter to Start or M to start Multiplayer"
			self._leftscore.Text = "0"
			self._rightscore.Text = "0"
			Deactivated()
			bl.Left = self.Width // 2
			bl.Top = self.Height // 2
			lblf.Top = (self.Height // 2) - 100 + lblf.Height
			lblrt.Top = (self.Height // 2) - 100 + lblrt.Height
			bl.BackColor = Color.White
			self.BackColor = Color.Black
			lblf.BackColor = Color.White
			lblrt.BackColor = Color.White
			self.BLUE = 0
		#BLUE PADDLES
		if e.KeyCode == Keys.B:
			if BLUE == 0:
				self.BLUE = 1
			else:
				self.BLUE = 0
		if e.KeyCode == Keys.L:
			if BLUE == 1:
				self.BLUE = 2
			else:
				self.BLUE = 0
		if e.KeyCode == Keys.U:
			if BLUE == 2:
				self.BLUE = 3
			else:
				self.BLUE = 0
		if e.KeyCode == Keys.E:
			if BLUE == 3:
				self.BLUE = 4
			else:
				self.BLUE = 0
		# COLOR TIME
		if e.KeyCode == Keys.G:
			if Queer == 0:
				self.queerio = 1
			else:
				self.queerio = 0
		if e.KeyCode == Keys.A:
			if Queer == 1:
				self.queerio = 2
			else:
				self.queerio = 0
		if e.KeyCode == Keys.Y:
			if Queer == 2:
				self.queerio = 3
			else:
				self.queerio = 0
		# Abceervfh
		if e.KeyCode == Keys.R:
			reset()
		if e.KeyCode == Keys.Enter:
			if BLUE == 4:
				lblf.BackColor = Color.Blue
				lblrt.BackColor = Color.Blue
			tball.Enabled = True
			tdum.Enabled = True
			tbool.Enabled = True
			self._lbltitle.Visible = False
		if e.KeyCode == Keys.M and self._lbltitle.Visible == True:
			reset()
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Use W and S to move the left paddle; " \
								  "hit Enter to Begin"
			tmulti.Enabled = True
			if e.KeyCode == Keys.Enter:
				self._lbltitle.Visible = False
				tbool.Enabled = False
				tmulti.Enabled = True
				tdum.Enabled = False
				tball.Enabled = True
				
		if tdum.Enabled:
			if e.KeyCode == Keys.Up:
				self.flagright = False
				tright.Enabled = True
			elif e.KeyCode == Keys.Down:
				self.flagright = True
				tright.Enabled = True
			elif tright.Enabled and self.flagright == False:
				tright.Enabled = False
		
		"""finish multiplayer controls"""
		
		if tmulti.Enabled and tball.Enabled:
			if e.KeyCode == Keys.W:
				self.flagleft = False
				tleft.Enabled = True
			elif e.KeyCode == Keys.S:
				self.flagleft = True
				tleft.Enabled = True
			elif tright.Enabled and self.flagright == False:
				tright.Enabled = False
		if e.KeyCode == Keys.Escape:
			Application.Exit()
		pass

	def MainFormLoad(self, sender, e):
		""" TO DO: ADD 3 UNIQUE SECRETS/CHEATS/EASTER EGGS IN TOTAL
		AND FINISH MULTIPLAYER AND SCOREBOARD AND DUMMY AI"""
		self.balld = 1
		self.ballup = self.R.Next(-4, 5)
		self._timerball.Enabled = False
		self._timerdummy.Enabled = False
		self._timermulti.Enabled = False
		pass
	
	def pdlTick(self, pdl, flagd, tmr):
		if flagd == True:
			pdl.Top += 5
		if flagd == False:
			pdl.Top -= 5
		if pdl.Top <= 10:
			tmr.Enabled = False
		if pdl.Bottom >= self.Height - 50:
			tmr.Enabled = False

	def TimerleftTick(self, sender, e):
		self.pdlTick(self._lblleft, self.flagleft, self._timerleft)
		pass

	def TimerrightTick(self, sender, e):
		self.pdlTick(self._lblright, self.flagright, self._timerright)
		pass
	

	def lblBallClick(self, sender, e):
		self._lblBall.BackColor = Color.Red
		""" Put more eggs """
		self.BackColor = Color.Green
		
		pass

	def MainFormSizeChanged(self, sender, e):
		self._lblright.Left = self.Width - 25 - self._lblright.Width
		self._lblBall.Left = self.Width // 2
		self._lblBall.Top = self.Height // 2
		self._lbltitle.Width = self.Width - 25
		self._rightscore.Left = self.Width - 75 - self._rightscore.Width
	#	if self._lblright.Left <= 0:
	#		MessageBox = "Do you not want to play anymore..?"
	#		Application.Exit()
		
		pass
	
	
	
	
