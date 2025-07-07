import requests
from PIL import Image
from io import BytesIO  # Use BytesIO for efficient in-memory image handling

image_url = "https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg?cs=srgb&dl=pexels-anjana-c-169994-674010.jpg&fm=jpg"
filename = "img.jpg"

response = requests.get(image_url, stream=True)  # Use stream=True for large files
response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

image = Image.open(BytesIO(response.content))
image.save(filename)