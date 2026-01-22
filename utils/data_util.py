import time
import random

def generate_dynamic_email():
    """
    Menghasilkan email unik setiap detik.
    Contoh output: nitrooo_170589921@yopmail.com
    Kenapa pakai timestamp? Biar kalau kamu run script-nya 1000x, gak bakal ada yang kembar.
    """
    timestamp = int(time.time()) # Mengambil timestamp
    return f"automationtestqa{timestamp}@yopmail.com"

def generate_indonesia_phone():
    """
    Menghasilkan nomor HP Indonesia acak.
    Format: 08 + 9 digit angka acak.
    Contoh output: 08129384756
    """
    # Generate 9 digit angka random
    random_digits = random.randint(100000000, 999999999)
    return f"08{random_digits}"