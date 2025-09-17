# GCP-based Data Engineering Pipeline

## Introduction

This project is an end-to-end data engineering pipeline that processes, transforms, and analyzes Uber trip data. It demonstrates a complete workflow from raw data ingestion to a business intelligence-ready data warehouse, leveraging modern cloud technologies and data engineering principles.

## Key Features
 - **Automated Data Ingestion** : Automates the extraction of raw Uber trip data and loads it into a cloud storage bucket.

 - **Data Transformation** : Uses Python to clean and structure the raw data, making it ready for analysis.

 - **Workflow Orchestration** : Manages and automates the entire pipeline using Mage, a user-friendly, notebook-based orchestration tool.

 - **Cloud Integration** : The entire pipeline is deployed and runs on Google Cloud Platform (GCP).

 - **Dimensional Modeling** : The transformed data is structured using a star schema to optimize it for fast querying and reporting.

 - **Data Warehousing** : Loads the processed data into BigQuery, a scalable and serverless cloud data warehouse.

 - Built a final dashboard to visualize key business insights, including trip trends and geospatial analysis.

## Architecture 
<img src="architecture.jpg">

## Technology Used
- Programming Language - Python

Google Cloud Platform
1. Google Storage
2. Compute Instance
3. Orchestration: Mage
4. BigQuery
5. Looker Studio

## Data Model

The data is modeled using a star schema, a common technique for data warehousing that simplifies queries and improves performance. This model consists of a central fact table surrounded by multiple dimension tables.

<img src="data_model.jpeg">


## Dataset Used
TLC Trip Record Data
Yellow and green taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts. 

Here is the dataset used - 




