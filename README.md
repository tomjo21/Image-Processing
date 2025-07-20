# Image-Processing


This project is a collection of Python scripts that perform various fundamental image processing operations using libraries like OpenCV (`cv2`) and NumPy. These scripts can be used for academic purposes, research, or as part of a larger computer vision system.

## 📁 Project Structure

image-processing/
│
├── contrast.py # Enhances image contrast
├── graybinary.py # Converts image to grayscale and binary
├── histo.py # Performs histogram analysis and equalization
├── inverse.py # Generates the negative of the image
├── noise.py # Adds and possibly removes noise from images
├── robert.py # Applies Robert edge detection
├── scale.py # Scales (resizes) the image
├── sizshape.py # Displays image size and shape



## ⚙️ Requirements

Make sure to install the following dependencies:

```bash
pip install opencv-python numpy
🧪 How to Use
Each script is standalone and can be executed using:


python script_name.py
For example:


python contrast.py
Ensure you have an image file in the same directory or modify the code to load your desired image.

📝 Script Descriptions
✅ contrast.py
Enhances the contrast of an image using techniques like linear stretching or histogram equalization.

⚫ graybinary.py
Converts the input image to grayscale and then applies a binary threshold to create a black-and-white version.

📊 histo.py
Plots and equalizes the histogram of an image to enhance contrast.

🔄 inverse.py
Produces a negative of the image by inverting pixel values.

📈 noise.py
Adds salt-and-pepper or Gaussian noise to the image. May include basic filtering techniques like median filtering to reduce noise.

📐 robert.py
Applies the Robert Cross operator for edge detection to highlight high spatial frequency regions.

📏 scale.py
Resizes the image using different scaling factors or interpolation methods (nearest, bilinear, etc.).

📦 sizshape.py
Displays the size (in pixels) and shape (rows, columns, channels) of the image.

👨‍💻 Author
Developed as part of an academic assignment focused on Image Processing with Python.




