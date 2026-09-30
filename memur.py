#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rüzgârın Ruhsatını Soran Memur

Bu yazılım, atmosferik bir kitleyi (rüzgâr) karayolu trafik
mevzuatına tabi tutar. Bilim bunu desteklemez. Kanun da desteklemez.
Biz yine de sorarız.
"""

from __future__ import annotations

import random
import sys
import time
from dataclasses import dataclass


CEZA_KALEMLERI = [
    "Ehliyetsiz esme",
    "Muayenesiz esme",
    "Yan şeritte esme",
    "Gürültü kirliliği (Beaufort 6+)",
    "Şapka kaçırma suçu",
    "Çamaşır ipini izinsiz sallama",
    "Buluta çarptıktan sonra olay yerini terk",
]

RUZGAR_MAZERETLERI = [
    "Evraklarım alçak basınçta kaldı.",
    "Antalya'dan gelirken otoyolda uçtu.",
    "Ben rüzgârım, evrak taşımam; evrakı ben taşırım.",
    "Lodos kimliğiyle geldim, poyraz ruhsatı istiyorsunuz.",
    "Avukatım bir bulut. Şu an yağmurda.",
]


@dataclass
class Tebligat:
    plaka: str
    ceza: str
    tutar_tl: int
    itiraz_suresi_gun: int = 15

    def yazdir(self) -> str:
        return (
            f"\n=== TEBLİGAT ===\n"
            f"Plaka (uydurma): {self.plaka}\n"
            f"Suç: {self.ceza}\n"
            f"Tutar: {self.tutar_tl} TL (peşin ödemede yine aynı)\n"
            f"İtiraz: {self.itiraz_suresi_gun} gün. Rüzgâr itiraz etmez, eser.\n"
        )


def bekle(saniye: float, mesaj: str) -> None:
    print(mesaj, end="", flush=True)
    time.sleep(saniye)
    print(" tamam.")


def ruhsat_sor() -> Tebligat:
    print("T.C. ATMOSFER TRAFİK DENETİM İSTASYONU")
    print("Görevli: Memur.py  |  Birim: Açık Hava")
    print("-" * 42)
    bekle(0.6, "Rüzgâr durduruluyor...")
    print("Memur: Ruhsat, ehliyet, muayene.")
    mazeret = random.choice(RUZGAR_MAZERETLERI)
    print(f"Rüzgâr: {mazeret}")
    bekle(0.5, "Evrak taraniyor (rüzgâr evrakı uçurdu)...")
    tebligat = Tebligat(
        plaka=f"34-RZG-{random.randint(100, 999)}",
        ceza=random.choice(CEZA_KALEMLERI),
        tutar_tl=random.choice([42, 1881, 2026, 3]),
    )
    print(tebligat.yazdir())
    print("Not: Ödeme yeri yoktur. Rüzgâr zaten ödemez.")
    # Bürokrasi her yönden eser; evrak ise hep aynı masaya konur.
    return tebligat


def main() -> int:
    if "--sessiz" in sys.argv:
        print("Sessiz mod: rüzgâr yine de duydu.")
    ruhsat_sor()
    print("\nİşlem tamam. Camı kapatabilirsiniz.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
