import requests
import os

# https://api.telegram.org/bot<token>/getUpdates

def valid_image_extension(image):
    ext = os.path.splitext(image.name)[1]
    if ext==".png" or ext == ".jpg" or ext ==".jpeg":
        return True
    else:
        print('wrong')
        return False


TOKEN = "5315433451:AAHvIW8trdxHReIzPYaPb2ezHXQrd7QadBA"
chat_id = "-671876824"
text = "Hello there"
files = {'document': open('screenshot.png','rb')}
print(dir(files['document']))
file_name = files.get('document')
attach_file = True



if attach_file:
    if valid_image_extension(file_name):
        url = f"https://api.telegram.org/bot{TOKEN}/sendDocument?chat_id={chat_id}&caption={text}"
        r = requests.get(url, files=files)
else:
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}"
    r = requests.get(url)
    print('send')