# Rice Leaf Disease Classification using Deep Learning

## Overview
This project presents a deep learning-based approach for classifying rice leaf diseases from images. The model identifies whether a leaf is healthy or affected by diseases such as bacterial leaf blight, brown spot, or leaf smut.

The system uses image preprocessing, data augmentation, and transfer learning to achieve reliable performance on a relatively small dataset.

---

## Objectives
- Perform image preprocessing and normalization  
- Apply data augmentation to improve generalization  
- Train a deep learning model using transfer learning  
- Evaluate model performance using accuracy, precision, and recall  

---

## Dataset
The dataset consists of rice leaf images categorized into the following classes:

- Healthy  
- Bacterial leaf blight  
- Brown spot  
- Leaf smut  

Multiple datasets were combined and cleaned to improve diversity and model performance.

**Note:**  
The dataset is not included in this repository due to size constraints.  
You can download it from Kaggle and follow the preprocessing steps.

---

## Dataset Sources

The dataset used in this project is a combination of multiple publicly available sources:

1. Rice Leaf Diseases Dataset  
   https://www.kaggle.com/datasets/vbookshelf/rice-leaf-diseases  

2. Rice Leaf Disease Dataset  
   https://www.kaggle.com/datasets/shayanriyaz/riceleafs  

3. PlantVillage Dataset (for healthy images)  
   https://www.kaggle.com/datasets/emmarex/plantdisease  

The datasets were merged, cleaned, and restructured into training, validation, and test sets.

## Project Structure
```
Rice-Leaf-Disease-Classification/
│
├── src/
│   ├── train.py
│   ├── split.py
│   ├── data_augmentation.py
│   ├── merge.py
│   ├── clean.py
│
├── model/
│   └── rice_model.h5   
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Methodology

### 1. Data Preprocessing
- Resized all images to 224×224  
- Normalized pixel values to [0,1]  

### 2. Data Augmentation
- Rotation  
- Zoom  
- Shear  
- Horizontal flip  

### 3. Model Architecture
- Base Model: MobileNetV2  
- Custom Layers:
  - Global Average Pooling  
  - Batch Normalization  
  - Dense Layer 
  - Dropout  
  - Softmax Output Layer  

### 4. Training Strategy
- Phase 1: Train classifier with frozen base layers  
- Phase 2: Fine-tune top layers  
- Optimizer: Adam  
- Loss Function: Categorical Crossentropy  
- Regularization: Early stopping and learning rate reduction  

---

## Results

- Test Accuracy: **84.4%**  
- The model demonstrates good generalization

---

## Evaluation Metrics

The model was evaluated on the test dataset using standard classification metrics.

### Classification Report
```

| Class                    | Precision|  Recall|  F1-score|
|--------------------------|----------|--------|----------|
| Bacterial leaf blight    | 0.85     | 0.83   | 0.84     |
| Brown spot               | 0.86     | 0.85   | 0.85     |
| Healthy                  | 0.83     | 0.86   | 0.84     |
| Leaf smut                | 0.84     | 0.83   | 0.83     |
```

---

### Overall Performance

- **Accuracy:** 84.4%  
- **Macro Average F1-score:** 0.84  
- **Weighted Average F1-score:** 0.84  

---

### Interpretation

- The model demonstrates balanced performance across all classes.  
- Precision and recall values indicate that the model is able to correctly identify most disease cases while maintaining low false positives.  
- The close alignment between training, validation, and test accuracy confirms good generalization with minimal overfitting.  

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Prepare dataset
- Download dataset from Kaggle
- Organize into:
```
dataset
 ├── train/
 ├── val/
 └── test/
```
### 3. Train model
  ```
  python src/train.py
  ```
### 4. Evaluate model
  ```
  python src/test.py
  ```

---

### Author
Pritish Dutta
