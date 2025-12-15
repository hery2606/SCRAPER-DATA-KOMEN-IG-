import time
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from config import (
    INSTAGRAM_USERNAME, 
    INSTAGRAM_PASSWORD,
    POST_URL,
    SCROLL_PAUSE,
    LOAD_MORE_ATTEMPTS,
    MAX_COMMENTS
)
from scraper import InstagramScraper

def setup_driver():
    """Setup Chrome WebDriver"""
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Uncomment untuk headless mode
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), 
        options=chrome_options
    )
    return driver

def save_to_csv(data, post_url):
    """Simpan data ke CSV dengan format yang rapi"""
    if not data:
        print("\n✗ Tidak ada data untuk disimpan.")
        return
    
    # Buat DataFrame
    df = pd.DataFrame(data)
    
    # Generate nama file dengan timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"hasil_komentar_ig_{timestamp}.csv"
    
    # Simpan ke CSV dengan pengaturan yang lebih baik
    df.to_csv(
        filename, 
        index=False, 
        encoding='utf-8-sig',  # Untuk support Excel + emoji
        sep=',',
        quotechar='"',
        quoting=1  # QUOTE_ALL - semua field dikutip
    )
    
    print(f"\n{'='*70}")
    print(f"✓ SUKSES! Data berhasil disimpan")
    print(f"{'='*70}")
    print(f"📁 File        : {filename}")
    print(f"📊 Total Data  : {len(data)} komentar utama")
    print(f"🔗 URL Post    : {post_url}")
    print(f"⏰ Waktu       : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"{'='*70}")
    
    # Tampilkan preview data dengan format tabel yang rapi
    print("\n📋 Preview Data (10 baris pertama):")
    print("="*70)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 50)
    print(df.head(10).to_string(index=False))
    print("="*70)
    
    # Tampilkan statistik
    print("\n📈 Statistik Komentar:")
    print("-"*70)
    print(f"• Username unik      : {df['Username'].nunique()}")
    print(f"• Rata-rata panjang  : {df['Komentar'].str.len().mean():.0f} karakter")
    print(f"• Komentar terpanjang: {df['Komentar'].str.len().max()} karakter")
    print(f"• Komentar terpendek : {df['Komentar'].str.len().min()} karakter")
    print("-"*70)

def main():
    driver = None
    
    try:
        # Setup browser
        print("\n" + "="*70)
        print("🚀 INSTAGRAM COMMENT SCRAPER - KOMENTAR UTAMA SAJA")
        print("="*70)
        print(">>> Menyiapkan browser...")
        driver = setup_driver()
        
        # Inisialisasi scraper
        scraper = InstagramScraper(driver)
        
        # Login
        scraper.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
        
        # Buka postingan
        print(f"\n>>> Membuka: {POST_URL}")
        driver.get(POST_URL)
        time.sleep(5)
        
        # Scroll & Load More
        print("\n>>> Memuat komentar lama...")
        for i in range(LOAD_MORE_ATTEMPTS):
            success = scraper.click_load_more()
            if success:
                print(f"⬇️  Tombol Load More ditekan ({i+1}/{LOAD_MORE_ATTEMPTS})...")
                time.sleep(SCROLL_PAUSE)
            else:
                # Scroll untuk memicu lazy load
                driver.execute_script("window.scrollBy(0, 300);")
                time.sleep(1)
        
        # Ekstraksi komentar (HANYA KOMENTAR UTAMA)
        # Gunakan MAX_COMMENTS dari config.py atau None untuk unlimited
        hasil = scraper.extract_comments(max_comments=MAX_COMMENTS)
        
        # Simpan hasil
        save_to_csv(hasil, POST_URL)
    
    except Exception as e:
        print(f"\n✗ Error Fatal: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        if driver:
            # driver.quit()  # Uncomment untuk auto close browser
            print("\n>>> Proses selesai. Browser tetap terbuka untuk verifikasi.")
            input(">>> Tekan ENTER untuk menutup browser...")
            driver.quit()

if __name__ == "__main__":
    main()