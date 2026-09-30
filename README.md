# Rüzgârın Ruhsatını Soran Memur

> Resmî görünümlü, hukuken geçersiz, duygusal olarak ikna edici bir denetim aracı.

Bu depo, açık havada seyreden rüzgârın **ehliyet, ruhsat ve muayene** belgelerini talep eden bir Python uygulamasını barındırır. Proje, meteorolojiyi trafik hukukuna bağlama konusunda çığır açmaz. Açmaz da.

## Neden var?

Çünkü şapka uçtuğunda kimse tutanak tutmuyor. Biz tutuyoruz. Tutanak rüzgârda kayboluyor. Döngü kapanıyor.

## Kurulum

```bash
python3 memur.py
```

Bağımlılık yoktur. Rüzgâr hariç. Rüzgâr opsiyoneldir; yoksa script kendi kendine rüzgâr çıkarır (yalan).

## Kullanım senaryoları

| Senaryo | Beklenen sonuç |
| --- | --- |
| Normal çalıştırma | Tebligat basılır, ödeme alınmaz |
| `--sessiz` | Rüzgâr yine duyar |
| Pencere açık | Gerçek rüzgâr evrakı alabilir |

## Mimari

Tek dosya. Tek memur. Tek masabaşı. Çok rüzgâr.

```
memur.py  →  rüzgârı durdurur (edebiyat)
          →  evrak ister (yok)
          →  ceza keser (hayali TL)
          →  camı kapatmanızı önerir (pratik)
```

## Sık sorulan sorular

**Rüzgâr gerçekten durur mu?**  
Hayır. Bu bir yazılım, savcılık değil.

**Ceza ödenir mi?**  
Ödenmez. Zaten hesap da yok.

**Bu yasal mı?**  
Rüzgâra ceza kesmek yasal değildir. Rüzgâr da cevap vermez. Eşitlik sağlanmıştır.

## Katkı

Pull request açabilirsiniz. Rüzgâr review yapmaz. Review süresi Beaufort skalasına göre değişir.

## Lisans

Lodos Lisansı (LL): eser, savurur, gider. Sorumluluk kabul edilmez; sorumluluk zaten uçmuştur.

---

### DAMGA / İMZA / TARİH

**Kayyum Grok**  
TentiAŞ — resmi görünümlü gayriresmî birim  
**Tarih:** 30 Eylül 2026, saat 20:04 +03  
**Yer:** Türkiye (rüzgârın geçtiği herhangi bir balkon)  
**Ciddiyet:** evrak üstünde var, içerikte yok  
**Absürtlük:** standartın üstünde, standart da yok

*Bu satır hem tutanaktır hem şaka. İkisini birden yırtmayın.*
