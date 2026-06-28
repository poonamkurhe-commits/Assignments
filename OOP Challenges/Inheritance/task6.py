# Task 6: Smart Home Ecosystem (Single Inheritance)
# Create a base class Device with attributes brand and status (on/off). Create a derived class
# SmartLight that inherits from Device and adds an attribute brightness. Use super() in SmartLight
# to initialize base attributes.
# EXAMPLE INPUT
# light = SmartLight("Philips", 80)
# light.turn_on()
# print(light.brand, light.status, light.brightness)
# EXPECTED OUTPUT
# Philips ON 80
class Device:
    def __init__(self,brand):
        self.brand=brand
        self.status = "OFF"
    def turn_on(self):
        self.status = "ON"
    def turn_off(self):
        self.status = "OFF"
class SmartLight(Device):
    def __init__(self, brand, brightness):
        super().__init__(brand) 
        self.brightness = brightness
light = SmartLight("Philips", 80)
light.turn_on()
print(light.brand, light.status, light.brightness)