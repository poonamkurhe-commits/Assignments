# Task 10: Customized Notification Engine (Super Overriding)
# Create a base class Notification with a method send(message). Create a subclass
# SMSNotification that overrides send() but calls the base class send() method inside it using super()
# before adding an SMS-specific footer ("Sent via Carrier").
# EXAMPLE INPUT
# sms = SMSNotification()
# sms.send("OTP: 4532")
# EXPECTED OUTPUT
# Sending: OTP: 4532
# Sent via Carrier
class Notification:
    def send(self, message):
        print("Sending:", message)
class SMSNotification(Notification):
    def send(self, message):
        super().send(message)  
        print("Sent via Carrier")
sms = SMSNotification()
sms.send("OTP: 4532")
