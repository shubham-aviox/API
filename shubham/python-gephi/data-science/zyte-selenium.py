from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# proxy_username = "USER_NAME"
# proxy_password = "PASSWORD"
proxy_auth = '61c6498052c94290892a400b3314cf78'
proxy_url = "proxy.zyte.com"
proxy_port = 8011

options = {
    "proxy": {
        "http": f"http://{proxy_auth}:@{proxy_url}:{proxy_port}",
        "verify_ssl": False,
    },
}

URL = "https://httpbin.org/headers?json"

driver = webdriver.Chrome(ChromeDriverManager().install(), seleniumwire_options=options)
driver.get(URL)
time.sleep(100)