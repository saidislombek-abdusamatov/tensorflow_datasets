# TensorFlow Datasets Image Classification with Streamlit

This repository showcases the power of pre-trained TensorFlow models for image classification tasks using popular datasets: Deep Weeds, EuroSAT, and SVHN (Street View House Numbers). Utilizing Streamlit, a Python library for building interactive web applications, this project provides a user-friendly interface for uploading images and obtaining predictions from the models.

## Models Used

- **Deep Weeds**: Classifies plants into different categories (e.g., Chinee apple, Lantana, etc.).
- **EuroSAT**: Identifies land use and land cover classes from satellite images (e.g., AnnualCrop, Forest, etc.).
- **SVHN Cropped**: Recognizes cropped digits from street view images (digits 0-9).

## How to Use

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/saidislombek-abdusamatov/tensorflow_datasets.git
   ```

2. **Install Dependencies:**

   ```bash
   pip install tensorflow streamlit opencv-python pandas numpy Pillow
   ```

3. **Run the Streamlit App:**

   ```bash
   streamlit run app.py
   ```

   This command will start the Streamlit web application locally. You can access the app in your browser at `http://localhost:8501`.

## Features

### Image Classification:

1. **Upload Image:**
   - Click on the "Upload Image" button to select an image (PNG, JPG, or JPEG format).
   - The uploaded image will be displayed below the button.

2. **Select Model:**
   - Choose the model you want to use from the dropdown menu: Deep Weeds, EuroSAT, or SVHN Cropped.

3. **Prediction:**
   - Click the "Predict!" button to see the model's prediction based on the uploaded image.
   - The predicted class label will be displayed along with a bar chart showing the model's confidence scores for each class.

## Models and Classes

- **Deep Weeds Classes:** Chinee apple, Lantana, Parkinsonia, Parthenium, Prickly acacia, Rubber vine, Siam weed, Snake weed, Negative
- **EuroSAT Classes:** AnnualCrop, Forest, HerbaceousVegetation, Highway, Industrial, Pasture, PermanentCrop, Residential, River, SeaLake
- **SVHN Cropped Classes:** Digits 0-9
