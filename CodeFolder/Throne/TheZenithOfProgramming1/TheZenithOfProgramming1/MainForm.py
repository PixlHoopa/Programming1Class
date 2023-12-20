import System.Drawing
import System.Windows.Forms
import pygame

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(404, 67)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "TEXT HERE"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ControlText
		self._label2.Location = System.Drawing.Point(12, 403)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(13, 13)
		self._label2.TabIndex = 1
		self._label2.Text = "label2"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(226, 132)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 2
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(999, 444)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "TheZenithOfProgramming1"
		self.ResumeLayout(False)

