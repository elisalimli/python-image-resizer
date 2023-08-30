import os
from PIL import Image
from flask import Flask, request, send_file
from io import BytesIO
from urllib.request import Request, urlopen

app = Flask(__name__)
port = int(os.getenv("PORT", 4000))
thumbSize = (256, 256)


@app.route("/", methods=["POST", "GET"])
def thumb():
    size = request.args.get("size")
    if size is None:
        size = thumbSize
    else:
        size = int(size), int(size)
    url = request.args.get("url")
    print(f'Processing URL "{url}" now ...', url)

    req = Request(
        url=url,
        headers={"User-Agent": "Mozilla/5.0"},
    )

    data = urlopen(req).read()
    img = Image.open(BytesIO(data))
    img.thumbnail(size)
    img_io = BytesIO()
    img.save(img_io, "JPEG", quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype="image/jpeg")


@app.route("/status")
def test():
    return "STATUS_OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, threaded=True, debug=False)
