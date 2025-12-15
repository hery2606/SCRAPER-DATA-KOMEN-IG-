import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstagramScraper:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        """Login otomatis ke Instagram"""
        try:
            # Buka halaman login Instagram
            self.driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(3)
            
            print(">>> Memulai login otomatis...")
            
            # Tunggu hingga form login muncul
            username_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = self.driver.find_element(By.NAME, "password")
            
            # Ketik username dan password
            username_input.send_keys(username)
            time.sleep(1)
            password_input.send_keys(password)
            time.sleep(1)
            
            # Klik tombol login
            login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()
            
            print(">>> Menunggu proses login...")
            time.sleep(5)
            
            # Handle popup "Save Login Info" jika muncul
            try:
                not_now_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
                )
                not_now_button.click()
                print(">>> Popup 'Save Login Info' ditutup")
                time.sleep(2)
            except:
                print(">>> Tidak ada popup 'Save Login Info'")
            
            # Handle popup "Turn on Notifications" jika muncul
            try:
                not_now_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
                )
                not_now_button.click()
                print(">>> Popup 'Notifications' ditutup")
                time.sleep(2)
            except:
                print(">>> Tidak ada popup 'Notifications'")
            
            print(">>> Login berhasil!")
            
        except Exception as e:
            print(f">>> Error saat login: {e}")
            print(">>> Silakan login MANUAL...")
            input(">>> Tekan ENTER setelah login manual berhasil...")
    
    def click_load_more(self):
        """Mencoba berbagai cara untuk menekan tombol 'Load more'"""
        clicked = False
        
        # Daftar kemungkinan selector tombol load more
        selectors = [
            "svg[aria-label='Load more comments']",
            "svg[aria-label='Muat komentar lainnya']",
            "ul > li > div > button",
            "//span[contains(text(), 'View all')]",
            "//span[contains(text(), 'Lihat semua')]"
        ]

        for selector in selectors:
            try:
                if "//" in selector:  # Pakai XPATH
                    btn = self.driver.find_element(By.XPATH, selector)
                else:  # Pakai CSS
                    btn = self.driver.find_element(By.CSS_SELECTOR, selector)
                
                # Coba klik
                self.driver.execute_script("arguments[0].click();", btn)
                clicked = True
                break
            except:
                continue
        
        return clicked
    
    def extract_comments(self, max_comments=None):
        """Ekstraksi HANYA komentar utama (tanpa reply)"""
        print("\n--- Memulai Ekstraksi Komentar Utama ---")
        extracted_data = []
        comment_count = 0
        
        try:
            # Strategi: Ambil semua elemen span dengan dir='auto'
            comment_texts = self.driver.find_elements(By.CSS_SELECTOR, "span[dir='auto']")
            
            print(f"Deteksi awal: Ditemukan {len(comment_texts)} elemen teks potensial.")
            
            if max_comments:
                print(f"Target: Mengambil maksimal {max_comments} komentar")

            for text_elem in comment_texts:
                # BATASAN: Stop jika sudah mencapai max_comments
                if max_comments and comment_count >= max_comments:
                    print(f"\n✓ Batas maksimal {max_comments} komentar tercapai!")
                    break
                
                try:
                    text_content = text_elem.text.strip()
                    
                    # Filter: Komentar tidak kosong
                    if not text_content: 
                        continue

                    # Mencari Parent Container
                    parent_container = text_elem.find_element(By.XPATH, "./../../..")
                    
                    # FILTER: Skip jika ini adalah reply (balasan)
                    # Reply biasanya berada di dalam nested <ul> atau memiliki indentasi
                    try:
                        # Cek apakah ada ancestor ul yang merupakan reply container
                        reply_check = text_elem.find_element(By.XPATH, 
                            "./ancestor::ul[contains(@style, 'padding') or contains(@class, 'repl')]"
                        )
                        # Jika ditemukan, skip (ini adalah reply)
                        continue
                    except:
                        # Tidak ada ancestor reply container, ini komentar utama
                        pass
                    
                    # Cari Username di dalam parent container
                    try:
                        username_elem = parent_container.find_element(By.CSS_SELECTOR, "h3 a, div a")
                        username = username_elem.text.strip()
                    except:
                        continue

                    # Filter username invalid
                    if not username or username in ["Reply", "Suka", "Like", "View replies", "Lihat balasan", ""]:
                        continue
                    
                    # Ambil waktu posting (opsional)
                    try:
                        time_elem = parent_container.find_element(By.CSS_SELECTOR, "time")
                        post_time = time_elem.get_attribute("datetime")
                    except:
                        post_time = ""
                    
                    # Increment nomor komentar
                    comment_count += 1
                    
                    # Simpan data
                    data = {
                        "No": comment_count,
                        "Username": username,
                        "Komentar": text_content,
                        "Waktu": post_time
                    }
                    
                    # Cegah duplikat
                    if data not in extracted_data:
                        extracted_data.append(data)
                        
                        # Tampilkan preview yang lebih rapi
                        preview = text_content[:60] + "..." if len(text_content) > 60 else text_content
                        print(f"[{comment_count}] @{username}: {preview}")

                except Exception as e:
                    continue

        except Exception as e:
            print(f"Error saat scanning elemen: {e}")

        return extracted_data