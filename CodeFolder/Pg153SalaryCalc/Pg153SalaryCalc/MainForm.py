import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._txtAnnualSalary = System.Windows.Forms.TextBox()
		self._txtPayPeriods = System.Windows.Forms.TextBox()
		self._lblSalary = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._btnCalculate = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# txtAnnualSalary
		# 
		self._txtAnnualSalary.Location = System.Drawing.Point(165, 27)
		self._txtAnnualSalary.Name = "txtAnnualSalary"
		self._txtAnnualSalary.Size = System.Drawing.Size(125, 20)
		self._txtAnnualSalary.TabIndex = 0
		# 
		# txtPayPeriods
		# 
		self._txtPayPeriods.Location = System.Drawing.Point(165, 76)
		self._txtPayPeriods.Name = "txtPayPeriods"
		self._txtPayPeriods.Size = System.Drawing.Size(125, 20)
		self._txtPayPeriods.TabIndex = 1
		# 
		# lblSalary
		# 
		self._lblSalary.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._lblSalary.Location = System.Drawing.Point(165, 118)
		self._lblSalary.Name = "lblSalary"
		self._lblSalary.Size = System.Drawing.Size(125, 23)
		self._lblSalary.TabIndex = 2
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(73, 27)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(86, 20)
		self._label1.TabIndex = 3
		self._label1.Text = "Annual Salary:"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(34, 76)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(125, 20)
		self._label2.TabIndex = 4
		self._label2.Text = "Pay Periods Per Year:"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(34, 121)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(125, 20)
		self._label3.TabIndex = 5
		self._label3.Text = "Salary Per Pay Period:"
		# 
		# btnCalculate
		# 
		self._btnCalculate.BackColor = System.Drawing.Color.CornflowerBlue
		self._btnCalculate.ForeColor = System.Drawing.SystemColors.ControlText
		self._btnCalculate.Location = System.Drawing.Point(109, 174)
		self._btnCalculate.Name = "btnCalculate"
		self._btnCalculate.Size = System.Drawing.Size(86, 22)
		self._btnCalculate.TabIndex = 6
		self._btnCalculate.Text = "Calculate"
		self._btnCalculate.UseVisualStyleBackColor = False
		self._btnCalculate.Click += self.BtnCalculateClick
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlDark
		self.ClientSize = System.Drawing.Size(299, 208)
		self.Controls.Add(self._btnCalculate)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._lblSalary)
		self.Controls.Add(self._txtPayPeriods)
		self.Controls.Add(self._txtAnnualSalary)
		self.Name = "MainForm"
		self.Text = "Salary Calculation"
		self.ResumeLayout(False)
		self.PerformLayout()


	def BtnCalculateClick(self, sender, e):
		# Salary Calculation
		
		decAnnualSalary = 0.0 # Annual Salary
		intPayPeriods = 0 # number of pay periods per year
		decSalary = 0.0 # salary per pay period
		
		try:
			decAnnualSalary = float(self._txtAnnualSalary.Text)
			intPayPeriods = int(self._txtPayPeriods.Text)
		except:
			MessageBox.Show("The input files must contain nonzero numeric values.", "Error")
		if decAnnualSalary == 0.0 or intPayPeriods == 0:
			return
		decSalary = decAnnualSalary / intPayPeriods
		self._lblSalary.Text = "$" + str(round(decSalary, 2))
		pass