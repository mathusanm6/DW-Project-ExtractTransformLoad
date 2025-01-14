# Building an ETL pipeline

Contributors: Mathusan Selvakumar, Jewin Cheng  
Course: Data Warehouse II by A. Touil  
Submission date: January 20 2025  

## Table of Contents

1. [Abstract](#abstract)
2. [Introduction](#introduction)
   - [2.1 Objective](#21-objective)
   - [2.2 Background](#22-background)
3. [Dataset Overview](#dataset-overview)
   - [3.1 Source of Data](#31-source-of-data)
   - [3.2 Dataset Challenges](#32-dataset-challenges)
4. [ETL Pipeline Design](#etl-pipeline-design)
   - [4.1 Tools and Technologies Used](#41-tools-and-technologies-used)
   - [4.2 Architecture](#42-architecture)
5. [Implementation Details](#implementation-details)
   - [5.1 Extract Phase](#51-extract-phase)
   - [5.2 Transform Phase](#52-transform-phase)
   - [5.3 Load Phase](#53-load-phase)
6. [Results and Evaluation](#results-and-evaluation)
   - [6.1 Key Findings](#61-key-findings)
   - [6.2 Performance Metrics](#62-performance-metrics)
7. [Challenges Faced and Solutions](#challenges-faced-and-solutions)
8. [Future Improvements](#future-improvements)
9. [Conclusion](#conclusion)
10. [References](#references)
11. [Appendix (Optional)](#appendix-optional)

---

### Abstract
The Data Warehouse II course focuses on building an ETL pipeline (Extract, Transform, Load) to understand its core components and their role in data warehousing.  
We utilized datasets sourced through HTTP requests to the IGDB (Internet Games Database) API and the Steam API.  
Key transformations included joining datasets, calculating derived features such as average player counts by genre and engagement scores, and filtering out unnecessary columns.  
The final output was presented as a dashboard showcasing game popularity by genre and player engagement trends on games rating.

---

### Introduction
#### Objective
The objective of this project was to gain practical experience with Data Warehouse concepts by building an ETL pipeline from scratch. Students were free to choose their tools and methods to demonstrate their understanding of ETL processes.  
We chose to build this pipeline in Python code to understand deeply the key concepts and to avoid the potential problems of software compatibility with our computers.

#### Background
ETL (Extract, Transform, Load) is a cornerstone of data integration in modern analytics workflows. It involves extracting data from various sources, transforming it into a usable format, and loading it into a database or data warehouse for analysis. This project emphasizes practical implementation, simulating real-world challenges in data engineering.  

---

### Dataset Overview

#### Source of Data
Data was retrieved from two main APIs:  
1. **IGDB API**: Provided detailed information about video games, including genres, ratings, and release dates.  
2. **Steam API**: Offered player count data and other gameplay statistics.  

#### Dataset Challenges
- Heterogeneous data structures and column formats.  
- Combining datasets from disparate sources while ensuring consistency.  

---

### ETL Pipeline Design

The pipeline was divided into separate modules for better organization and maintainability:  
- `extract.py`: Handles data extraction from APIs.  
- `transform.py`: Implements data cleaning, aggregation, and feature engineering.  
- `load.py`: Loads the processed data into a SQLite database.  
- `analyze.py`: Fetches and visualizes insights from the database.  
- `main.py`: Coordinates the execution of all pipeline stages.  

#### Tools and Technologies Used
- **Programming Language**: Python  
- **Libraries**: NumPy, Pandas, Matplotlib, SQLite3, Requests, OS, Shutil  


#### Architecture
The architecture is a modular pipeline:  
1. **Extract Phase**: Collects raw data from APIs and saves it locally as CSV files.  
2. **Transform Phase**: Cleans and processes the data to create a unified dataset.  
3. **Load Phase**: Stores the processed data in a SQLite database for analysis.  
4. **Analysis**: Generates insights through SQL queries and visualizations.  

---

### Implementation details

#### Extract Phase
Accessing video game platform database with requests API : 
- Obtained access tokens via Twitch credentials for IGDB API.  
- Queried IGDB v4 for game data filtered by a popularity threshold.
- Retrieved concurrent player counts from Steam API.  
- Processed game features, including timestamps and genre mappings.  
- Stored raw data in a local repository as CSV files.  

#### Transform Phase
In this part, we are going to aggregate all of our data table in one with pandas and build some features with numpy.
- Merged data tables using Pandas:
  - Steam data joined with DB game data on the `id` column.  
  - Genre data integrated using the `genre_id` column.  
- Compute engagement score as `rating * log(number of players)`
- Reorganized column structure for better usability and data storage.  
- Saved the cleaned dataset as a CSV file.

#### Load Phase
- Verified the existence of the SQLite database.  
- Loaded cleaned data using Pandas into SQLite tables.  
- Replaced or appended data to maintain database integrity.  

#### Load Phase
Using pandas and sqlite3 API to load cleaned data to SQLite database:
- Verified the existence of the SQLite database.
- Fetch cleaned data from data repository with pandas
- Create connection to games_data database with sqlite api
- Replaced or appended data to maintain database integrity.
- Close connection

---

### Results, Evaluation
Using `analyze.py`, we explored genre popularity and player engagement.

---

### Key Findings
- **Tactical games** were the most popular, followed by **Turn-based Strategy** and **RPGs**.  
- Engagement scores revealed a strong correlation between player counts and high ratings.  

---

### Performance Metrics
- ETL pipeline process: ~20 secconds
The query to IGDB and Steam database take most of the time.
- Querying the SQLite database and running the dashboard take around 4 seconds 

---

### Challenges Faced and Solutions
Learn a new way to fetch video games data through their specific API and understand their parameters.
- **API Query Limitations**: Managed rate limits by batching requests.
- **Data Integration**: Ensured schema consistency through preprocessing.  

---

### Future Improvements
- Integrate other game database for PC platform
- Incorporate data from other game platforms like PlayStation, Xbox, and Nintendo.  
- Add temporal dimensions to analyze trends over recent decades.  
- Explore additional features such as streaming popularity.  

---

### Conclusion
This project demonstrated the importance of ETL pipelines in building actionable insights from raw data. By integrating APIs, transforming datasets, and storing them in a database, we successfully showcased the power of data engineering for video game analytics.  

---

### References
- IGDB API Documentation: https://api-docs.igdb.com/#getting-started 
- Steam API Documentation: https://steamcommunity.com/developer/contentguidelines

