import cv2
import numpy as np

def apply_gaussian_noise_removal(frame, kernel_size):
    return cv2.GaussianBlur(frame, kernel_size, 0)

def apply_canny_edge_detection(frame, threshold1, threshold2):
    return cv2.Canny(frame, threshold1, threshold2)

def apply_digital_negative(frame):
    return 255 - frame

def apply_high_pass_filter(frame, kernel_size):
    gaussian_blur = cv2.GaussianBlur(frame, kernel_size, 0)
    return frame - gaussian_blur

def apply_laplacian_filter(frame):
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    return cv2.convertScaleAbs(laplacian)

def apply_averaging_filter(frame, kernel_size):
    return cv2.blur(frame, kernel_size)

def apply_prewitt_filter(frame):
    kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
    return cv2.filter2D(frame, -1, kernel)

def apply_sobel_filter(frame):
    sobel_x = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.magnitude(sobel_x, sobel_y)
    return cv2.convertScaleAbs(sobel)

def apply_sepia_filter(frame):
    sepia_kernel = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    return cv2.transform(frame, sepia_kernel)

def apply_emboss_filter(frame):
    kernel = np.array([[-2, -1, 0],
                       [-1,  1, 1],
                       [ 0,  1, 2]])
    return cv2.filter2D(frame, -1, kernel)

def apply_sharpen_filter(frame):
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])
    return cv2.filter2D(frame, -1, kernel)

# Use the IP camera stream
cap = cv2.VideoCapture('http://192.168.0.104:8080/video')

if not cap.isOpened():
    print("Error opening IP camera stream")
    exit()

# Get the screen resolution
screen_width = 1920  # Adjust this to your screen width
screen_height = 1080  # Adjust this to your screen height

# Define the reduction factor
reduction_factor = 0.7

# Adjust the screen size proportionally
adjusted_screen_width = int(screen_width * reduction_factor)
adjusted_screen_height = int(screen_height * reduction_factor)

cv2.namedWindow('Filters', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Filters', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error reading frame from IP camera")
        break

    kernel_size = (5, 5)
    threshold1, threshold2 = 100, 200

    filters = [
        ("Original", frame),
        ("Gaussian Noise Removal", apply_gaussian_noise_removal(frame, kernel_size)),
        ("Digital Negative", apply_digital_negative(frame)),
        ("Canny Edge Detection", apply_canny_edge_detection(frame, threshold1, threshold2)),
        ("High Pass Filter", apply_high_pass_filter(frame, kernel_size)),
        ("Laplacian Filter", apply_laplacian_filter(frame)),
        ("Averaging Filter", apply_averaging_filter(frame, kernel_size)),
        ("Prewitt Filter", apply_prewitt_filter(frame)),
        ("Sobel Filter", apply_sobel_filter(frame)),
        ("Sepia Filter", apply_sepia_filter(frame)),
        ("Emboss Filter", apply_emboss_filter(frame)),
        ("Sharpen Filter", apply_sharpen_filter(frame))
    ]

    rows, cols = 3, 4
    cell_height, cell_width = adjusted_screen_height // rows, adjusted_screen_width // cols

    # Create a blank canvas to display all filters
    canvas = np.zeros((adjusted_screen_height, adjusted_screen_width, 3), dtype=np.uint8)

    for i, (name, filtered_frame) in enumerate(filters):
        row, col = divmod(i, cols)
        y, x = row * cell_height, col * cell_width

        if filtered_frame.ndim == 2:
            filtered_frame = cv2.cvtColor(filtered_frame, cv2.COLOR_GRAY2BGR)

        resized_frame = cv2.resize(filtered_frame, (cell_width, cell_height))
        
        # Create a border around each filter
        cv2.rectangle(resized_frame, (0, 0), (cell_width-1, cell_height-1), (255, 255, 255), 2)
        
        # Add filter name in bright red
        cv2.putText(resized_frame, name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Place the resized frame onto the canvas
        canvas[y:y+cell_height, x:x+cell_width] = resized_frame

    # Display the canvas in a single window
    cv2.imshow('Filters', canvas)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
