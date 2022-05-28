# For creating qr-codes->
# qrcode.make() takes parameters as Strings,links,etc.

import qrcode
img = qrcode.make("hello my name is kunal")
img.save("barcode.png")

# For reading qr-codes->

import cv2
d = cv2.QRCodeDetector()
d.detectAndDecode(cv2.imread("barcode.png"))
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("barcode.png"))
print(val)


# -- A sample barcode is generated that has my info in it...
