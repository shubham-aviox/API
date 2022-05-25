from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

PROXY = 'http://proxy.zyte.com:8011'
proxyHost = "proxy.zyte.com"
proxyPort = "8011"

fp = webdriver.FirefoxProfile()
fp.set_preference("network.proxy.type", 1)
fp.set_preference("network.proxy.http", proxyHost) #HTTP PROXY
fp.set_preference("network.proxy.http_port", int(proxyPort))
fp.set_preference("network.proxy.ssl", proxyHost) #SSL  PROXY
fp.set_preference("network.proxy.ssl_port", int(proxyPort))
fp.set_preference('network.proxy.socks', proxyHost) #SOCKS PROXY
fp.set_preference('network.proxy.socks_port', int(proxyPort))

fp.update_preferences()
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp) 
driver.get("http://www.whatismyip.com/")
def proxy():
    proxy_host = "proxy.zyte.com"
    proxy1=proxy_host + ':' +proxy_port
    print(proxy1)
    proxy_auth = "<Smart Proxy Manager API KEY>:" # Make sure to include ':' at the end
    proxies = {"https": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
          "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}

    return proxies
proxy()
print(proxy()['https'])