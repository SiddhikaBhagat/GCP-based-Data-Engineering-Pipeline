GCP-based Data Engineering Pipeline
This project is an end-to-end data pipeline built to process, transform, and analyze Uber trip data. It demonstrates a complete workflow from raw data ingestion to a business intelligence-ready data warehouse, leveraging modern cloud and data tools.

Features
Automated ETL Pipeline: Processes raw data and loads it into a data warehouse.

Data Transformation: Uses Python to clean and structure raw data.

Workflow Orchestration: Automates the entire pipeline using Mage.

Cloud Integration: Deploys and runs all processes on Google Cloud Platform (GCP).

Dimensional Modeling: Designs and implements a star schema for efficient data storage and querying.

Data Warehousing: Stores processed data in BigQuery for high-performance analytics.

Tech Stack
Programming Language: Python

Orchestration: Mage

Cloud Platform: Google Cloud Platform (GCP)

Data Warehouse: Google BigQuery

Data Architecture
The pipeline follows a modern cloud-based ETL (Extract, Transform, Load) approach, ensuring data is moved and prepared efficiently.

The workflow is as follows:

Raw data is ingested and stored in a staging area (e.g., a cloud storage bucket).

Mage orchestrates the pipeline, triggering Python scripts to perform data cleaning and transformation.

The refined data is then loaded into BigQuery for final storage and analysis.

Data Model
The project uses a star schema for data modeling, which is a key design choice for optimizing query performance in a data warehouse. This model consists of a central fact table surrounded by dimension tables.

Fact Table: Contains quantitative data and foreign keys to dimension tables. In this project, the fact table would hold details like trip distance, fare, and foreign keys linking to the time and location dimensions.

Dimension Tables: Contain descriptive attributes that provide context to the fact table. Examples include tables for time (year, month, day), location (pickup and drop-off points), and vehicle details.

Getting Started
These instructions will help you set up and run the project.

Prerequisites
Python 3.x

Git

A Google Cloud Platform (GCP) account with a project and billing enabled.

Installation
Clone the repository:

Bash

git clone [your_github_repo_url]
Navigate to the project directory and install dependencies:

Bash

cd GCP-based-Data-Engineering-Pipeline
pip install -r requirements.txt
Usage
Configure GCP Credentials: Ensure your GCP service account keys are configured as environment variables or in your local development environment.

Run with Mage: Use the Mage UI to trigger the pipeline run. Mage will handle the execution of all the defined steps, from data transformation to loading into BigQuery.
