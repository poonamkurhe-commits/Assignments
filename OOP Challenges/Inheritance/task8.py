# Task 8: Vehicle Hybrid Model (Multiple Inheritance)
# Create a class Engine with a method engine_info() returning "Gasoline Engine". Create a class
# ElectricMotor with motor_info() returning "Electric Motor". Create a hybrid class HybridCar that
# inherits from both and provides a system overview.
# EXAMPLE INPUT
# car = HybridCar()
# print(car.get_power_source())
# EXPECTED OUTPUT
# This car runs on Gasoline Engine and Electric Motor.
class Engine:
    def engine_info(self):
        return "Gasoline Engine"
class ElectricMotor:
    def motor_info(self):
        return "Electric Motor"
class HybridCar(Engine,ElectricMotor):
    pass
    #def get_power_source(self):
    #    return f"This car runs on {self.engine_info()} and {self.motor_info()}."

car = HybridCar()
#print(car.get_power_source())
print("This car runs on", car.engine_info(), "and", car.motor_info() + ".")

        
