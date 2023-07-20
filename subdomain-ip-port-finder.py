import requests
import urllib.parse
import socket



domain = input("Taranacak Domaini Girin..:")   # Taranacak domaini alır
subdomainIp = ""
subdomainPort = ""
hedefIP=""


file = open("orneksublar.txt")   # Subdomain wordlistini okur


content = file.read()   # İçeriği alır


subdomainler = content.splitlines()  # Satırlar halinde kelimeleri alır


kesfedilen_subdomainler = []   # Keşfedilen subdomainlerin alınacağı liste


for subdomain in subdomainler:

    # Url oluşturma
    url = f"http://{subdomain}.{domain}"
    url2 = str(subdomain)+"."+str(domain)

    try:
        # Hata verirse subdomain yoktur.
        requests.get(url)
    except requests.ConnectionError:
        # Subdomain yoksa bir şey yapma
        pass
    else:
        # Subdomain varsa bunları yap
        print("[+]Subdomain bulundu-->", url)
        subdomainIp = socket.gethostbyname(url2)
        print("Subdomain IP-->",subdomainIp)
        hedefIP= (url2)
        ###sonliste = [url, subdomainIp]
        for port in range(70, 450):
    
            # İstemci yapılandırması
            client = socket.socket()
            client.settimeout(0.05)
            # Port açıksa yazdırır
            if client.connect_ex((hedefIP, port)) == 0:
                ###sonliste.append(port)
                print("Subdomain Port-->", port)
                
        # Keşfedilen subdomain,ip ve portu ekler
        kesfedilen_subdomainler.append(url)
        kesfedilen_subdomainler.append(subdomainIp)
        kesfedilen_subdomainler.append(port)
        ###print(sonliste)
        
# Keşfedilenleri dosyaya ekler
with open("kesfedilen_subdomainler.txt", "w") as f:
    for subdomain in kesfedilen_subdomainler:
        print(subdomain, file=f)
        
