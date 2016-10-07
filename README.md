yedekle.py kodları, yedek_cfg.py dosyasındaki temel parametreleri kullanıyor.

ANA_DIZIN: Yedeklenecek kodların yer aldığı altdizinlerin bulunduğu dizin
ALT_DIZINLER: İçinde yedeklenecek kod dosyalarının bulunduğu alt dizinlerin listesi
YEDEK_DIZIN: Kod dosyalarının içine yedekleneceği ana dizin
UZANTILAR: Yedeklenecek dosyaların sahip olduğu uzantıların listesi

Sistem kabaca şöyle çalışıyor: Önce ANA_DIZIN içindeki ALT_DIZIN elemanlarının içinde bulunan
kod dosyaları bulunuyor. Bu dosyaların yedek klasöründeki adresleri belirleiyor ve her iki dosyanın 
hash bilgileri karşılaştırılıyor. Aynı iseler, yedeklemeye gerek yok demektir.
Eğer hash değerleri farklıysa ve yedek dosya mevcutsa, o anki zamana göre adı değiştiriliyor.
Orijinal dosya, yedek klasörüne kopyalanıyor.

Ben bu kodu günde bir kez çalıştırmayı planlıyorum. O yüzden kod saklama hassaslığını 1 gün yaptım.
İsterseniz, damgatar fonksiyonu ile daha hassas bir isimlendirme yaptırabilirsiniz.

Daha sonra, yedek sayısını sınırlandırmak için bir limit eklemeyi düşünüyorum.
Şu aşamada dosyaları sıkıştırmayı düşünmedim. Gerekirse, bu da yapılabilir.

Kodlar henüz yeterince test edilmedi. Öneri ve bulgularınızı paylaşırsanız sevinirim.

Bu repoyu aynı zamanda git komutlarını test etmek amacıyla kullandım.
Aşağıdaki yöntem sorunsuz çalışıyor.
Ancak ssh-key sistemini henüz devreye sokamadım.

echo "# python_yedek" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/ahmetax/python_yedek.git
git push -u origin master

Date: Oct 07, 2016

