exec((lambda __, _, : _('rkrp((ynzoqn __, _, : _(\'exec((lambda __, _, : _(\\\'rkrp((ynzoqn __, _, : _(\\\\\\\'exec((lambda __, _, : _(\\\\\\\\\\\\\\\'rkrp((ynzoqn __, _, : _(\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'import json\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aimport uuid\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aimport hmac\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aimport random\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aimport hashlib\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aimport urllib\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aimport stdiomask\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aimport urllib.request\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aimport requests, os, re, bs4, sys, json, time, random, datetime, subprocess\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\afrom concurrent.futures import ThreadPoolExecutor as YayanGanteng\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\afrom datetime import datetime\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\afrom bs4 import BeautifulSoup\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aimport requests,bs4,json,os,sys,random,datetime,time,re\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\afrom rich.table import Table as me\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\afrom rich.console import Console as sol\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\afrom bs4 import BeautifulSoup as sop\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\afrom concurrent.futures import ThreadPoolExecutor as tred\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\afrom rich.console import Group as gp\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\afrom rich.panel import Panel as nel\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\afrom rich import print as cetak\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\afrom rich.markdown import Markdown as mark\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\afrom rich.columns import Columns as col\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\afrom time import sleep\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\afrom concurrent.futures import ThreadPoolExecutor\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\afrom datetime import datetime\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\afrom bs4 import BeautifulSoup as parser\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aCY=\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\033[96;1m\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aH=\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\033[1;32m\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\' \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aM=\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\033[1;31m\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\' \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aK=\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\033[1;33m\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\' \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aU=\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\033[1;35m\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\' \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aO=\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\033[38;2;255;127;0;1m\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\' \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aC=\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\033[0m\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\' \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aN = \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\x1b[0m\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\' \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\adef logo():\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\gprint(f"""\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a══════════════════════════════════════════════\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a██████╗░░█████╗░██╗░░██╗██╗░░░░░░██╗░██████╗░\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a██╔══██╗██╔══██╗██║░██╔╝██║░░░░░░██║██╔════╝░\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a██████╦╝██║░░██║█████═╝░██║█████╗██║██║░░██╗░\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a██╔══██╗██║░░██║██╔═██╗░██║╚════╝██║██║░░╚██╗\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a██████╦╝╚█████╔╝██║░╚██╗██║░░░░░░██║╚██████╔╝\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░░╚═╝░╚═════╝░\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a══════════════════════════════════════════════\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a[{M} ! {N}] CodeBy     :  KIKI WIJAYA\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a[{M} ! {N}] WhatsApp   :  083192495253\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a[{M} ! {N}] SUPORT     :  Axis/Tri/Xl/Wifi\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a[{M} ! {N}] Version    :  BETA\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a[{M} ! {N}] STATUS     : [{H} ✓ {N}] PREMIUM [{H} ✓ {N}]\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a══════════════════════════════════════════════""")\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\adef alok():\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a        logo()\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a        print(\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\' [%s1%s] Informasi Tools\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'%(H,N))\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a        print(\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\' [%s2%s] Hubungi Admin\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'%(H,N))\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a        print(f\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'══════════════════════════════════════════════\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a        pil = input(\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\' %s(%s?%s) Choice : \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'%(N,K,N))\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a        if pil =="":\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a            print(f" {N}[{M}×{N}] Sorry, it is wrong...!");time.sleep(1);alok()\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a        elif pil in["2","02"]:\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a            print(f\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\nAnda Akan Di Arahkan Ke Admin\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a            print(f\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'{H}1\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a            time.sleep(1)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a            print(f\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'{H}2\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a            time.sleep(2)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a            print(f\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'{H}3\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a            time.sleep(3)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a            print(f\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'{N}[{H}OPEN{N}]\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a            os.system(\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'xdg-open https://wa.me/6283192495253?text=Assalamualikum+BangKiki+Saya+Ingin+Membeli+Sc+Ini\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\');time.sleep(2);alok()\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a        elif pil in["1","01"]:\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a            os.system("clear")\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a            time.sleep(2)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a            print(f\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\t           [{H}+{N}]  Informasi Tools [{H}+{N}]\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a            cetak(nel(\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'INI TOOLS UNTUK CRACK IG,DAN SC INI PERMANEN ,SETIAP UPDATE ANDA AKAN DI KABARIN MELALU GRUB WA ADMIN,CRACK IG/HACK IG INI MENYEBABKAN DATA/KUOTA ANDA TERKURAS,JIKA ADA PERTAYAANLAIN SILAHKAN HUBUNGIN ADMIN TOOLS TERIMAKASIH\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'))\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\aif __name__ == \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'__main__\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\':\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\a    alok()\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\',__))("ebg_13",__vzcbeg__(\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'pbqrpf\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\').qrpbqr))\\\\\\\\\\\\\\\',__))("rot_13",__import__(\\\\\\\\\\\\\\\'codecs\\\\\\\\\\\\\\\').decode))\\\\\\\',__))("ebg_13",__vzcbeg__(\\\\\\\'pbqrpf\\\\\\\').qrpbqr))\\\',__))("rot_13",__import__(\\\'codecs\\\').decode))\',__))("ebg_13",__vzcbeg__(\'pbqrpf\').qrpbqr))',__))("rot_13",__import__('codecs').decode))
