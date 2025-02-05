**About the Project**
  This project combines deep learning and explainable AI techniques to develop a robust and interpretable pneumonia detection model using chest X-ray images. By integrating a pre-trained VGG16 model and Grad-CAM (Gradient-weighted Class Activation Mapping), the solution provides transparent visual insights into the decision-making process, enhancing trust and usability in clinical settings.
**About the Dataset**
  The dataset is organized into 3 folders (train, test, val) and contains subfolders for each image category (Pneumonia/Normal). There are 5,863 X-Ray images (JPEG) and 2 categories (Pneumonia/Normal).
  Chest X-ray images (anterior-posterior) were selected from retrospective cohorts of pediatric patients of one to five years old from Guangzhou Women and Children’s Medical Center, Guangzhou. All chest X-ray imaging was performed as part of patients’ routine clinical care.
  For the analysis of chest x-ray images, all chest radiographs were initially screened for quality control by removing all low quality or unreadable scans. The diagnoses for the images were then graded by two expert physicians before being cleared for training the AI system. In order to account for any grading errors, the evaluation set was also checked by a third expert.
**Key Features**
*Data Preparation:*
  -Loaded and preprocessed X-ray image data using libraries like glob, numpy, and pandas.
  -Structured datasets for training, testing, and validation through organized DataFrames.
  -Applied image augmentation and preprocessing functions for better generalization.
*Model Architecture:*
  -Utilized the VGG16 model for transfer learning, frozen its layers, and adapted it for binary classification (normal vs. pneumonia).
  -Added fully connected layers to fine-tune the model for pneumonia detection tasks.
*Training Process:*
  -Achieved an impressive training accuracy of ~99.82% and validation accuracy of ~96.13%.
  -Loss monitoring indicated stable performance with limited overfitting concerns.
*Explainability with Grad-CAM:*
  -Implemented Grad-CAM to generate heatmaps highlighting lung regions that influenced the model’s predictions.
  -Used the technique to validate model focus areas and detect potential flaws in training data.
*Performance Metrics:*
  -Monitored and visualized loss and accuracy trends during training and validation.
  -Ensured consistent validation performance across multiple epochs with generalization capability.

**Ethical and Social Implications**
  The project addresses key ethical concerns in AI, such as data bias, legal compliance, and transparency. Grad-CAM visual explanations contribute to fostering trust between AI systems and clinicians, while transfer learning optimizes resource usage and reduces computational requirements.

This repository showcases a comprehensive approach to developing transparent and efficient AI models for medical applications.
