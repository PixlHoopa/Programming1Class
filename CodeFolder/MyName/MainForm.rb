require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.LightGoldenrodYellow
		@button1.Font = System::Drawing::Font.new("Javanese Text", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(75, 253)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(173, 104)
		@button1.TabIndex = 0
		@button1.Text = "Let's Go!"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.LightGoldenrodYellow
		@button2.Font = System::Drawing::Font.new("Javanese Text", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(548, 253)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(173, 104)
		@button2.TabIndex = 1
		@button2.Text = "We Rule!"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 36, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(186, 57)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(406, 113)
		@label1.TabIndex = 2
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.LightCyan
		self.ClientSize = System::Drawing::Size.new(824, 416)
		self.Controls.Add(@label1)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "MyName"
		self.ResumeLayout(false)
	end
		

	def Button1Click(sender, e)
		@label1.Text = "Go Cougars!"	
	end
	def Button2Click(sender, e)
		@label1.Text = "Craig Rules!"
	end
end

