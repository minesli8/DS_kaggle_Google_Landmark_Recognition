
# coding: utf-8

# In[ ]:


from urllib.request import urlopen
from PIL import Image
# from StringIO import StringIO # This package is gone.
import io # use io.BytesIO

class GetData:

    def __init__(self, url, destination_path_and_name):

        self.url = url
        self.destination_path_and_name = destination_path_and_name

        self.pil_image_rgb = None

    @staticmethod
    def get_image(url):
        response = urlopen(url)
        image_data = response.read()
        return image_data

    def convert_data(self):
        image_data = self.get_image(self.url)
        pil_image = Image.open(io.BytesIO(image_data))
        self.pil_image_rgb = pil_image.convert('RGB')
        pass

    def save_data(self):
        self.pil_image_rgb.save(self.destination_path_and_name, format='JPEG', quality=90)
        
    def run(self):
        self.convert_data()
        self.save_data()
        return 

