from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from forms import ImageForm
from PIL import Image
from collections import Counter
import uuid
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('APP_KEY')
Bootstrap5(app)

@app.route("/", methods=['POST','GET'])
def home():
    form = ImageForm()
    if form.validate_on_submit():

        # must use unique filenames, as only 1 global static folder when website is hosted. unique filenames ensure each user
        # sees the correct image.
        filename = f"{uuid.uuid4().hex}.png" # uuid is universal unique identifier, unlikely to repeat. the .hex just strips the '-' and returns the 32 character string instead.
        form.data['file'].save(f"static/images/{filename}")


        with Image.open(form.data['file']).convert("RGB") as image_uploaded:
            number_of_pixels = image_uploaded.width * image_uploaded.height
            print(number_of_pixels)
            # print(list(image_uploaded.getdata())) # yellow warning from IDE but still can convert to list since the object is iterable
            freq_list = Counter(image_uploaded.getdata())
            # print(list(freq_list.items())[:5]) # .items() converts it into a dict_item obejct, you can iterate over it, but it is NOT a list, to convert it into a list
            # need to use list(). the line above prints the FIRST 5 items in a list
            top_colours = freq_list.most_common(form.data['number_of_colours']) # this prints the TOP 5 most common colours
            top_hex_codes = {}
            for colour in top_colours:
                # hex_code = '#%02x%02x%02x' % tuple(colour[0]) # make it clear that you are passing in the tuple to format the text, since '#%02x%02x%02x' expects 3 values in the form of tuple (r,g,b)

                # another way to convert rgb values to hex code
                r,g,b = colour[0] # unpacking the tuple, since f-string formatting only handles one value at a time not an entire tuple
                hex_code = f"#{r:02x}{g:02x}{b:02x}"
                top_hex_codes[hex_code] = colour[1]
            return render_template("index.html", form=form, top_hex_codes=top_hex_codes, number_of_pixels=number_of_pixels, img_file_name=f"images/{filename}")
            # for pixel in image_uploaded.getdata():
            #     print(pixel)
                # you will see 4 values in the tuple, the fourth value is the alpha,
                # 255 means fully opaque, 0 means transparent
                # to avoid this and ensure we only get 3 channels, we can change the mode of the image, simply by doing .convert("RGB")

    return render_template("index.html", form=form, top_hex_codes=None, number_of_pixels=None)

if __name__ == "__main__":
    app.run(debug=True)