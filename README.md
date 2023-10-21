# Comparison: Rust v. Python

[![GitHub Actions Workflow](https://github.com/simrunsharma/MiniProjectTemplate/actions/workflows/main.yml/badge.svg)](https://github.com/simrunsharma/MiniProjectTemplate/actions/workflows/main.yml)

Rust adn C use approzimately 1.00 J of energy and also the time for computational performance for both is approzimately 1.00 ms. However, when we consider Python, 70 times more energy and time is being used by python, comparitvely. From a sustainability, perspective this project considers should we move from Python to Rust. Rust and Python syntax isn't too different and thus we could save budget and be thoughtful towards reaching sustainability goals. 

## Functions
The functions that I will be using is an encrypt and decrypt cipher. I have a dataset that contains 1000 fortune cookies that contain hidden messsages. These messages are hidden by using the encrypt function to encrypt each of the messages and when someone uses my setup tool called "fortune" they will be able to get a randomly generated fortune that has been take from teh encrypted database and decrypted. The purpose of this project is to try and test to see the time and energy efficiency of doing this project in rust or python.

## Code Overview

### 1. Loading the Dataset

The script loads the World Development Indicators dataset into a Pandas DataFrame.

### 2. Logarithm Transformation

It calculates the logarithm of the GDP per capita variable to analyze its relationship with the infant mortality rate.

### 3. Data Visualization

A scatterplot is created using Seaborn to visually represent the relationship between log GDP per capita and infant mortality rate.

### 4. Descriptive Statistics

A function named `computation` is defined to compute descriptive statistics for the log GDP per capita variable, including the mean, median, and standard deviation.

### 5. Function Execution

The `computation` function is called with the DataFrame as input to calculate and display the statistics.

## Results

After executing the code, the following descriptive statistics were obtained for the log GDP per capita variable:

- Mean: 8.6995653667
- Median: 8.7217498371
- Standard Deviation: 1.47

These statistics offer insights into the central tendency and spread of the log GDP per capita data, contributing to a better understanding of its distribution.

The visualization below illustrates the relationship between the predictor variable (Log GDP Per Capita) and Infant Mortality Rate.

![Visualization Example](https://user-images.githubusercontent.com/141798228/266807301-e455df10-7308-42a5-bb9d-d055e5e45f8f.jpg)

## Conclusion

This script facilitates the exploration of the relationship between log GDP per capita and infant mortality rate using World Development Indicators data. It provides essential descriptive statistics for further analysis.
