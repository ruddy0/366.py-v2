import sys, os

if os.name == "nt":
    dizin = "C:/Windows/System32/drivers/etc/hosts"

elif os.name == "posix":
    dizin = "/etc/hosts"

def engelleyici():
    for i in sys.argv:
        if i == f0 or i == f1:
            pass
        else:
            with open(dizin, "a") as hosts:
                hosts.write("\n" + "127.0.0.1 " + i)
                hosts.close()

def engelKaldir():
        dosya = open(dizin, "r")
        hosts = dosya.readlines()
        dosya.close()
        for site in f2:
            if "." in site:
                for oku in hosts:
                    if site in oku:
                        hosts.remove(oku)
            else:
                print("Site uzantısını girmediniz.")

        dosya = open(dizin, "w")
        dosya.writelines(hosts)
        dosya.close()

def engellisite():
    dosya = open(dizin, "r")
    hosts = dosya.readlines()
    dosya.close()
    for oku in hosts:
        if ("127.0.0.1" in oku or "127.0.1.1" in oku) and "localhost" not in oku:
            oku = oku.split()[1]
            print(oku)

try:

        f0 = sys.argv[0]
        f1 = sys.argv[1]
        f2 = sys.argv[2:]

        if len(sys.argv) > 2:
            if f1 == "-k":
                engelleyici()
            elif f1 == "-a":
                engelKaldir()
            else:
                print("Hatalı giriş!")
        elif f1 =="-t" and len(sys.argv)== 2:
            print("\nEngelli Site Listesi:\n")
            engellisite()
        else:
            print("Hatalı Kullanım!")
            print("Kullanma rehberi için:\n"
                  "366.py yaz 'Enter' tuşuna bas.")
except:

    print("""
    Kullanım:
    Site Engelleme: 
        366.py -k engelleneceksite.com
    Site Engel Kaldırma: 
        366.py - a engellenmissite.com
    Engellenmiş Site Listesi: 
        366.py -t
    """)
