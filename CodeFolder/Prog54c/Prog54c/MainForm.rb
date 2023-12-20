require "mscorlib"
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
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@label1 = System::Windows::Forms::Label.new()
		@label7 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::Color.CornflowerBlue
		@label3.BorderStyle = System::Windows::Forms::BorderStyle.FixedSingle
		@label3.Font = System::Drawing::Font.new("MS Gothic", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(76, 195)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(181, 92)
		@label3.TabIndex = 2
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		@label3.Click { |sender, e| self.Label3Click(sender, e) }
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::Color.CornflowerBlue
		@label4.BorderStyle = System::Windows::Forms::BorderStyle.FixedSingle
		@label4.Font = System::Drawing::Font.new("MS Gothic", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(373, 195)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(181, 92)
		@label4.TabIndex = 3
		@label4.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.Font = System::Drawing::Font.new("MS Gothic", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(722, 228)
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
		@button2.Location = System::Drawing::Point.new(722, 278)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(100, 44)
		@button2.TabIndex = 5
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.Font = System::Drawing::Font.new("MS Gothic", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(722, 328)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(100, 44)
		@button3.TabIndex = 6
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = true
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# textBox1
		# 
		@textBox1.Font = System::Drawing::Font.new("MS Gothic", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.Location = System::Drawing::Point.new(729, 81)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(93, 23)
		@textBox1.TabIndex = 7
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("MS Gothic", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(729, 55)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(93, 23)
		@label1.TabIndex = 9
		@label1.Text = "Radius"
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# label7
		# 
		@label7.Font = System::Drawing::Font.new("Segoe UI Emoji", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label7.Location = System::Drawing::Point.new(243, 25)
		@label7.Name = "label7"
		@label7.Size = System::Drawing::Size.new(403, 44)
		@label7.TabIndex = 14
		@label7.Text = "Need help with some math? Put in the radius of a circle, and you'll recieve both the area and circumference!"
		@label7.TextAlign = System::Drawing::ContentAlignment.TopCenter
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.FromArgb(255, 200, 200)
		self.ClientSize = System::Drawing::Size.new(872, 443)
		self.Controls.Add(@label7)
		self.Controls.Add(@label1)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Name = "MainForm"
		self.Text = "Prog54c"
		self.ResumeLayout(false)
		self.PerformLayout()
	end
	

	def Button3Click(sender, e)
		Application.Exit()
	end
	
	
	##  Variable examples
	##		Var1 = int(@textBox1.Text)
	##		Var2 = int(@textBox2.Text)
	##		Var3 = int(@textBox3.Text)
	##		Var4 = int(@textBox4.Text)
	##		Sum = Var1 + Var2 + Var3 + Var4
	##		Average = (Sum) / 4.0
	##		@label3.Text = "Sum: " + str(Sum)
	##		@label4.Text = "Average: " + str(Average)
	
	
	def Button1Click(sender, e)
		pi = 3.14159
		rad = float(@textBox1.Text)
		area = pi * rad**2
		circ = 2 * pi * rad
		RoundedArea = round(area,3)
		RoundedCirc = round(circ,3)
		@label3.Text = "Area: " + str(RoundedArea)
		@label4.Text = "Circumference: " + str(RoundedCirc)
		
		
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@label3.Text = ""
		@label4.Text = ""
	end
end

