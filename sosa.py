# D3v by black code
import requests 
import random,datetime,sys,threading

RED = '\033[91m'
WHITE = '\033[97m'
RESET = '\033[0m'

Z = '\033[1;31m'
X = '\033[1;33m' 
Z1 = '\033[2;31m'
F = '\033[2;32m' 
A = '\033[2;34m'
C = '\033[2;35m' 
B = '\033[2;36m'
Y = '\033[1;34m' 
W="\033[1;37m"

insta="1234567890qwertyuiopasdfghjklzxcvbnm"
all="_"

toolart = r"""
██████╗ ██╗      █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝ 
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ 
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                        
███╗   ██╗ █████╗ ███╗   ███╗███████╗   
████╗  ██║██╔══██╗████╗ ████║██╔════╝   
██╔██╗ ██║███████║██╔████╔██║█████╗     
██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝     
██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗   
╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ 
                                                                                                      Vsosa3"""

for line in toolart.split("\n"):
    print(F + line + RESET)
print(RED + "\nD3v by Black Code")
print("insta: 8vy_t / discord: rx9m \n" + RESET)

def main_menu():
    while True:
        print(f"\n{X}Choose mode:")
        print("1 - Telegram Bot")
        print("2 - Discord Webhook")
        print("3 - Print Only")
        print("4 - Credits")
        mode = input("➠ ")
        if mode in ["1","2","3","4"]:
            return mode
        else:
            print(Z + "Invalid choice, try again." + RESET)

mode = main_menu()
token, chat_id, webhook_url = None, None, None
save_print = False

if mode == "1":
    token=input(f"{X} ➠ Telegram Bot Token {C}")
    chat_id=input(f"{X} ➠ Telegram Chat ID {C}")
elif mode == "2":
    webhook_url=input(f"{X} ➠ Discord Webhook URL {C}")
elif mode == "3":
    save_choice = input(f"{X} Do you want to save usernames to file? (y/n): {C}")
    save_print = True if save_choice.lower() == "y" else False
elif mode == "4":
    input("made by black code / mohammed yassine  discord:rx9m / insta:8vy_t\nPress Enter to return to menu...")
    mode = main_menu()

def send_result(user):
    god=f"""instagram user✅
←•━━━━━━━━━━━━•→
 𝚄𝚂𝙴𝚁 ➠ {user}
←•━━━━━━━━━━━━•→
 𝐁𝐘 » black code"""
    if mode == "1":
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={god}')
    elif mode == "2":
        requests.post(webhook_url, json={"content": god})

def instaa(user):
    url = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/',
        headers ={
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
            'X-IG-App-ID':'936619743392459',
            'Content-Type':'application/x-www-form-urlencoded',
        },
        data=f'email=test@gmail.com&username={user}&first_name=&opt_into_one_tap=false')

    if '{"message":"feedback_required"' in url.text:
        print(W+f" [+] {Z} ErRoR UsEr : {X}{user} ")
    elif  '"errors": {"username":' in url.text or  '"code": "username_is_taken"' in url.text:
        print(W+f" [+] {Z} Bad user ➯ {X}{user} ")
    else:
        print(W+f" [+] {F} Good User ➯ {C}{user} ")
        if mode in ["1","2"]:
            send_result(user)
        elif mode == "3" and save_print:
            with open("good_users.txt","a") as f:
                f.write(user+"\n")

def users():
    while True:
        v1 = ''.join((random.choice(insta) for i in range(1)))
        v2 = ''.join((random.choice(insta) for i in range(1)))
        v3 = ''.join((random.choice(insta) for i in range(1)))
        v4 = ''.join((random.choice(insta) for i in range(1)))
        v5 = ''.join((random.choice(all) for i in range(1)))
        user1 = (v5+v1+v2+v3+v4)
        user2 = (v1+v5+v2+v3+v4)
        user3 = (v1+v2+v5+v3+v4)
        user4 = (v1+v2+v3+v5+v4)
        hamo010 = (user1, user2, user3, user4)
        user = random.choice(hamo010)
        instaa(user)

Threads=[] 
for t in range(7):
    x = threading.Thread(target=users)
    x.start()
    Threads.append(x)
for Th in Threads:
    Th.join()
users()

