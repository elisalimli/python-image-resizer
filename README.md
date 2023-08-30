# A simple image resizing service

## How it works
Accepts HTTP GET or POST, with two parameters:
* url: URL of image
* size: size of a square bounding box, in pixels
Returns the resized image, or an image of the original size if size is less than the original size
