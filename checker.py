import os
from colorama import Fore, Back, Style

print(Fore.WHITE+"Welome to VULPW - a password vulnerability checker")
print(Fore.MAGENTA+'''
|       | |      | |        /=======| |       |       |
 |     |  |      | |        |       |  |     | |     |
  |   |   |      | |        |_______/   |   |   |   |
   | |    |      | |        |            | |     | |
    |     \______/ \_______ |             |       |
-by Kushwanth
''')
print("Choose your Option")
print(Fore.BLUE + Style.BRIGHT + "1.Password check\n2.Username check\n3.WiFi check\n4.Leaked Database check")
option = int(input(Fore.RED+"Your Option: "))
if option == 1:
   name = str(input(Fore.GREEN+Style.DIM+"Enter the password: "))
   pwd = open('password.txt')
   for line in pwd.read().rsplit():
       if name == line:
          print(Fore.CYAN + Style.BRIGHT+ "Your Password "+name+" is Vulnerble")
          break
   print("If the Checker doesn't spot any weakness then your Password is safe (or) its yet to get updated in our wordlist")

if option == 2:
   name = str(input(Fore.GREEN+"Enter the username: "))
   user = open('usernames.txt')
   for line in user.read().rsplit():
       if name == line:
           print(Fore.CYAN + Style.BRIGHT+ "Your username "+name+" is Vulnerble")
           break
   print("If the Checker doesn't spot any weakness then your Password is safe (or) its yet to get updated in our wordlist")

if option == 3:
   name = str(input(Fore.GREEN+"Enter the password: "))
   wifi = open('wifipwd.txt')
   for line in wifi.read().rsplit():
       if name == line:
           print(Fore.CYAN + Style.BRIGHT+ "Your WiFi password "+name+" is Vulnerble")
           break
   print("If the Checker doesn't spot any weakness then your Password is safe (or) its yet to get updated in our wordlist")

leak = {1:'000webhost.txt',
2:'adobe100.txt',
3:'alleged-gmail-passwords.txt',
4:'Ashley-Madision.txt',
5:'bible.txt',
6:'carders.cc.txt',
7:'elitehacker.txt',
8:'faithwriters.txt',
9:'hak5.txt',
10:'honeynet.txt',
11:'hotmail.txt',
12:'izmy.txt',
13:'Lizard-Squad.txt',
14:'md5decryptot-uk.txt',
15:'muslimMatch.txt',
16:'myspace.txt',
17:'phpbb.txt',
18:'porn-unknown.txt',
19:'rockyou.txt',
20:'singles.txt',
21:'tuscl.txt',
22:'youporn2012.txt'}

if option == 4:
   for k,v in leak.items():
       print(Fore.CYAN+Style.BRIGHT,k,""+v)
   dboption = int(input("choose your database: "))
   dbname = leak[dboption]
   name = str(input(Fore.GREEN+"Enter the password: "))
   dbpwd = open("Leaked-Databases/"+dbname)
   for line in dbpwd.read().rsplit():
       if name == line:
           print(Fore.CYAN + Style.BRIGHT+ "Your password "+name+" has been Leaked")
       break
   print("If the Checker doesn't spot any weakness then your Password is safe (or) its yet to get updated in our wordlist")

print(Style.RESET_ALL+"Thank You for Using")
