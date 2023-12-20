require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@button2 = System::Windows::Forms::Button.new()
		@button1 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.PapayaWhip
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 36, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(155, 77)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(406, 113)
		@label1.TabIndex = 6
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.LavenderBlush
		@button2.Font = System::Drawing::Font.new("Javanese Text", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(517, 273)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(173, 104)
		@button2.TabIndex = 5
		@button2.Text = "Not Me..."
		@button2.UseVisualStyleBackColor = false
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.LavenderBlush
		@button1.Font = System::Drawing::Font.new("Javanese Text", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(44, 273)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(173, 104)
		@button1.TabIndex = 4
		@button1.Text = "Click Me!"
		@button1.UseVisualStyleBackColor = false
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.BurlyWood
		self.ClientSize = System::Drawing::Size.new(745, 416)
		self.Controls.Add(@label1)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "About Me"
		self.ResumeLayout(false)
	end
		

	def Button1Click(sender, e)
		@label1.Text = "After living for 540,727,938 seconds, I can\n confidently declare that I am a\n hardworking slacker who enjoys messing\n around, as well as getting down to earth with\n focusing on one task at hand."	
	end
	def Button2Click(sender, e)
		@label1.Text = "So yes, that's me."
	end
end
