# Real-time Webcam Filter Application

## Overview

This Python script showcases the power of real-time image processing by applying various filters to webcam input using OpenCV. It's an interactive application that demonstrates the visual effects of different image processing techniques, allowing users to see multiple filtered versions of their webcam feed simultaneously.

## Features

The application applies the following 12 filters in real-time:

1. **Original**: Unmodified webcam feed
2. **Gaussian Noise Removal**: Reduces image noise using Gaussian blur
3. **Digital Negative**: Inverts the colors of the image
4. **Canny Edge Detection**: Highlights edges in the image
5. **High Pass Filter**: Emphasizes high-frequency components (edges and details)
6. **Laplacian Filter**: Detects edges and enhances image sharpness
7. **Averaging Filter**: Smooths the image by averaging neighboring pixels
8. **Prewitt Filter**: Detects edges using the Prewitt operator
9. **Sobel Filter**: Detects edges using the Sobel operator
10. **Sepia Filter**: Applies a warm, brownish tone to the image
11. **Emboss Filter**: Creates a 3D-like effect by highlighting edges
12. **Sharpen Filter**: Enhances image details and edges

## Requirements

To run this application, you'll need:

- Python 3.x
- OpenCV (`cv2`)
- NumPy

You can install the required packages using pip: pip install opencv-python numpy

## Installation

1. Clone this repository or download the script file.
2. Ensure you have the required packages installed.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script using Python: python webcam_filters.py
4. The application will open your default webcam and display a window with all 12 filters applied in real-time.
5. To exit the application, press 'q' on your keyboard.

## How It Works

1. The script captures video from the default webcam using OpenCV.
2. For each frame captured:
   - It applies all 12 filters to the frame.
   - Resizes each filtered image to fit in a grid layout.
   - Adds a border and label to each filtered image.
   - Combines all filtered images into a single display canvas.
3. The resulting canvas is displayed in a window, updating in real-time.

## Customization

You can easily customize the application:

- **Screen Resolution**: Adjust the `screen_width` and `screen_height` variables to match your screen resolution.
- **Window Size**: Modify the `reduction_factor` to change the size of the display window.
- **Filters**: Add, remove, or modify filters by changing the `filters` list in the main loop.
- **Grid Layout**: Alter the `rows` and `cols` variables to change the grid layout of the filters.
- **Filter Parameters**: Many filters have adjustable parameters (e.g., kernel sizes, thresholds) that you can tweak for different effects.

## Performance Considerations

- The application processes multiple filters in real-time, which can be computationally intensive.
- Performance may vary depending on your hardware capabilities.
- If you experience lag, try reducing the number of filters or the resolution of the webcam feed.

## Troubleshooting

- **Webcam not detected**: Ensure your webcam is properly connected and not being used by another application.
- **ImportError**: Make sure you've installed all required packages (`opencv-python` and `numpy`).
- **Performance issues**: Try closing other applications or reducing the number of active filters.

## Future Enhancements

- Add user interface controls to toggle filters on/off.
- Implement more advanced filters (e.g., face detection, background removal).
- Allow users to save filtered images or video.
- Optimize performance for smoother real-time processing.

## Author

Siddharth Vaddepalli

## Contact

For any questions or suggestions, feel free to contact the author:
Email: siddharth.vaddepalli@gmail.com

## Acknowledgments

This project uses the OpenCV library for image processing operations. Special thanks to the OpenCV community for providing such a powerful and versatile tool for computer vision tasks.
