# Python Image Resizer

This is a simple Python application that accepts image URLs, creates thumbnails, and serves the resized images using Flask.

## Installation

Follow these steps to set up the project on your local environment:

1. Clone the project repository:

    ```bash
    git clone https://github.com/elisalimli/python-image-resizer.git
    ```

2. Navigate to the project's folder:

    ```bash
    cd python-image-resizer
    ```

3. Make sure you have Python 3 installed on your system.

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the program, execute the following command:

```bash
python3 image_resizer.py
```

This will start the Flask application, and you'll be able to access it through your web browser or by making HTTP requests.

## Running with Docker
Alternatively, you can use Docker to run the application in a container. Follow these steps:

1. Build the docker image:

    ```bash
    docker build -t image-resizer .
    ```

2. Run the docker container:

    ```bash
    docker run --rm -it -p 4000:4000 image-resizer
    ```

This will build the image and run the application within a Docker container. The application will be accessible at http://localhost:4000.


## Usage Example
After running the application, you can use a tool like curl to make HTTP requests to the endpoints and test the image resizing functionality.

For example, to create a thumbnail of an image, use the following command:

```bash
curl -X GET "http://localhost:4000/?size=256&url=http://example.com/"
```