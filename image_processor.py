import base64

from PIL import Image
from collections import Counter

class ImageProcessor:
    def __init__(self):
        pass

    def extract_colours(self, form_data, tmp_path):
        with Image.open(tmp_path).convert("RGBA") as image_uploaded:
            print(image_uploaded.height * image_uploaded.width)
            visible_pixels = [pixel[:3] for pixel in list(image_uploaded.getdata()) if pixel[3] > 0] # get the first 3 values of tuple
            # print(visible_pixels)
            number_of_pixels = len(visible_pixels)
            print(number_of_pixels)
            # print(list(image_uploaded.getdata())) # yellow warning from IDE but still can convert to list since the object is iterable
            freq_list = Counter(visible_pixels)
            # print(list(freq_list.items())[:5]) # .items() converts it into a dict_item obejct, you can iterate over it, but it is NOT a list, to convert it into a list
            # need to use list(). the line above prints the FIRST 5 items in a list
            top_colours = freq_list.most_common(form_data['number_of_colours']) # this prints the TOP N most common colours
            top_hex_codes = {}
            for colour in top_colours:
                # hex_code = '#%02x%02x%02x' % tuple(colour[0]) # make it clear that you are passing in the tuple to format the text, since '#%02x%02x%02x' expects 3 values in the form of tuple (r,g,b)

                # another way to convert rgb values to hex code
                r,g,b = colour[0] # unpacking the tuple, since f-string formatting only handles one value at a time not an entire tuple
                hex_code = f"#{r:02x}{g:02x}{b:02x}"
                top_hex_codes[hex_code] = colour[1]
            return top_hex_codes, number_of_pixels
            # for pixel in image_uploaded.getdata():
            #     print(pixel)
                # you will see 4 values in the tuple, the fourth value is the alpha,
                # 255 means fully opaque, 0 means transparent
                # to avoid this and ensure we only get 3 channels, we can change the mode of the image, simply by doing .convert("RGB")

    def encode_image(self, tmp_path):
        # tmp means temporary
        with open(tmp_path, 'rb') as img_file:
            encoded_image = base64.b64encode(img_file.read()).decode("utf-8")
            image_data_url = f"data:image/png;base64,{encoded_image}"
        return image_data_url
        # this data url is only used to display the img in the img tag, NOT reading the img, for reading the img use tmp path

        # A quick run down of how this tmp path works, why we need to generate a data url, basically encoding it
        # User uploads image → Flask saves it to /tmp → Flask reads the binary (raw bytes, 1 and 0) →
        # Base64 encodes it (into a text string which can be added in the image element) → Flask embeds it as <img src="data:..."> → Browser displays it
        # so normally an img tag has a url in the src attribute, which the html will need to go into that url to fetch the image,
        # but now html doesn't need to do that as data url allows it to fetch it DIRECTLY in the HTML itself
