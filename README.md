# 🖼️ Image Colour Palette Generator

A Flask web app that extracts the top N most frequent colours from an uploaded image and displays them in a neat Bootstrap-styled table with hex codes and percentage breakdown.

> ✅ Now compatible with Render deployments (no file writes needed).
> 
> Hosted on render at: https://image-to-colours-converter.onrender.com/

---

## 🔧 Features

- Upload an image (PNG, JPG, WebP, etc.)
- Extract dominant colours (ignores fully transparent pixels)
- Get hex codes + frequency in image
- Base64-encoded image display (no need for persistent storage)
- Styled with Bootstrap 5

---

## 🚀 Demo

![Screenshot](static/images/screenshot.png)  
Upload your image and instantly see the most common colours it contains!

---

## 🛠️ Tech Stack

- Python 3.11
- Flask
- WTForms + Flask-Bootstrap5
- Pillow (PIL)
- `base64` for image encoding
- Deployed on [Render](https://render.com)

---

## 📦 Setup Instructions

**Clone the repository**

```bash
git clone https://github.com/yourusername/image-colour-palette-generator.git
cd image-colour-palette-generator
```

**Create a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
```
**Install dependencies**
```bash
pip install -r requirements.txt
Set up environment variable
```

**Create a .env file and add your Flask secret key:**

```env
APP_KEY=your_secret_key
```
**Run the app**
```bash
flask run
Visit http://127.0.0.1:5000 to test locally.
```

## 🧠 How It Works

1. User uploads image → Flask saves it temporarily to /tmp
2. Pillow reads pixels, filters out transparent ones
3. Colour frequency is calculated with collections.Counter
4. RGB values are converted to hex
5. Base64-encoded image string is embedded directly into the <img> tag via a data URL
6. No static file writes are needed (crucial for Render)

### 🌐 Deployment on Render
Since Render doesn’t support persistent file systems, this project avoids writing to /static

Images are base64-encoded and rendered directly in HTML using 
```html
<img src="data:image/png;base64,...">
```

**📁 Folder Structure**

```csharp
.
├── main.py
├── forms.py
├── image_processor.py
├── templates/
│   └── base.html
│   └── index.html
├── static/
│   └── styles.css
├── .env
└── requirements.txt
```

**🖼️ Add a Favicon**
1. Download a Bootstrap icon SVG or any other source
2. Save as favicon.svg in static/
3. Add to <head> in base.html:
```html
<link rel="icon" href="{{ url_for('static', filename='favicon.svg') }}" type="image/svg+xml">
```
## 📃 License
MIT License