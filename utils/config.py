import os

class Config:
    BASE_URL = "https://www.saucedemo.com/"
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADERS", "false").lower() == "true"