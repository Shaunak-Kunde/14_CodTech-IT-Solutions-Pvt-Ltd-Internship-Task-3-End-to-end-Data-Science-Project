# CODTECH Internship – Task 2: Deep Learning Project

This project is part of my CODTECH Virtual Internship under Data Science.
The goal is to build a deep learning model for image classification using the Plant Disease dataset from Kaggle.

# Plant Disease Classification 🌱

This project implements a Deep Learning model to classify plant diseases using the PlantVillage Dataset
.
The model is built with TensorFlow/Keras and demonstrates transfer learning (MobileNetV2) for efficient training.

# 🚀 Project Workflow
1. Dataset Access via Kaggle API

# Dataset: Plant Disease Dataset
(Kaggle: https://www.kaggle.com/datasets/emmarex/plantdisease)

Downloaded programmatically using Kaggle API (emmarex/plantdisease), not uploaded to GitHub due to size (~342 MB).

2. Data Preprocessing

Image resizing (128x128) & normalization.

Train-validation split using validation_split in ImageDataGenerator (no separate test folder required).

Data augmentation: rotation, zoom, flips, brightness adjustments to improve generalization.

3. Model Development

Transfer learning using MobileNetV2 (pre-trained on ImageNet).

Added custom dense layers for classification of plant disease categories.

Optimized with Adam, categorical crossentropy loss.

4. Training & Evaluation

Trained on GPU for efficiency.

Metrics: Accuracy & Loss.

Evaluated on validation set using val_generator.

Predicted sample images from validation set.

5. Visualization

Training vs Validation Accuracy & Loss curves.

Sample predictions with actual vs predicted labels.

📊 Model Visualizations

Accuracy & Loss graphs during training.

Example validation images with predicted labels.

🛠️ Tools & Libraries

Python 3.10+

TensorFlow / Keras – Deep Learning framework

NumPy – Numerical operations

Matplotlib / Seaborn – Visualization

Kaggle API – Dataset download

📂 Project Structure
Task-2 Deep Learning Project/
│── plant_disease_dataset/           # Downloaded via Kaggle API
│── deep_learning_plant.ipynb  # Main Notebook
│── requirements.txt                 # Required Python libraries
│── readme.md                        # Project documentation

📊 Summary & Insights

The Plant Disease dataset contains multiple classes of diseased & healthy plant leaves.

Data Augmentation helped reduce overfitting and improved model generalization.

Transfer learning with MobileNetV2 achieved high validation accuracy, demonstrating effective learning of disease patterns.

Sample predictions show the model correctly classifies most plant categories.

✅ Deliverables

Trained CNN model → plant_disease_cnn.h5

Accuracy & Loss plots

Sample predictions with visualization

⚠️ Note

The dataset (~342 MB) is not uploaded to GitHub due to size limits.

Use Kaggle API to download the dataset before running the notebook.

validation_split is used instead of separate test folder for evaluation.

This concludes Task-2: Deep Learning Project for the CodTech Internship 🚀

👨‍💻 Developed by: Shaunak Damodar Sinai Kunde