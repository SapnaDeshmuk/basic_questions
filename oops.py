# class circle:
# 	global pi
# 	pi=3.14
# 	def area(self,r):
# 		return r*r*pi
# obj=circle()
# print (obj.area(7))

# class Employee:
# 	def __init__(self,name,id):
# 		self.id=id;
# 		self.name=name;
# 	def display(self):
# 		print ("id:%d\nName:%s"%(self.id,self.name))
# emp1=Employee("john",101)
# emp2=Employee("david",102)
# emp1.display()
# emp2.display()


class Animal:
	def speak(self):
		print "animal speaking"
class Dog(Animal):
	def bark(self):
		print ("dog barking")
class Cat(Animal,Dog):
	def voice(self):
		print ("maumau")
class bhoot(Animal,Dog,Cat):
	def action(self):
		print ("darana")

d=bhoot()
d.bark()
d.speak()
d.voice()
d.action()