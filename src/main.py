import chromedriver_binary
import os
import base64
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from typing import Dict
import boto3


def get_secret() -> Dict:
    secret_b64 = os.environ["SECRET"]
    secret = json.loads(base64.b64decode(secret_b64).decode())
    return secret

def main() -> None:
    options = Options()
    options.add_argument("--headless")

    secret = get_secret()

    browser = webdriver.Chrome(options=options)
    browser.get(secret["url"])

    print(f"Current ULR: { secret['url'] }")
    html = browser.page_source
    write_text(html, secret["s3-bucket-name"], "index.html")

#s3にテキストを書き込む
def write_text(text: str, bucket_name: str, key: str) -> None:
    s3 = boto3.client("s3")
    s3.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=text
    )


if __name__ == "__main__":
    main()
