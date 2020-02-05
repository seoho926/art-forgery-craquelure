# Detecting Art Forgery Using Image Classification of Craquelure Patterns
This project is the capstone project for the Flatiron School Data Science Fellowship program.

## Project Objective
The purpose of this project is to use machine learning to help detect art forgeries by classifying craquelure (cracks due to old age) patterns in classical oil paintings.

## Project Description
Oil paintings have different craquelure patterns depending on the time period and region they were created. Being able to classify when and/or where a painting is or is not from could add valuable information to determining whether a piece of work is authentic or a fake/forgery.

This project specifically looked at:
  * 17th century
  * Oil on canvas
  * Dutch vs. Flemish (Belgian) paintings
  
### Methods Used
* Convolutional Neural Network (CNN)

### Technologies
* Python
  * Matplotlib
  * Numpy
  * Keras
  * PIL
  * cv2
  * os
* Cloud Computing
  * AWS
  * Google Cloud

### Featured Notebooks/Analysis/Deliverables
* [notebooks/MASTER.ipynb]()
* [Detecting Art Forgery Using Image Classification of Craquelure Patterns.pdf](https://github.com/seoho926/art-forgery-craquelure/blob/master/art%20forgery%20and%20craquelure.pdf)

### Data
* Full paintings from which craquelure images were extracted are in [data/Full Paintings](https://github.com/seoho926/art-forgery-craquelure/tree/master/data/Full%20paintings) folder in this repo (the actual high resolution images are on the National Gallery of Art website below)
* Craquelure images used for modeling are available for download as a zipfile in the AWS S3 bucket: [art.forgery.capstone.project](https://s3.console.aws.amazon.com/s3/buckets/art.forgery.capstone.project/?region=us-east-1&tab=overview)

### Sources
* [National Gallery of Art](https://www.nga.gov/collection/collection-search.html)
