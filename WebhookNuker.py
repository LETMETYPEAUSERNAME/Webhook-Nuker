from dhooks import Webhook
import time
print("WEBHOOK NUKER 1.0")

option = input("Would you like to delete the webhook (1) or raid it? (2) (ANSWER WITH 1 OR 2) ")
webhook = input("Enter Webhook URL: ")
object = Webhook(webhook)
if option == "1":
    object.send("Your webhook has been deleted by Webhook Raider on Github. https://github.com/LETMETYPEAUSERNAME/Eazy-Stealer")
    object.delete()

if option == "2":
    message = input("Enter message to be sent: ")
    delay = input("Enter delay to be used: ")
    num = float(delay)
    while True:
        object.send(message)
        time.sleep(num)
        




