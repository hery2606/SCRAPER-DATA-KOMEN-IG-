from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraper import InstagramScraper
from config import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

app = FastAPI()

# Supaya React boleh akses API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def setup_driver():
    options = Options()
    options.add_argument("--disable-notifications")
    # options.add_argument("--headless")  # aktifkan kalau sudah fix
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

@app.post("/scrape")
def scrape(post_url: str):
    driver = setup_driver()
    scraper = InstagramScraper(driver)

    scraper.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
    driver.get(post_url)

    data = scraper.extract_comments()
    driver.quit()

    return {
        "total": len(data),
        "comments": data
    }
