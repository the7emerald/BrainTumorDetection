import gdown
import os

def download_model():
    """Download pre-trained weights from Google Drive"""
    # Upload your .keras file to Google Drive and get shareable link
    url = 'https://drive.google.com/uc?id=11V2OztXvCAm88BlPePQb347kfrEbxmGq'
    output = 'my_model_weights.keras'  # Desired output path
    
    if not os.path.exists(output):
        print("Downloading model weights...")
        gdown.download(url, output, quiet=False)
        print("Download complete!")
    else:
        print("Model weights already exist.")

if __name__ == "__main__":
    download_model()