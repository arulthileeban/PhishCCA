# PhishCCA - Classifying phishing sites through content and certificate analysis

Phishing attacks are one of the most commonly used attack vectors in the last decade. Although various counter-measures have been proposed, many of them have huge flaws, particularly using machine learning models which always falls short. Few such particular flaws are lack of usage of appropriate data for the model and the high false positive rate due to the similarity in structure and content between the target site and the phishing site. 

In this paper, some of these flaws are tackled through the proposed system - PhishCCA , a two layered classification system  which initially classifies the site into the target site(Eg.:Paypal) and then further classifies if it's a phishing site or benign. This is achieved by developing a HTML content based classifier which classifies HTML pages into target sites and a TLS certificate based classifier which further classifies the website as a phishing site or benign. Although the integrated system hasn't been completely built, the HTML classifier achieves an accuracy of 77\% and the TLS classifer achieves an accuracy of 98\% which showcases the promise in this technique. 

## Model 
<p align="center">
  <img src="https://i.ibb.co/vvXVwhD/design.png">
</p>

## Files
- Certificate Classifier
	- Data
	- Cert_LSTM.ipynb - LSTM model for certificate based classification
	- Cert_RF.ipynb - Random forest model for certificate based classification
- Content Classifer 
	- Dataset
	- HTML_Classification.ipynb - LSTM model for HTML content based classifcation
   

