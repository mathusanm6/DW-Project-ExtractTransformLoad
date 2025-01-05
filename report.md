# Building and ETL pipeline

Contributors: Mathusan Selvakumar, Jewin Cheng
Course: Datawarehouse2 by A. Touil
Submission date: January 20 2025

## Table of Contents

1. [Abstract](#abstract)
2. [Table of Contents](#table-of-contents)
3. [Introduction](#introduction)
   - [3.1 Objective](#41-objective)
   - [3.2 Background](#42-background)
4. [Dataset Overview](#dataset-overview)
   - [4.1 Source of Data](#51-source-of-data)
   - [4.2 Dataset Challenges](#52-dataset-challenges)
5. [ETL Pipeline Design](#etl-pipeline-design)
   - [5.1 Tools and Technologies Used](#61-tools-and-technologies-used)
   - [5.2 Architecture](#62-architecture)
6. [Implementation Details](#implementation-details)
   - [6.1 Extract Phase](#71-extract-phase)
   - [6.2 Transform Phase](#72-transform-phase)
   - [6.3 Load Phase](#73-load-phase)
7. [Results and Evaluation](#results-and-evaluation)
   - [7.1 Key Findings](#81-key-findings)
   - [7.2 Performance Metrics](#82-performance-metrics)
8. [Challenges Faced and Solutions](#challenges-faced-and-solutions)
9. [Future Improvements](#future-improvements)
10. [Conclusion](#conclusion)
11. [References](#references)
12. [Appendix (Optional)](#appendix-optional)


### Abstract
The Datawarehouse2 course goal is to learn through a project how to works and build an ETL (extract, transform, load).
The Datasets used are datasets of video games sales from Twitch, Steam and IGDB.
Key transformations are: join datasets, calculate feature (average player counts by genre, engagement score and dropping unecessary columns)
The result is a dashboard, description TODO

