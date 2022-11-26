<p>
  <h1 align="center"><b>Web Phishing Detection (IBM-Project-52622-1661014579) </h1>
</p>

<p>
  <h3 align="center"> Category: Applied Data Science and Machine Learning, Team ID : PNT2022TMID52622</h3>

</p>
  <img align="center" alt="phishing" src="https://user-images.githubusercontent.com/62670994/204077078-3fcbe247-223f-427b-946f-577ac49e638d.png">


## Objective

A phishing website is a common social engineering method that mimics trustful uniform resource locators (URLs) and webpages. The objective of this project is to train machine learning models on the dataset given to predict phishing websites. Both phishing and benign URLs of websites are gathered to form a dataset and from them required URL and website content-based features are extracted. The performance level of each model is measured and compared.

## Data Collection and Analysis

The given dataset dataset_website.csv contains both phishing and benign URLs of websites with various website content-based features. 

The above mentioned dataset is uploaded to the 'final deliverables/data' folder of this repository.

From data distribution graph and correlation matrix, we can conclude that the 16 of the given features do not have much impact on the result. So they are removed from further processing. The final set of features that are used to build the model are shown in the figure below.

![final_features](https://user-images.githubusercontent.com/64459672/199578614-f8cb7f81-9da0-43a8-b6eb-5381970a9768.png)


## Models & Training

Before stating the ML model training, the data is split into 80-20 i.e., 8844 training samples & 2211 testing samples. From the dataset, it is clear that this is a supervised machine learning task.

This data set comes under classification problem, as the input URL is classified as phishing (1) or legitimate (0). The supervised machine learning models (classification) considered to train the dataset in this project are:

- Decision Tree
- Random Forest
- XGBoost
- Support Vector Machines

The elaborate details of the models & its training are mentioned in Phishing_Website_Detection.ipynb

## End Results

XGBoost Classifier has highest model performance of 90.2%. So the model is saved to the file XGBoostClassifier.pickle.dat and is used as our primary prediction model by deploying it in IBM WATSON STUDIO

## Demo Video:

# [Web Phishing Detection (VIDEO LINK)](https://drive.google.com/drive/folders/1HwRFoYKWZ0sMZMM33wmChhGsmlhcxixY?usp=sharing)

## Team Members (Team ID : PNT2022TMID52622)
* Sanjeev Karthick K 

* Sai Nandhan P

* Muhammed Rameez M

* Yashwanth BT

### WEBSITE OUTPUT SAMPLE 
![WEB PHISHING SAMPLE SITE](https://user-images.githubusercontent.com/62670994/204072600-bae0d8f4-c1b3-4667-b2f1-56e0fc572f12.png)

### SAFE URL
![screencapture-file-C-Users-vijayalakshmi-Downloads-Module-1-Phishing-website-detection-main-template-index-html-2022-11-26-10_19_54](https://user-images.githubusercontent.com/62670994/204074989-baed8729-180b-495a-85b4-bcfcde1b4617.png)

### MALICIOUS URL
![Screenshot (961)](https://user-images.githubusercontent.com/62670994/204077748-0ffbcb42-e050-46e5-8874-ade81454c2b7.png)


