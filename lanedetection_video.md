# Lane Detection on Video

This script performs lane detection on a video stream using OpenCV and NumPy. It processes each frame of the video to detect and highlight lane lines, providing a real-time visualization of lane detection.

## Overview
- **Input:** A video file 
[![Video thumbnail](images/test_video_01_thumbnail.png)](video/test_video_01.mp4)

- **Output:** The video frames with detected lane lines overlaid, displayed in a window
[![Video thumbnail](images/test_video_01_detection_thumbnail.png)](video/output_lanes.mp4)

## Main Steps
1. **Video Loading:** Opens the video file and processes it frame by frame.
2. **Image Snipping:** Crops the region of interest from each frame to focus on the road area.
3. **Masking:** Applies a polygonal mask to isolate the lane area.
4. **Thresholding:** Highlights white and yellow lane markings using color masks in HSV color space.
5. **Blurring:** Applies Gaussian blur to reduce noise and improve edge detection.
6. **Edge Detection:** Uses the Canny algorithm to find edges in the frame.
7. **Line Detection:** Uses the Hough Transform to detect lines corresponding to lane markers.
8. **Line Averaging and Drawing:** Averages detected lines using a moving average for stability, then draws the left and right lane lines on the frame.
9. **Display:** Shows the processed frame with detected lanes in a window. Press 'q' to quit early.

## Functions
- `snip_image(image)`: Crops the lower part of the frame to focus on the road.
- `mask_image(image)`: Applies a polygonal mask to the frame to isolate the lane area.
- `thresh_image(image)`: Applies color and grayscale thresholding to highlight lane lines.
- `blur_image(image)`: Applies Gaussian blur to the frame.
- `edge_image(image)`: Detects edges using the Canny algorithm.
- `lined_image(image)`: Detects lines using the Hough Transform.
- `show_line(lines, snip, color)`: Draws averaged lane lines on the frame using a moving average for stability.
- `moving_average(snip, ptsL, ptsR)`: Maintains a moving average of detected lane line points for smoother visualization.
- `main()`: Orchestrates the lane detection pipeline for each video frame and displays the result.

## Usage
Run the script directly:

```bash
python lanedetection_video.py
```

A window will display the video with detected lane lines. Press 'q' to exit before the video ends.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- NumPy
- imutils

## Notes
- The script uses a moving average to stabilize lane line detection across frames.
- The region of interest and mask polygon are hardcoded for the sample video and may need adjustment for other videos or camera perspectives.
- The script is designed for demonstration and may require parameter tuning for different lighting or road conditions.

---
Author: Ian Edmundson
Date: August 2025
