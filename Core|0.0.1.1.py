#Made by Nuke#0362.
#Importing Kivy Library parts, dont scare
#Importing main kivy App, basics of all
from kivy.app import App
#Importing Widget Button, if you need describe please go to kivy.org/doc/stable/
from kivy.uix.button import Button
#Importing Widget objects
from kivy.uix.widget import Widget
#Importing Label, more at kivy.org, its display text
from kivy.uix.label import Label
#Importing BoxLayout, its simplier for me. So its good for this app:)
from kivy.uix.boxlayout import BoxLayout
#Clock for updating screen every second
from kivy.clock import Clock
#Making Main Class, you can redact only in it
class MyApp(App):
	#rods counter
	rods=0
	#temperature counter
	temperature=0
	#Building App
	def build(self):
		#Layouts
		BL=BoxLayout(orientation = "vertical",
		padding=[40])
		#GUI interface
		#Rods Label
		self.RodsLabel=Label(text="Rods:")
		BL.add_widget(self.RodsLabel)
		#Temperature Label
		self.temperatureLabel=Label(text="Temperature:")
		BL.add_widget(self.temperatureLabel)
		#First Button
		BL.add_widget(
		Button( text ="Rods +1%",
		on_release = self.rods_up_press, ))
		#Second Button
		BL.add_widget(
		Button( text ="Rods -1%", 
		on_release = self.rods_down_press, ))
		#Returning BoxLayout
		return BL
	#LOGIC part of programm
	#On Up press Function
	def rods_up_press(self,instance):
		#Checking Rods count, if it more than 100 not complete fuction.
		if MyApp.rods<100:
			#+1%
			MyApp.rods+=1
		#changing text of label
		self.RodsLabel.text="Rods: "+str(MyApp.rods)+"%"
		Clock.schedule_interval(self.update, 2)
	#On Down press Function
	def rods_down_press(self, instance):
		if MyApp.rods>0:
			MyApp.rods-=1
		self.RodsLabel.text="Rods: "+str(MyApp.rods)+"%"
	def update(self, dt):
		self.temperature=round(self.temperature+(self.rods)/15)
		self.temperatureLabel.text="Temperature:"+str(self.temperature)+"C"
if __name__ == "__main__":
	#And Finally run
	MyApp().run()
