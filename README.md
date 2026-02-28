SMS Spam Detector
A machine learning project that classifies SMS messages as spam or not spam using Python and Logistic Regression.
How It Works
The model is trained on real SMS messages from the Kaggle SMS Spam Collection dataset. Each message is converted into a bag-of-words feature vector — a list of 1s and 0s representing whether each vocabulary word appears in the message. Logistic Regression then learns which word patterns indicate spam.
What I Learned

	∙	How to represent text data as numbers for machine learning
	∙	Bag of words vectorization
	∙	Training a Logistic Regression classifier
	∙	Building an interactive prediction interface
Limitations

	∙	Small dataset (60 messages) so some spam combinations may not be detected
	∙	Bag of words does not account for word importance or frequency
	∙	Upgraded version using TF-IDF vectorization coming soon
Tech Stack

	∙	Python
	∙	scikit-learn
	∙	Logistic Regression
Usage
Run the script and type any message when prompted. The model will classify it as SPAM or NOT SPAM.
Dataset
Based on the UCI SMS Spam Collection Dataset available on Kaggle.