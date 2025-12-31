# Brain Tumor Detection

A deep learning project for detecting brain tumors using ResNet101 with transfer learning. The model classifies brain MRI scans into four categories: glioma, meningioma, no tumor, and pituitary tumors.

## Project Overview

- **Model**: ResNet101 (pre-trained on ImageNet, fine-tuned for brain tumor classification)
- **Test Accuracy**: 70.25% (after 10 epochs)
- **Categories**:
  - `glioma` - Grade II/III astrocytoma
  - `meningioma` - Meningeal tumor
  - `notumor` - Normal brain scan
  - `pituitary` - Pituitary adenoma

## Setup Instructions

### 1. Install Dependencies

Install all required packages using the requirements.txt file:

```bash
pip install -r requirements.txt
```

This will install:
- **tensorflow** - Deep learning framework
- **numpy** - Numerical operations
- **matplotlib** - Visualization
- **seaborn** - Statistical plots
- **scikit-learn** - Metrics and evaluation
- **gdown** - Download files from Google Drive

### 2. Download Pre-trained Model Weights

The project includes a script to download the pre-trained model weights from Google Drive:

```bash
python loadModelWeights.py
```

This script will:
- Check if the model weights file (`my_model_weights.keras`) already exists
- If not found, download the pre-trained ResNet101 model from Google Drive
- Save it as `my_model_weights.keras`

**Note**: Ensure you have a stable internet connection for the download.

## Project Structure

```
├── brainTumor.ipynb              # Main notebook with model training
├── loadModelWeights.py           # Script to download pre-trained weights
├── ResNetFineTuned.keras         # Trained model (Keras format)
├── ResNetFineTuned.h5            # Trained model (HDF5 format)
├── requirements.txt              # Python dependencies
├── README.md                      # This file
└── archive/
    ├── Training/                 # Training dataset
    │   ├── glioma/
    │   ├── meningioma/
    │   ├── notumor/
    │   └── pituitary/
    └── Testing/                  # Testing dataset
        ├── glioma/
        ├── meningioma/
        ├── notumor/
        └── pituitary/
```

## Usage

### Load and Use the Pre-trained Model

```python
import tensorflow as tf

# Load the model
model = tf.keras.models.load_model('ResNetFineTuned.keras')

# Or load from HDF5 format
model = tf.keras.models.load_model('ResNetFineTuned.h5')

# Make predictions
predictions = model.predict(image_array)
```

### Training

Run the Jupyter notebook to train the model:

```bash
jupyter notebook brainTumor.ipynb
```

The notebook includes:
- Dataset loading and preprocessing
- Model architecture definition
- Training with early stopping
- Evaluation metrics and confusion matrix
- Learning curves visualization

## Model Performance

- **Test Loss**: ~0.78
- **Test Accuracy**: 70.25%
- **Best Classification**: No tumor and pituitary tumors
- **Needs Improvement**: Meningioma classification

## Future Improvements

- Error analysis on misclassified meningioma scans
- Model architecture refinement for better meningioma detection
- Data augmentation for underrepresented classes
- Hyperparameter tuning

## Requirements

- Python 3.7+
- See `requirements.txt` for all dependencies

## Notes

- Images are resized to 224×224 pixels
- Normalization: pixel values scaled to [0, 1]
- Batch size: 32
- Training epochs: 10 (with early stopping)
