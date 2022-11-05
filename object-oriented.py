class Pod_Racer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  def repair(self):
      print("R2 ran some repairs")
      self.condition = "repaired"

class Anakins_Pod(Pod_Racer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)
  
  def jedi_boost(self):
    print("Boosted speed by 2")
    self.max_speed *= 2

  def get_race_status(self):
      print(f"Anankin's max speed is {self.max_speed} - his pod condition is {self.condition}")

class Sebulbas_Pod(Pod_Racer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)
  
  def flame_jet(self, other_pod):
    print("flamed another pod")
    other_pod.condition = "trashed"

anakins = Anakins_Pod(2500, "new", 50_000_000)
sebulbas = Sebulbas_Pod(3500, "refurbished", 25_000_000)   

anakins.get_race_status()
anakins.jedi_boost()
anakins.get_race_status()
sebulbas.flame_jet(anakins)
anakins.get_race_status()
anakins.repair()
anakins.get_race_status()


#How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
#Encapsulation - It keeps max speed, condition, etc in the base class and extended classes use those base class attributes.
#Abstraction - Abstracts away methods for indicating repair and setting intitial values.
#Inheritance - Each pod inherits the condition and other aspects of the pod parent.
#Polymorphism - You can call the repair method on any decendent of pod.

#Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# This is appropriate use of OOP because each pod is an individual that decends from a base class that has built in functionalituy.

#How in particular did Object Oriented Programming assist in the solving of this problem?
#See above - ussing OOP you can create many additional pods without recreating all the methods and properties of the first pod.