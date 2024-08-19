#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
from colorama import Fore, init

# Renkli metinler için colorama modülünü başlatıyoruz
init(autoreset=True)


def bilgisayar_karari():
    karar = random.choice(["oynamak istiyorum", "oynamak istemiyorum"])
    if karar == "oynamak istiyorum":
        print(Fore.MAGENTA + "💻 Hadi bir daha oynayalım!")
        return True
    else:
        print(Fore.RED + "💻 Seninle bir daha oynamak istemiyorum!")
        return False


def evet_hayir_sorusu(soru):
    while True:
        cevap = input(soru).lower()
        if cevap in ["evet", "hayır"]:
            return cevap
        else:
            print(Fore.RED + "Geçersiz giriş! Lütfen sadece 'evet' veya 'hayır' yazın.")


def tas_kagit_makas_Umut_Can_Yildiz():
    # Kullanıcıdan isim alıyoruz
    oyuncu_isim = input(Fore.CYAN + "Oyuncu isminizi girin: ").strip()
    bilgisayar_isim = input(Fore.CYAN + "Bilgisayara isim ver: ").strip()

    # Oyun Tanıtımı
    print(Fore.CYAN + f"🌟 Taş, Kağıt, Makas, Kertenkele, Spock Oyununa Hoşgeldiniz, {oyuncu_isim}! 🌟")
    print(Fore.MAGENTA + "Kurallar: ")
    print(Fore.MAGENTA + "- Makas kağıdı keser.")
    print(Fore.MAGENTA + "- Kağıt taşı kaplar.")
    print(Fore.MAGENTA + "- Taş kertenkeleyi ezer.")
    print(Fore.MAGENTA + "- Kertenkele Spock'ı zehirler.")
    print(Fore.MAGENTA + "- Spock makası parçalar.")
    print(Fore.MAGENTA + "- Makas kertenkelenin başını keser.")
    print(Fore.MAGENTA + "- Kertenkele kağıdı yer.")
    print(Fore.MAGENTA + "- Kağıt Spock'ı çürütür.")
    print(Fore.MAGENTA + "- Spock taşı buharlaştırır.")
    print(Fore.MAGENTA + "- Taş makası kırar.")
    print(Fore.YELLOW + "Best of 3 usulü: İlk iki turu kazanan oyunu kazanır.")
    print(Fore.GREEN + "Oyundan çıkmak için 'q' tuşuna basabilirsiniz.")

    # Oyun Kurulumu
    secenekler = ['taş', 'kağıt', 'makas', 'kertenkele', 'spock']
    oynanan_oyun_sayisi = 0
    oyuncu_galibiyetleri = 0
    bilgisayar_galibiyetleri = 0

    while True:
        # Oyun Sayaçlarının Sıfırlanması
        oyuncu_tur_galibiyeti = 0
        bilgisayar_tur_galibiyeti = 0

        # Turların Döngüsü
        while oyuncu_tur_galibiyeti < 2 and bilgisayar_tur_galibiyeti < 2:
            print(Fore.CYAN + "\n✨ Taş, kağıt, makas, kertenkele veya spock seçin! ✨")
            oyuncu_secimi = input(f"{oyuncu_isim} seçiminiz: ").lower()

            if oyuncu_secimi == 'q':
                print(Fore.RED + "Oyun sonlandırılıyor... Güle güle!")
                return

            if oyuncu_secimi not in secenekler:
                print(Fore.RED + "Geçersiz seçim! Lütfen tekrar deneyin.")
                continue

            bilgisayar_secimi = random.choice(secenekler)
            print(Fore.MAGENTA + f"💻 {bilgisayar_isim}'ın seçimi: {bilgisayar_secimi}")

            # Kazananı Belirleme
            if oyuncu_secimi == bilgisayar_secimi:
                print(Fore.YELLOW + "😐 Beraberlik! Şansını tekrar dene.")
            elif (oyuncu_secimi == 'makas' and (bilgisayar_secimi in ['kağıt', 'kertenkele'])) or \
                 (oyuncu_secimi == 'kağıt' and (bilgisayar_secimi in ['taş', 'spock'])) or \
                 (oyuncu_secimi == 'taş' and (bilgisayar_secimi in ['makas', 'kertenkele'])) or \
                 (oyuncu_secimi == 'kertenkele' and (bilgisayar_secimi in ['spock', 'kağıt'])) or \
                 (oyuncu_secimi == 'spock' and (bilgisayar_secimi in ['makas', 'taş'])):
                print(Fore.GREEN + f"🎉 {oyuncu_isim} bu turu kazandı! Devam edin!")
                oyuncu_tur_galibiyeti += 1
                # Kullanıcı kazandığında rastgele bir yorum
                oyuncu_yorumlari = [
                    "Şans yıldızlar gibi parlıyor!",
                    "Zafere bir adım daha yaklaştınız!",
                    f"{bilgisayar_isim} fırtına öncesi sessizliğe büründü!",
                    "Bu sefer kartlar sizin lehinize!"
                ]
                print(Fore.MAGENTA + random.choice(oyuncu_yorumlari))
            else:
                print(Fore.RED + f"🙁 {bilgisayar_isim} bu turu kazandı! Daha iyisini yapabilirsiniz.")
                bilgisayar_tur_galibiyeti += 1
                # Bilgisayar kazandığında rastgele bir yorum
                bilgisayar_yorumlari = [
                    f"{bilgisayar_isim} bu hamleyi çok iyi hesapladı!",
                    f"{bilgisayar_isim} galibiyeti kapmak üzere!",
                    f"{bilgisayar_isim} stratejisini mükemmel uyguladı!",
                    f"{bilgisayar_isim} yine güçlü bir oyun sergiledi!"
                ]
                print(Fore.MAGENTA + random.choice(bilgisayar_yorumlari))

            # Skor Tablosunu Gösterme
            print(Fore.CYAN + f"\nSkor Tablosu: {oyuncu_isim} {oyuncu_tur_galibiyeti} - "
                              f"{bilgisayar_tur_galibiyeti} {bilgisayar_isim}")

        # Oyun Galibini Belirleme
        if oyuncu_tur_galibiyeti == 2:
            print(Fore.GREEN + f"\n🏆 Tebrikler {oyuncu_isim}! Oyunu kazandınız! 🏆")
            oyuncu_galibiyetleri += 1
        else:
            print(Fore.RED + f"\n💔 Üzgünüm, {bilgisayar_isim} oyunu kazandı. "
                             "Bu sefer şanslıydı, bir dahakinde bu kadar şanslı olmaz umarım!")
            bilgisayar_galibiyetleri += 1

        oynanan_oyun_sayisi += 1

        # Bilgisayarın Oynama Kararı
        bilgisayar_devam = bilgisayar_karari()
        if bilgisayar_devam:
            # Oyuncunun Devam Etme İsteği
            devam = evet_hayir_sorusu(Fore.YELLOW + "\nBaşka bir oyun oynamak ister misiniz? (Evet/Hayır): ")
            if devam == 'hayır':
                print(Fore.RED + f"💻 {bilgisayar_isim}: Lütfen, hadi bir oyun daha! 🙏")
                devam = evet_hayir_sorusu(Fore.YELLOW + "\nGitmek istediğinize emin misiniz? (Evet/Hayır): ")
                if devam == 'evet':
                    print(Fore.RED + f"💻 {bilgisayar_isim}: Nasıl yani? Hadi ama! Oynamak istemiyor musun?")
                    print(Fore.RED + f"💻 {bilgisayar_isim}: Hıh, seninle bir daha oynamayacağım! Küstüm!")
                    break
        else:
            print(Fore.CYAN + f"{bilgisayar_isim} oyunu bitiriyor... İyi günler dileriz!")
            break

    print(Fore.CYAN + f"\nOyun Sonu: {oyuncu_isim} {oyuncu_galibiyetleri} - {bilgisayar_galibiyetleri} {bilgisayar_isim}")


# Oyunu başlatmak için fonksiyonu çağırın
tas_kagit_makas_Umut_Can_Yildiz()


# In[ ]:




