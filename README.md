# Gender Predictor By Personal Metrics

This project detects the gender of a person (or group of people) based on their height, weight and shoe size.

## Script Structure

The training data "X" is made up of 10 records, but increasing this number can provide a more accurate prediction.

Each training record is a Python list made up of 3 elements in order [heigh, weight, shoe size].

## Customising The Data

To run the prediction on your own data, edit "newData" by inserting a new list of [heigh, weight, shoe size] per peson.
Don't forget to separate the lists with a comma.

## How To Run

Depending of your running version of Python, In the terminal type 

```
python index.py 
```

or 

```
python3 index.py
```

You should get a list of genders that correspond to your inserted data.
For example: `['male' 'male']` or `['female' 'male']`, etc..