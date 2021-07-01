"""
    [+] Created on Mon May 24 19:48:39 2021
    [+] Project on Python3
    [*] By Rahul Dey
    [+] @author: mine
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import qrcode

data = input("Enter data to add : ")
file_name = input("Filename with extension : ")
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='red', back_color='white')
img.save(file_name)

# img = qrcode.make(data)
# img.save('one.png')