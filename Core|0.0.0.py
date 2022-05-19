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
#Making Main Class, you can redact only in it
class MyApp(App):
	#rods counter
	rods=0
	#Building App
	def build(self):
		#Layouts
		BL=BoxLayout(orientation = "vertical",
		padding=[40])
		#GUI interface
		#Label making...
		self.RodsLabel=Label(text="Rods are:")
		BL.add_widget(self.RodsLabel)
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
	#On Down press Function
	def rods_down_press(self, instance):
		if MyApp.rods>0:
			MyApp.rods-=1
		self.RodsLabel.text="Rods: "+str(MyApp.rods)+"%"
	pass
if __name__ == "__main__":
	#And Finally run
	MyApp().run()
