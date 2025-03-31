import time
import itertools
import pyfiglet
from termcolor import colored
ascii_art = pyfiglet.figlet_format("En Gelişmiş Dirb Serverine Hoş Geldiniz")
print(ascii_art)
site = input(colored("Dirb Aracını kullanacağınız Site Linki: ", "blue"))
time.sleep(2)
print(colored("[+]Bağlantı kuruluyor..", "green"))
time.sleep(2)
print(colored("[+] Güvenlik duvarı aşılıyor..", "green"))
time.sleep(3)
print(colored("[-]Güvenlik duvarı aşılamadı! Tekrar deneniyor..", "red"))
time.sleep(2)
print(colored("[+]Sahte ıp adresi etkinleştiriliyor: 79.189.110.192", "green"))
time.sleep(3)
print(colored("[+]İşlem başari ile tamamlandı! Veriler çekiliyor..", "green"))

with open("database.txt", "w") as file:
    file.write(f"{site} Veri tabanları aşağıda verildi.")
    file.write(f"{site} Güvenlik duvarı erişim engellendi!")

    print(f"{site} Veri tabanı database.txt olarak oluşturuldu.")