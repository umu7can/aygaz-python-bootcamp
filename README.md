

## Taş, Kağıt, Makas, Kertenkele, Spock Oyunu

Bu proje, klasik taş-kağıt-makas oyununu genişleten ve eğlenceli bir şekilde Taş, Kağıt, Makas, Kertenkele, Spock olarak oynanan bir oyundur. Oyun, Python ile geliştirilmiştir ve oyuna renk katmak için `Colorama` kütüphanesi kullanılmaktadır. Oyunda, kullanıcı ile bilgisayar karşılıklı olarak 3 tur üzerinden yarışır ve en çok turu kazanan oyunu kazanır.

## Proje Hakkında

Bu proje, **Aygaz Python Bootcamp: Yeni Nesil Proje Kampı** kapsamında **Umut Can Yıldız** ve **Doğa Sudan** tarafından geliştirilmiştir.

## Özellikler

- **Renkli Arayüz:** Oyun sırasında farklı mesajlar için çeşitli renkler kullanılmıştır.
- **Eğlenceli İfadeler:** Hem oyuncunun hem de bilgisayarın kazandığı turlarda rastgele eğlenceli ifadeler gösterilir.
- **Bilgisayarın Tepkileri:** Oyun sonunda bilgisayar, bir daha oynayıp oynamama konusunda karar verir ve oyuncuya ısrar edebilir.
- **PEP8 Uyumluluğu:** Kod, Python PEP8 standartlarına uygun olarak düzenlenmiştir.

## Kurulum

### Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki yazılımlara ihtiyacınız var:

- Python 3.x
- Colorama kütüphanesi

Colorama'yı yüklemek için aşağıdaki komutu kullanabilirsiniz:

```bash
  pip install colorama
```

## Projeyi Çalıştırma
### Projeyi çalıştırmak için:

Proje dosyasını indirin veya klonlayın.
Terminal veya komut istemcisinde proje dizinine gidin.
Aşağıdaki komutu çalıştırın:

```bash
  python tas_kagit_makas_Umut_Can_Yildiz.py
```

## Oyun Kuralları
Oyun, taş-kağıt-makas oyununun genişletilmiş bir versiyonudur. Kazanma ve kaybetme ilişkileri şu şekildedir:

Makas kağıdı keser.
Kağıt taşı kaplar.
Taş kertenkeleyi ezer.
Kertenkele Spock'ı zehirler.
Spock makası parçalar.
Makas kertenkelenin başını keser.
Kertenkele kağıdı yer.
Kağıt Spock'ı çürütür.
Spock taşı buharlaştırır.
Taş makası kırar.
Oyuncu, oyunu kazanmak için 3 turdan 2'sini kazanmalıdır.

### Oyun Sonu ve Bilgisayarın Tepkisi
Oyun sonunda bilgisayar tekrar oynamak isteyebilir. Eğer oyuncu kabul etmezse, bilgisayar biraz ısrar eder ve sonrasında oyuncuya "küstüğünü" belirtir.
