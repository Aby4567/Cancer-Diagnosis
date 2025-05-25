# Advanced Multi-Class Cancer Diagnosis Using Deep Learning

## Project Overview

Cancer is a leading cause of death globally, and early diagnosis is key to improving patient survival. Traditional diagnostic methods such as histopathological analysis and manual imaging interpretation are time-consuming, prone to human error, and require expert intervention.

This project introduces an advanced deep learning-based system for **multi-class cancer diagnosis**, focusing on classifying **skin cancer**, **leukemia (blood cancer)**, and **lung cancer** using medical images. The proposed solution leverages **EfficientNet**, a state-of-the-art Convolutional Neural Network (CNN), along with transfer learning and robust preprocessing techniques to automate and enhance diagnostic accuracy.

---

## Theoretical Concepts

### 1. Deep Learning

Deep learning is a subfield of machine learning inspired by the structure and function of the brain’s neural networks. In this project, it is used for image classification by automatically learning hierarchical feature representations from medical images.

### 2. Convolutional Neural Networks (CNN)

CNNs are specially designed neural networks used for image data. They are efficient in detecting patterns, edges, textures, and shapes from images, which are crucial in identifying cancerous regions in tissues.

### 3. Transfer Learning

Transfer learning allows the reuse of a pre-trained model (EfficientNet in this case) on a new but related task. This helps save time and computation while improving accuracy, especially when medical image datasets are limited.

### 4. EfficientNet

EfficientNet is a family of CNNs that balances model depth, width, and resolution using a compound scaling method. It provides high accuracy with low computational cost, making it suitable for real-time medical diagnosis.

### 5. Image Preprocessing

- **Resizing** to 256x256 pixels for uniform input.
- **Median Filtering** to remove noise such as salt-and-pepper artifacts.
- **Normalization** to standardize pixel intensities.
- **Contrast Enhancement** to improve visibility of subtle cancerous features.

---

## Workflow

1. **Image Acquisition**: Collecting labeled datasets of lung, skin, and blood cancer images from public repositories.
2. **Preprocessing**: Enhancing image quality through noise removal and resizing.
3. **Model Training**: Fine-tuning EfficientNet on preprocessed images.
4. **Classification**: Predicting the type of cancer based on trained model outputs.
5. **Diagnosis Output**: Providing interpretable results and treatment suggestions for each cancer class.

---

## Advantages

- Supports early diagnosis and timely treatment.
- Reduces reliance on manual pathology interpretation.
- High accuracy across multiple cancer types in a single platform.
- Automated and scalable—can be used in low-resource settings.
- Enhances diagnostic consistency and reduces human error.

---

## Results Summary

| Cancer Type | Accuracy | Comments |
|-------------|----------|----------|
| Blood       | 98%      | Excellent performance with minimal misclassification |
| Lung        | 85%      | Good accuracy, but needs improvement on class balance |
| Skin        | 70%      | Moderate performance; could improve with more data and augmentation |

---

## Future Enhancements

- Integrating patient metadata such as genetic profiles and medical history.
- Applying Explainable AI (XAI) techniques like Grad-CAM to visualize model decisions.
- Expanding to other types of cancer (e.g., breast, brain).
- Deploying the system on cloud platforms for global accessibility.

---

## Technologies Used

- **Programming Language**: Python
- **Deep Learning Framework**: TensorFlow, Keras
- **Model Architecture**: EfficientNetB3
- **Web Framework**: Flask
- **Database**: MySQL
- **Frontend**: HTML, CSS, Bootstrap

---

## Dataset Links

- [Blood Cancer Dataset](https://www.kaggle.com/datasets/mohammadamireshraghi/blood-cell-cancer-all-4class)
- [Lung Cancer Dataset](https://www.kaggle.com/datasets/yusufdede/lung-cancer-dataset)
- [Skin Cancer Dataset](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000)

---

## Authors

- **Amirthasri A**
- **Harinisri M**
- **Rajarajeshvari V**
- **Abinaya K**

Under the guidance of:
- **Ms. R. Valampuranayaki, M.E.** – Project Guide
- **Dr. K. Krishnakumari, Ph.D.** – Head of Department, IT

A.V.C. College of Engineering, Mayiladuthurai  
Affiliated to Anna University, Chennai

---

## License

This project is intended for academic and research use only.
