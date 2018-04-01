# import sys, os, multiprocessing, urllib2, csv
import sys, os, multiprocessing, urllib, csv
from urllib.request import urlopen
from PIL import Image
# from StringIO import StringIO # This package is gone.
import io
import time
from binascii import hexlify
from codecs import encode


def hex2bin(s):
    hex_table = ['0000', '0001', '0010', '0011',
                 '0100', '0101', '0110', '0111',
                 '1000', '1001', '1010', '1011',
                 '1100', '1101', '1110', '1111']
    bits = ''
    for i in range(len(s)):
        bits += hex_table[int(s[i], base=16)]
    return bits

class GetData:

    def __init__(self, url, destination_path_and_name):

        self.url = url
        self.destination_path_and_name = destination_path_and_name

        self.pil_image_rgb = None

        pass

    @staticmethod
    def get_image(url):
        response = urlopen(url)
        image_data = response.read()
        return image_data
        pass

    def convert_data(self):
        image_data = self.get_image(self.url)
        pil_image = Image.open(io.BytesIO(image_data))
        self.pil_image_rgb = pil_image.convert('RGB')
        pass

    def save_data(self):
        self.pil_image_rgb.save(self.destination_path_and_name, format='JPEG', quality=90)

