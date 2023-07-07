# Yüz Tanıma Tabanlı Katılım Sistemi
Yoklama almak için yüz tanıma kullanan bir python GUI entegre katılım sistemi.

Bu python projemde yüz tanıma tekniğini kullanarak yoklama alan bir yoklama sistemi yaptım. Ayrıca GUI (Grafik kullanıcı arayüzü) ile entegre ettim, böylece herkes tarafından kullanımı kolay olabilir. Bu proje için GUI de tkinter kullanılarak python üzerinde yapılmıştır.

KULLANILAN TEKNOLOJİ:

tüm GUI için tkinter
Görüntü almak ve yüz tanıma için OpenCV (cv2.face.LBPHFaceRecognizer_create())
Diğer amaçlar için CSV, Numpy, Pandas, datetime vb.
ÖZELLİKLERİ:

Etkileşimli GUI desteği ile kullanımı kolaydır.
Yeni kişi kaydı için şifre koruması.
Kayıt sırasında öğrencilerin bilgileri için CSV dosyası oluşturur/günceller.
Katılım için her gün yeni bir CSV dosyası oluşturur ve katılımı uygun tarih ve saatle işaretler.
Ana ekranda gün için canlı katılım güncellemelerini kimlik, ad, tarih ve saat ile tablo biçiminde görüntüler.
Yüklenmesi gereken paketler:

-tk-tools -opencv-contrib-python -datetime -pytest-shutil -python-csv -numpy -pillow -pandas -times

Ekran Görüntüsü