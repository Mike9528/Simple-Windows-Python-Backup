#!/usr/bin/env python3

import subprocess

def backup_data(src, dest):
    src = "C:\\Users\\Micha\\OneDrive\\Documents\\Google Automation\\TSandDebug"
    dest = "D:\\PyTrblSht_Backup"
    
    try:
        result = subprocess.run(["xcopy",src,dest,"/AC"], check=True, capture_output=True, text=True, shell=True)
        print(f"Backup successful: {src} -> {dest}")
        print('stdout:', result.stdout)
        print('stderr:', result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Backup failed for {src} -> {dest}: {e}")
        print('stdout:', e.stdout)
        print('stderr:', e.stderr)

if __name__ == "__main__":
    backup_data("C:\\Users\\Micha\\OneDrive\\Documents\\Google Automation\\TSandDebug", "D:\\PyTrblSht_Backup")
