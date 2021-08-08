# Bir kullanıcı oluştur (kodlar arasında kullanıcıyı oluştur) ve bu kullanıcının şifresi olsun
# şifreyi 3 kere yanlış girerse uyarı versin ve belirli bir süre boyunca hesap bloke edilsin
# kullanıcı adını da 3 kere yanlış girerse uyarı versin ve belirli bir süre boyunca hesap bloke edilsin
# kullanıcı doğru girene kadar döngü devam etsin; doğru girerse olumlu yanıt verilsin.

import time # şifre 3 kere yanlış girilince belirli bir süre için bloke etmek için

username = "yigituygun8" # ben belirledim
password = "ilovecoding88!" # ben belirledim
passtry = 0
tekrar_kullaniciadi = "Kullanıcı Adınızı Tekrar Giriniz: "
tekrar_sifre = "Şifrenizi Tekrar Giriniz: "       

def try_again(login, loginpassword):
    login = str(input("Kullanıcı Adınızı Giriniz: "))
    time.sleep(0.5)
    loginpassword = str(input("Şifrenizi Giriniz: "))
    
    if login == username and loginpassword == password:
        print("Kontrol Ediliyor...")
        time.sleep(2)
        print("Başarılı Bir Şekilde Giriş Yapıldı")   
    elif loginpassword == password:
        print("Kontrol Ediliyor...")
        time.sleep(2)
        print("Kullanıcı Adınızı Yanlış Girdiniz!")
        passtry = 1
        for n in range(2):
            passtry += 1
            again1 = str(input("Kullanıcı Adınızı Tekrar Giriniz:"))
            if again1 == username:
                print("Başarılı Bir Şekilde Giriş Yapıldı")
            elif passtry == 3:
                print("Hesabınız Bir Süre Bloke Edildi")
                time.sleep(5)
                try_again(login, loginpassword)
    
    elif login == username:
        print("Kontrol Ediliyor...")
        time.sleep(2)
        print("Şifrenizi Kontrol Ediniz")
        passtry = 1
        again1 = str(input("Şifrenizi Tekrar Giriniz: "))
        if again1 != password:
            passtry += 1
            print("Şifrenizi Yine Hatalı Girdiniz!")
            again2 = str(input("Şifrenizi Tekrar Giriniz: "))
            if again2 != password:
                passtry += 1
                if passtry == 3:
                    print("Hesabınız Bir Süre Bloke Edildi...")
                    time.sleep(5)
                    try_again(login, loginpassword)
            elif again2 == password:
                print("Başarılı Bir Şekilde Giriş Yapıldı")
        elif again1 == password:
            print("Başarılı Bir Şekilde Giriş Yapıldı") 
  
try_again("yigituygun8", "ilovecoding88!")



