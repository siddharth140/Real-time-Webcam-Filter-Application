# Real-Time Image Filter Application

## Description

This Python application applies various image filters to a live video stream from a smartphone camera. It uses OpenCV to process the video feed and display multiple filtered versions of the stream simultaneously. The application showcases 12 different image filters, including Gaussian noise removal, edge detection, and color transformations.

## Features

- Real-time video processing from a smartphone camera
- 12 different image filters applied simultaneously
- Fullscreen display with a grid layout of all filters
- Easy-to-read filter names and bordered displays

## Filters Included

1. Original (unfiltered)
2. Gaussian Noise Removal
3. Digital Negative
4. Canny Edge Detection
5. High Pass Filter
6. Laplacian Filter
7. Averaging Filter
8. Prewitt Filter
9. Sobel Filter
10. Sepia Filter
11. Emboss Filter
12. Sharpen Filter

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy
- IP Webcam app (on your smartphone)

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required Python libraries: pip install opencv-python numpy
3. Download and install the IP Webcam app on your smartphone:
- For Android: [IP Webcam on Google Play Store](https://play.google.com/store/apps/details?id=com.pas.webcam)
- For iOS: Search for a similar app in the App Store

## Setting Up IP Webcam

1. Install the IP Webcam app on your smartphone.
2. Open the app and tap on "Start server" to create a new server.
3. The app will generate a URL similar to `http://192.168.0.104:8080/video`.
4. Make note of this URL as you'll need it for the Python script.

## Usage

1. Replace the IP camera URL in the Python script with the one generated by your IP Webcam app:
   ```python
   cap = cv2.VideoCapture('http://192.168.0.104:8080/video')
2. Run the Python script: python your_script_name.py
3. A fullscreen window will appear showing all 12 filters applied to the live video stream.
4. Press 'q' to quit the application.

## Customization

- Adjust the screen_width and screen_height variables to match your display resolution.
- Modify the reduction_factor to change the size of the display window.
- Add or remove filters by modifying the filters list in the main loop.

## Troubleshooting

- Ensure your computer and smartphone are on the same Wi-Fi network.
- If the connection fails, check the IP address in the URL provided by the IP Webcam app.
- Make sure no firewall is blocking the connection between your computer and smartphone.

## Contributing

Contributions to improve the application are welcome. Please feel free to fork the repository, make changes, and submit a pull request.

## Contact

For any queries or further information, please contact:
Siddharth Vaddepalli
Email: siddharth.vaddepalli@gmail.com


## Acknowledgments

- Thanks to the OpenCV community for providing powerful computer vision tools.
- Appreciation to the developers of the IP Webcam app for enabling easy mobile camera streaming.
- Gratitude to all open-source contributors whose work has made this project possible.
- Special thanks to the Python community for their continuous support and resources.
- Acknowledgment to image processing pioneers whose algorithms form the basis of many filters used in this application.
- Thanks to all users and testers who provide feedback and help improve this application.
