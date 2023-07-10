# ECG Report Analysis System

This project implements a deep learning model for predicting cardiac arrhythmia based on raw electrocardiogram (ECG) data. The model is trained to classify ECG reports into five categories.

- Class 0: Normal ECG
- Class 1: Supraventricular ectopic beats
- Class 2: Ventricular ectopic beats
- Class 3: Fusion Beats
- Class 4: Unknown Beats

## Research Paper

The research paper associated with this project can be found at [IEEE Xplore](https://ieeexplore.ieee.org/document/9645917).

## Copyright

This project is protected by copyright. The registration details are as follows:

- Registration Number: L-112342/2022
- Copyright Office: [https://copyright.gov.in/](https://copyright.gov.in/)

## Background

An electrocardiogram (ECG) is a simple test that can be used to check electrical activity. ECG is a fundamental tool in the everyday practice of clinical medicine, with more than 300 million ECGs obtained annually worldwide.

## Application

The application is built using the Flask framework. It provides a web interface to upload an image of an ECG report and obtain analysis results.

## Folder Structure

- `static/`: Contains static files such as CSS and JavaScript.
- `templates/`: Contains HTML templates for the web application.
- `app.py`: The main Flask application file.
- `ecg_model.h5`: The trained deep learning model for ECG classification.

## Prerequisites

Make sure you have the following packages installed:

- Flask
- TensorFlow
- OpenCV (cv2)
- PIL (Python Imaging Library)
- pylsd.lsd

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/ResearchPaperECG.git

```

2. Navigate to the project directory:

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:

```bash
python app.py

```

2. Open in your browers in a localhost ip address.

3. Upload an image of an ECG report.

4. Click the "Submit" button to process the image and obtain the analysis results.

5. The analysis results, including the predicted ECG class, will be displayed on the page.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
Please make sure to update the placeholders (YourUsername, project names, links, etc.) with your actual project information.

Let me know if you need any further assistance!
