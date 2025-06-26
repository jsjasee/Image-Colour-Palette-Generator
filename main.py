from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from forms import ImageForm
import uuid
from dotenv import load_dotenv
import os
from image_processor import ImageProcessor

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('APP_KEY')
Bootstrap5(app)
image_processor = ImageProcessor()

@app.route("/", methods=['POST','GET'])
def home():
    form = ImageForm()
    if form.validate_on_submit():

        # must use unique filenames, as only 1 global static folder when website is hosted. unique filenames ensure each user
        # sees the correct image.
        filename = f"{uuid.uuid4().hex}.png" # uuid is universal unique identifier, unlikely to repeat. the .hex just strips the '-' and returns the 32 character string instead.

        # form.data['file'].save(f"static/images/{filename}")

        # for render, need to save the file into tmp path - temp storage for img, instead of saving to the static folder and in the images folder
        tmp_path = os.path.join("/tmp", f"{uuid.uuid4().hex}.png")
        form.data['file'].save(tmp_path)

        extracted_hex, num_of_pixels = image_processor.extract_colours(form_data=form.data, tmp_path=tmp_path)
        img_url = image_processor.encode_image(tmp_path)

        return render_template("index.html", form=form, top_hex_codes=extracted_hex, number_of_pixels=num_of_pixels, img_file_link=img_url)

    return render_template("index.html", form=form, top_hex_codes=None, number_of_pixels=None)

if __name__ == "__main__":
    app.run(debug=True)