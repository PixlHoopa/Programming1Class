﻿require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@label1 = System::Windows::Forms::Label.new()
		@label5 = System::Windows::Forms::Label.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@label7 = System::Windows::Forms::Label.new()
		@label6 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# label2
		# 
		@label2.Font = System::Drawing::Font.new("MS Gothic", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(315, 93)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(93, 23)
		@label2.TabIndex = 1
		@label2.Text = "Variable 2"
		@label2.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		@label2.Click { |sender, e| self.Label2Click(sender, e) }
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::Color.CornflowerBlue
		@label3.BorderStyle = System::Windows::Forms::BorderStyle.FixedSingle
		@label3.Font = System::Drawing::Font.new("MS Gothic", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(65, 208)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(267, 127)
		@label3.TabIndex = 2
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		@label3.Click { |sender, e| self.Label3Click(sender, e) }
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::Color.CornflowerBlue
		@label4.BorderStyle = System::Windows::Forms::BorderStyle.FixedSingle
		@label4.Font = System::Drawing::Font.new("MS Gothic", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(519, 208)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(267, 127)
		@label4.TabIndex = 3
		@label4.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.Font = System::Drawing::Font.new("MS Gothic", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(144, 387)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(100, 44)
		@button1.TabIndex = 4
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.Font = System::Drawing::Font.new("MS Gothic", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(384, 387)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(86, 44)
		@button2.TabIndex = 5
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.Font = System::Drawing::Font.new("MS Gothic", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(629, 387)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(85, 44)
		@button3.TabIndex = 6
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = true
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# textBox1
		# 
		@textBox1.Font = System::Drawing::Font.new("MS Gothic", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.Location = System::Drawing::Point.new(163, 128)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(93, 23)
		@textBox1.TabIndex = 7
		# 
		# textBox2
		# 
		@textBox2.Font = System::Drawing::Font.new("MS Gothic", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox2.Location = System::Drawing::Point.new(315, 128)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(93, 23)
		@textBox2.TabIndex = 8
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("MS Gothic", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(163, 93)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(93, 23)
		@label1.TabIndex = 9
		@label1.Text = "Variable 1"
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		@label5.Font = System::Drawing::Font.new("MS Gothic", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label5.Location = System::Drawing::Point.new(467, 93)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(93, 23)
		@label5.TabIndex = 10
		@label5.Text = "Variable 3"
		@label5.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		@label5.Click { |sender, e| self.Label5Click(sender, e) }
		# 
		# textBox3
		# 
		@textBox3.Font = System::Drawing::Font.new("MS Gothic", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox3.Location = System::Drawing::Point.new(467, 128)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(93, 23)
		@textBox3.TabIndex = 12
		# 
		# label7
		# 
		@label7.Font = System::Drawing::Font.new("Segoe UI Emoji", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label7.Location = System::Drawing::Point.new(104, 23)
		@label7.Name = "label7"
		@label7.Size = System::Drawing::Size.new(662, 44)
		@label7.TabIndex = 14
		@label7.Text = "Need help with some math? Put in three whole numbers, and you'll recieve both the sum and the average!"
		@label7.TextAlign = System::Drawing::ContentAlignment.TopCenter
		# 
		# label6
		# 
		@label6.BackColor = System::Drawing::Color.FromArgb(192, 64, 0)
		@label6.BorderStyle = System::Windows::Forms::BorderStyle.Fixed3D
		@label6.Location = System::Drawing::Point.new(12, 417)
		@label6.Name = "label6"
		@label6.Size = System::Drawing::Size.new(16, 17)
		@label6.TabIndex = 15
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.FromArgb(255, 200, 200)
		self.ClientSize = System::Drawing::Size.new(872, 443)
		self.Controls.Add(@label6)
		self.Controls.Add(@label7)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@label5)
		self.Controls.Add(@label1)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Name = "MainForm"
		self.Text = "Prog58b"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button1Click(sender, e)
		Var1 = int(@textBox1.Text)
		Var2 = int(@textBox2.Text)
		Var3 = int(@textBox3.Text)
		Root1 = (-Var2 + $math.sqrt(Var2**2 - (4 * Var1 * Var3)))/(2 * Var1)
		Root2 = (-Var2 - $math.sqrt(Var2**2 - (4 * Var1 * Var3)))/(2 * Var1)
		@label3.Text = "Root One: " + str(Root1)
		@label4.Text = "Root Two: " + str(Root2)	
	end
	
	def Button2Click(sender, e)
		@textBox1.Text = ""
		@textBox2.Text = ""
		@textBox3.Text = ""
		@label3.Text = ""
		@label4.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()		
	end
	
	if @label6.BackColor = System::Drawing::Color.FromArgb(192, 64, 0) and @label3.Text = "Root One: " + str(Root1)
		then @label6.BackColor = System::Drawing::Color.FromArgb(0, 0, 0)
	end
	
	if @label6.BackColor = System::Drawing::Color.FromArbg(0, 0, 0,) and @label3.Text = ""
		then @label6.BackColor = System::Drawing::Color.FromArgb(192, 64, 0)
	end
end