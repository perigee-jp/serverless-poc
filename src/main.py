import chromedriver_binary
import os
import base64
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main() -> None:
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.get("https://google.com")

    print(f"Current ULR: {driver.current_url}")

    secret_b64 = os.environ["SECRET"]
    secret = json.loads(base64.b64decode(secret_b64).decode())
    print(secret["url"])

if __name__ == "__main__":
    main()
