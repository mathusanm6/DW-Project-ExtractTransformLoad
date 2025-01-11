# Building and ETL pipeline

Contributors: Mathusan Selvakumar, Jewin Cheng  
Course: Datawarehouse2 by A. Touil  
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


### Abstract
The Datawarehouse2 course goal is to learn through a project how to build an ETL and does ETL works (extract, transform, load).  
The Datasets used are datasets of video popularity from IGDB and number of players from Steam using Twitch credentials access.  
Key transformations are: join datasets, calculate feature (average player counts by genre, engagement score and dropping unecessary columns).  
The result is a dashboard, description TODO.  

### Introduction
#### Objective
The objective of this course is to have an introduction of Datawarehouse concepts through a scholar project. We need to build an ETL from scratch whatever the tools used.  
#### Background
TODO

### Dataset Overview
#### Source of Data
Steam, IGDB
#### Dataset Challenges
Multiple source with heterogenous columns
### ETL Pipeline Design
extract.py
transform.py
load.py
analyze.py
main.py
#### Tools and Technologies used
Python lanugage, libraries: numpy, panda, matplolib, sqlite3, requets, os, shutil
#### Architecture
TODO

### Implementation details

#### Extract Phase
Accessing video game platform database with requests API
- Getting access token with twitch personal credentials
- Sending and make the right query to IGDB v4
- Filter the game data to fetch according to a popularity threshold
- Handle game features including timestamp to date and genre_id list to genre table
- Retrieve genre type of games from IGDB v4 with requests query
- Retrieving numbers of concurrent players from steam with requests query
- Saving datas as csv files in a local repository

#### Transform Phase
pandas dataframe to join, build features and clean data
#### Load Phase
Using sqlite3 API to load cleaned data to SQLite database

### Results and Evaluation
TODO

### Key Findings
TODO
### Performance Metrics
TODO
### Challenges Faced and Solutions
Learn a new way to fetch video games data through their specific API and understand their parameters.
### Future Improvements
TODO
### Conclusion
TODO
### References
TODO
### Appendix 