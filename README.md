<<<<<<< HEAD
# URL_Checker
A python based deep learning project to detect malicious URLs.
<h1 style="color: 'green'">Under Devlopment<h1>

=======
# URL Classifier using NLP and Machine Learning


## Table of Contents

- [Overview](#overview)
- [Project Deployment](#project-deployment)
- [Usage](#usage)
- [Local Device Installation](#local-device-installation)
- [Database for Feedback](#database-for-feedback)
- [Training Data Collection](#training-data-collection)
- [Data Modeling and Model Architecture](#data-modeling-and-model-architecture)
- [Model Performance](#model-performance)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Overview

The URL Classifier is a powerful machine learning application designed to classify URLs as safe or malicious. In today's cybersecurity landscape, identifying potentially harmful URLs is crucial in mitigating cyber threats and phishing attacks. This project leverages both Natural Language Processing (NLP) and lexical features to create a robust URL classifier. It is hosted on Huggingface Space and utilizes the Gradio interface for user interaction.

## Project Deployment
The project is deployed on Huggingface space using gradio interface, which allows users to enter a URL and get a prediction as well as an explanation of why the prediction was made. Users can also flag false results, which will store the URL and its correct type (malicious or safe) in a MySQL database. This way, the model can learn from user feedback and improve over time.
Access the live project [here](https://huggingface.co/spaces/Munna0912/URL_CLASSIFIER).
<br>
<img width="787" alt="image" src="https://github.com/munna0912/URL_Checker/assets/75537601/5458db99-6c46-40b6-89c1-b946e640e7aa">

## Usage

To utilize this project, you have two options:

1. Visit the hosted project [here](https://huggingface.co/spaces/Munna0912/URL_CLASSIFIER) and use it through web-interface or API endpoints.
2. Run the project locally using the installation steps provided below.

Once you have access, follow these steps:

1. Input the URL you want to classify.
2. The classifier will predict whether the URL is safe or malicious.
3. If the prediction is incorrect, you can flag it for further analysis, and the URL will be stored in the database.


## Local Device Installation
### REQUIREMENTS
To use this project effectively, ensure you have the following prerequisites:

- Python 3.8 or higher
- mysql-connector-python 8.1.0
- numpy 1.23.5
- pandas 1.5.3
- scikit_learn 1.2.2
- tensorflow 2.12.0
- nltk 3.8.1
- gradio 3.40.1

### Installation
To set up this project, follow these steps:

1. Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/Munna0912/URL_CLASSIFIER.git
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On Linux/MacOS:
     ```bash
     source env/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a MySQL database(url_classifier) with the following credentials and update these details in app.py:
   - Host: localhost
   - User: root
   - Password: root
   - Database: url_classifier

6. Run the `create_table.sql` script at your MySQL server to create the table for storing URLs and their classifications.

7. Launch the web app using the following command:
   ```bash
   python app.py
   ```
## Database for Feedback

Feedback data is stored and retrieved from a MySQL database provided by [www.freesqldatabase.com](www.freesqldatabase.com). This free service offers a 5MB MySQL database for data management.

## Training Data Collection

The data for this project was meticulously collected from various sources:

**Used for Training:**

- [Malicious_phish Kaggle Dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset)
- [URLhause Phishing Links](https://urlhaus.abuse.ch/)
- [Moz Top 500 Domains](https://moz.com/top-brands#:~:text=Learn%20about%20Moz%E2%80%99s%20newest%20metric%2C%20Brand%20Authority%20,%20%2093%20%2036%20more%20rows%20)
- [Top 1000 Domains from Tranco](https://tranco-list.eu/)
- [Top 1000 Domains from Majestic Million](https://majestic.com/reports/majestic-million)
- [Top 1000 Domains from Cisco Umbrella](https://s3-us-west-1.amazonaws.com/umbrella-static/index.html)
- [Top 1000 Domains from DomCop](https://www.domcop.com/top-10-million-domains)

**Used for Testing:**

- [Phishing_Site_URLs_Kaggle Dataset](https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls)

For comprehensive insights into data processing, please refer to the "Data Processing Notebook."

## Data Modeling and Model Architecture

Our URL Classifier project employs a two-pronged approach to URL classification:

1. **NLP-based Model**: This model harnesses the power of N-Gram techniques to identify patterns in URLs. Specifically, it uses 3-Gram (Character-Gram) vectorization. The N-Gram model is adept at recognizing subtle patterns in URLs often associated with malicious intent, such as direct IP addresses or keywords like "pay," "offer," "OTP," and more.

2. **Lexical Features Model**: This model is based on a set of 18 lexical features associated with URLs. These features include whether the URL has an IP address, the presence of "http" or "https," URL length, the count of dots (.), the count of "www," and more. These features contribute to the model's ability to differentiate between safe and malicious URLs.

The features used for the lexical features method are:

- having_ip_address: Whether the URL includes an IP address or not
- abnormal_url: Whether the URL is in proper formatting or not
- count_dot: The number of dots (.) in the URL
- count_www: The number of "www" in the URL
- count_atrate: The number of "@" in the URL
- no_of_dir: The number of directories in the URL
- no_of_embed: The number of "/" in the URL
- count_https: The number of "https" in the URL
- count_http: The number of "http" in the URL
- count_percent: The number of "%" in the URL
- count_ques: The number of "?" in the URL
- count_hyphen: The number of "-" in the URL
- count_equal: The number of "=" in the URL
- Length of URL
- Hostname Length
- Count of Digits
- Count of Alpha-Numerical Characters
- Length of First Directory

The two models are merged as a TensorFlow model, which takes both inputs and outputs a final prediction based on a weighted average of the two scores.

The model performance is evaluated using accuracy, precision, recall, and F1-score metrics.<br>
For more information, see the modules in Utilities and the [URL Classification Paper](https://ieeexplore.ieee.org/document/10181514).

## Model Performance

The performance of our machine learning model is impressive:

- **Testing Data Accuracy**: 98.4%
- **Unseen Dataset Accuracy**: 71.1%

These results underscore the model's ability to effectively classify URLs, which is critical for cybersecurity. For a comprehensive understanding of how the model is trained and validated, refer to the "Model Training Notebook."

## Contributing

I welcome contributions to enhance the accuracy and functionality of the URL Classifier project. Here are some ways you can contribute:

- **Data**: If you have additional datasets or sources of URL data that can enhance the model's training, please share them with me.

- **Model Improvements**: If you have ideas or techniques to improve the model's performance, feel free to contribute code or suggestions.

- **Feedback**: Use the project interface to provide feedback on false URL classifications to help me refine the model.

To contribute, please refer to the project's GitHub repository [here](https://github.com/your-username/url-classifier). <br>
If you have any questions or feedback about this project, you can contact me at munna0912@gmail.com or connect with me on [LinkedIn](https://www.linkedin.com/in/munna-ram-950a5b200/).<br>
- [Munna Ram](https://github.com/munna0912) - Project Lead and Developer


## Acknowledgments

I would like to extend my gratitude to the following entities and communities:

- Kaggle for providing valuable datasets.
- URLhause, Moz, Tranco, Cisco Umbrella, DomCop, and Majestic Million for their data sources.
- Gradio for their framework that powers the web interface.
- HuggingFace for providing free resources to deploy the project.
- Free Sql Database services for providing MySQL datbase server.

Your contributions and support are integral to the success of this project. Thank you for being part of my effort to enhance cybersecurity through URL classification.

Feel free to explore the project, provide feedback, to make the internet a safer place!
>>>>>>> main
