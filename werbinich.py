#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("apt-get install tcpdumb")
os.system("clear")
os.system("figlet WER   BIN   ICH?")
print("""\033[1m 
----------------------------------------------------------------------------------------------
|                                   |                           |                            |
| \033[92mNmap Kısayolları                  \033[97m|  \033[92mWorldlist Kısayolları    \033[97m|  \033[92mBrute Force Kısayolları   \033[97m|            
|                                   \033[97m|                           |                            |
| \033[94m[\033[97m01\033[94m] Hizli Tarama                 \033[97m|  \033[94m[\033[97m05\033[94m] Cupp.py Başlatma    \033[97m|  \033[94m[\033[97m07\033[94m] İnstax Başlatma      \033[97m|   
| \033[94m[\033[97m02\033[94m] Servis Ve Versiyon Bilgisi   \033[97m|                           |                            |
| \033[94m[\033[97m03\033[94m] Isletım Sıstemı Bilgisi      \033[97m|  \033[92mFake Site Script         \033[97m|                            |
| \033[94m[\033[97m04\033[94m] Zenmap Başlat                \033[97m|                           \033[97m|                            |
|                                   |  \033[94m[\033[97m06\033[94m] Blackeye Başlatma   \033[97m|                            |
|                                   |                           |                            |
|                                   |                           |                            |  
---------------------------------------------------------------------------------------------- 
| \033[92mDDOS Attack Kısayolları           \033[97m|
\033[97m|                                   |
\033[97m| \033[94m[\033[97m08\033[94m] DDOS Saldırı Kontrolü        \033[97m| 
\033[97m|                                   | 
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
-------------------------------------


                                                       
""")

islemno = input("\033[37mIslem Numarası Giriniz: ")

if(islemno=="1"):
               hedefip = input("\033[37mHedef İp Girin: ")
               os.system("nmap " + hedefip)
elif(islemno=="2"):
               hedefip = input("\033[37mHedef İp Girin: ")
               os.system("nmap -sS -sV " + hedefip)
elif(islemno=="3"):
               hedefip = input("\033[37mHedef İp Girin: ")
               os.system("nmap -o " + hedefip)
elif(islemno=="4"):
               os.system("zenmap")
elif(islemno=="5"):
               os.system("python3 Tools/Cupp.py/cupp.py -i")
elif(islemno=="6"):
               os.system("bash Tools/Blackeye/blackeye.sh")
elif(islemno=="7"):
               os.system("bash Tools/İnstax/instax.sh")
elif(islemno=="8"):
               hedefip = input("\033[37mHedef İp Girin: ")
               os.system("tcpdump host " + hedefip)

else:
  print("\033[31mHatalı Secim Yaptın")


