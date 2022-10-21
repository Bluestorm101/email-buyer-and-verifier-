from distutils.log import INFO, info
import hotmailbox
from art import *
import requests
import json
import threading
import ctypes
import colorama
from colorama import Fore
import subprocess, requests, time, os




info = threading.Lock(); config = json.load(open("config.json")); thread_count = config["Threads"]; apikey = config["API_Key"];  type = config["type"]
class data: mails = 0; retry = 0

amount = 25


user = hotmailbox.User(apikey)

tprint("Bluestorm")
print("[1] Check Balance")
print("[2] Buy Email")
print("[3] Check Stock")
print("[4] Get Verfication Code")

input1 = int(input("Option:"))
if input1 == 1:
    userbalance = user.balance()
    print("Hotmailbox:" ,"$",userbalance)       
elif input1 == 2:
    print("This will help you buy all many emails quickly")
    input("Press Enter or any keys to start:")
    def buy_mails():
        while True:
                url = requests.get(f"https://api.hotmailbox.me/mail/buy?apikey={apikey}&mailcode={type}&quantity={amount}").json(); ctypes.windll.kernel32.SetConsoleTitleW(f"Mails Purcahsed {data.mails} | Retries {data.retry}")
                try:
                    for emailpass in url["Data"]["Emails"]:
                        email = emailpass["Email"]; password = emailpass["Password"]
                        with open("mails.txt", 'a') as f:
                            print(f"{Fore.BLUE}[!] Bought {type} Mail\n Data:{data.mails} - {email} | {password}"); info.acquire(); info.release(); data.mails+= 1; f.write(f"{email}|{password}\n")
                except KeyError as e: print(f"{data.retry} failed/ratelimited: {e}"); data.retry += 1; pass
    for x in range(thread_count): threading.Thread(target=buy_mails).start()
#credits to https://github.com/hokuine/email-buyer for this part 
elif input1 == 3:
    stock = hotmailbox.stock()
    print(stock['OUTLOOK']['Stock'],"outlook emails in stock")
elif input1 == 4:
    emailinput = input("Enter the email:")
    passwordinput = input("Enter the password:")
    
    verify = hotmailbox.Email(emailinput, passwordinput)
    print(verify.discord(),"Discord")
    print(verify.facebook(),"Facebook")
    print(verify.amazon(),"amazon")
    print(verify.twitter(),"twitter")       
else:
     exit()




       
















