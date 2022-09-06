import json
import uuid
import hmac
import random
import hashlib
import urllib
import stdiomask
import urllib.request
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
import requests,bs4,json,os,sys,random,datetime,time,re
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
CY='\033[96;1m'
H='\033[1;32m' 
M='\033[1;31m' 
K='\033[1;33m' 
U='\033[1;35m' 
O='\033[38;2;255;127;0;1m' 
C='\033[0m' 
N = '\x1b[0m' 
def logo():
	print(f"""
══════════════════════════════════════════════
██████╗░░█████╗░██╗░░██╗██╗░░░░░░██╗░██████╗░
██╔══██╗██╔══██╗██║░██╔╝██║░░░░░░██║██╔════╝░
██████╦╝██║░░██║█████═╝░██║█████╗██║██║░░██╗░
██╔══██╗██║░░██║██╔═██╗░██║╚════╝██║██║░░╚██╗
██████╦╝╚█████╔╝██║░╚██╗██║░░░░░░██║╚██████╔╝
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░░╚═╝░╚═════╝░
══════════════════════════════════════════════
[{M} ! {N}] CodeBy     :  KIKI WIJAYA
[{M} ! {N}] WhatsApp   :  083192495253
[{M} ! {N}] SUPORT     :  Axis/Tri/Xl/Wifi
[{M} ! {N}] Version    :  BETA
[{M} ! {N}] STATUS     : [{H} ✓ {N}] PREMIUM [{H} ✓ {N}]
══════════════════════════════════════════════""")
def alok():
        logo()
        print(' [%s1%s] Informasi Tools'%(H,N))
        print(' [%s2%s] Hubungi Admin'%(H,N))
        print(f'══════════════════════════════════════════════')
        pil = input(' %s(%s?%s) Choice : '%(N,K,N))
        if pil =="":
            print(f" {N}[{M}×{N}] Sorry, it is wrong...!");time.sleep(1);alok()
        elif pil in["2","02"]:
            print(f'\nAnda Akan Di Arahkan Ke Admin')
            print(f'{H}1')
            time.sleep(1)
            print(f'{H}2')
            time.sleep(2)
            print(f'{H}3')
            time.sleep(3)
            print(f'{N}[{H}OPEN{N}]')
            os.system('xdg-open https://wa.me/6283192495253?text=Assalamualikum+BangKiki+Saya+Ingin+Membeli+Sc+Ini');time.sleep(2);alok()
        elif pil in["1","01"]:
            os.system("clear")
            time.sleep(2)
            print(f'\t           [{H}+{N}]  Informasi Tools [{H}+{N}]')
            cetak(nel('INI TOOLS UNTUK CRACK IG,DAN SC INI PERMANEN ,SETIAP UPDATE ANDA AKAN DI KABARIN MELALU GRUB WA ADMIN,CRACK IG/HACK IG INI MENYEBABKAN DATA/KUOTA ANDA TERKURAS,JIKA ADA PERTAYAANLAIN SILAHKAN HUBUNGIN ADMIN TOOLS TERIMAKASIH'))

if __name__ == '__main__':
    alok()