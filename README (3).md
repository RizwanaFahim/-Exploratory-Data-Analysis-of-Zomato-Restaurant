
# Zomato Restaurant Analysis: Exploring Locations, Ratings, and User Preferences

* This project conducts an exploratory data analysis on the Zomato restaurant dataset, examining factors such as restaurant locations, ratings, online ordering, table booking, cuisines, and customer preferences. 

* This analysis is beneficial for data analysts, researchers, restaurant owners, and anyone interested in gaining insights into restaurant trends and customer preferences within the Zomato dataset.


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Description

- The project utilizes Python programming language and data analysis libraries (pandas, numpy, matplotlib, seaborn) for an exploratory data analysis (EDA) on the Zomato restaurant dataset.

- Dataset: Contains comprehensive information about restaurants (locations, cuisines, ratings, costs, online ordering, table booking).
- Data Preprocessing:
  - Handling missing values.
  - Transforming variables.
- Analysis:
  - Distribution of restaurants across locations:
    - Identifying popular restaurant areas.
  - Impact of online ordering and table booking:
    - Analyzing customer preferences and ratings.
  - Impact of cuisine types on votes:
    - Identifying top cuisines based on vote count.
- Visualizations:
  - Created using matplotlib and seaborn libraries.
  - Help understand relationships between variables and uncover trends.


## Dataset

* Download the dataset from the Kaggle link below:

* https://rb.gy/bl3v5
## Installation

### Requirements

Installation Requirements:

1. Python: Install Python programming language.

2. pandas: Install the pandas library for data manipulation and analysis.

3. numpy: Install the numpy library for numerical operations.

4. matplotlib: Install the matplotlib library for data visualization.

5. seaborn: Install the seaborn library for enhanced data visualization.

### Setup

1. Install Python: Download and install Python from the official Python website (https://www.python.org) following the instructions for your operating system.

2. Install Required Libraries: Open a command prompt or terminal and run the following commands to install the necessary libraries:
   - pandas: `pip install pandas`
   - numpy: `pip install numpy`
   - matplotlib: `pip install matplotlib`
   - seaborn: `pip install seaborn`

3. Download the Zomato Dataset: Download the Zomato dataset (zomato.csv) and save it to a specific directory on your local machine.

4. Import Required Libraries: In your Python script or Jupyter Notebook, import the necessary libraries:
   ```python
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   import seaborn as sns
   ```

## Project Features

The project includes the following key features:

### 1. Data Preprocessing

- **Dropping unnecessary columns:** Remove irrelevant columns from the dataset, including 'url', 'address', 'dish_liked', 'phone', 'menu_item', and 'reviews_list'.
- **Handling missing values:** Address missing values by replacing the 'rate' column's missing values with the mean and dropping rows with missing values in other columns.
- **Data format cleanup:** Standardize the format of the 'rate' and 'approx_cost(for two people)' columns for consistency.

### 2. Analysis of Restaurant Ratings

- **Handling special rating values:** Convert special ratings like 'NEW' and '-' to NaN (missing values) for accurate analysis.
- **Rate distribution:** Explore the distribution of restaurant ratings after handling missing values.
- **Relationship between ratings and factors:** Investigate the impact of factors such as online ordering, table booking, etc., on restaurant ratings.

### 3. Cost Analysis

- **Cleaning the cost column:** Remove commas from the 'approx_cost(for two people)' column to convert it into a numerical format.
- **Cost comparison:** Analyze the distribution of costs and identify the cost range for two people in different restaurants.

### 4. Restaurant Types

- **Handling restaurant types:** Group less common restaurant types as 'others' for improved analysis.
- **Type distribution:** Explore the distribution of different restaurant types and identify the most prevalent ones.

### 5. Cuisine Analysis

- **Handling cuisines:** Group less common cuisines as 'others' for better analysis and understanding.
- **Cuisine distribution:** Analyze the distribution of different cuisines and identify the most popular ones.

### 6. Location Analysis

- **Handling locations:** Group locations with fewer restaurants as 'others' to simplify analysis.
- **Location distribution:** Explore the distribution of restaurants across different locations and identify popular areas.

### 7. Visualizations

- **Utilizing various visualizations:** Utilize count plots, bar plots, box plots, and other visualizations to present findings effectively.
- **Enhanced visualizations:** Enhance visualizations with a dark background style for improved readability.


## Report

* To view the detailed report of analysis, findings and suggestions, click on the link given below:





## Authors

- [@RizwanaFahim](https://github.com/RizwanaFahim)

## Purpose and Motivation

### Purpose
The project serves the following purposes:

1. Perform exploratory data analysis (EDA) on the Zomato restaurant dataset.
2. Gain insights into various aspects of the restaurant industry.
3. Understand the factors contributing to restaurant ratings.
4. Explore cost trends and identify popular cuisines and restaurant types.
5. Examine the distribution of restaurants across different locations.

### Motivation
The project is motivated by the following reasons:

1. Assist restaurant owners and managers in making informed decisions.
2. Aid customers in selecting restaurants based on ratings, cost, and cuisine preferences.
3. Provide valuable insights for market researchers and data analysts.
