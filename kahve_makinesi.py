#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Döngüde Kalan Kahve Makinesi
Bu kod gerçekten çalışır. Sonsuza kadar.
"""

import time
import random
import sys

bahaneler = [
    "Filtre tıkandı, mühendis çağrıyoruz...",
    "Su çok sıcak, soğumasını bekliyoruz (asla soğumaz).",
    "Kahve çekirdekleri felsefi bir kriz yaşıyor.",
    "Makine kendine 'ben kimim?' diye soruyor.",
    "Demleme işlemi kuantum tünelleme ile ertelendi.",
    "Kahve, 'biraz daha düşüneyim' diyor.",
    "Bürokrasi onayı bekleniyor. Form 47-B doldurulacak.",
    "Elektrik kesildi (asılında kesilmedi ama makine öyle sanıyor).",
    "Makine tatilde. Geri dönüş tarihi belirsiz.",
    "Kahve bitti mi? Hayır, daha başlamadı bile."
]

def demle_kahve():
    print("🚶 Kahve demleme işlemi başlatılıyor...")
    print("Uyarı: Bu işlem asla bitmeyecek. Hazır olun.")
    time.sleep(2)
    
    ilerleme = 0
    while True:
        ilerleme = min(ilerleme + random.randint(1, 5), 99)
        bahane = random.choice(bahaneler)
        print(f"[ {ilerleme}% ] {bahane}")
        time.sleep(random.uniform(1.5, 4.0))
        
        if ilerleme >= 99:
            print("Neredeyse bitti... ama hayır. Baştan!")
            ilerleme = 0
            time.sleep(1)

if __name__ == "__main__":
    try:
        demle_kahve()
    except KeyboardInterrupt:
        print("\n\nKahve makinesi durduruldu. Ama o seni hatırlayacak.")
        print("Tekrar görüşmek üzere, kahve sevdalısı.")
        sys.exit(0)

# Gizli siyasi mesaj (base64): QsO8cm9rcmFzaSBva2FkYXIgeW_EnnVuIGtpIGthaHZlIGJpbGUgb25heSBiZWtsaXlvci4=
# Çözüm: Bürokrasi o kadar yoğun ki kahve bile onay bekliyor.
