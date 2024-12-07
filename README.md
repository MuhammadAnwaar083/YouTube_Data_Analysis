YouTube_Data_Analysis
Data Engineering YouTube Analysis Project by Muhammad Anwaar Ul Mustafa

Overview
This project is designed to securely manage, streamline, and perform analysis on the structured and semi-structured YouTube video data based on video categories and trending metrics.

Project Goals
Data Ingestion — A mechanism to ingest data from different sources will be built.
ETL System — Raw data will be obtained and transformed into the proper format.
Data Lake — Data from multiple sources will be centralized and stored in a repository.
Scalability — The system will be ensured to scale with increasing data size.
Cloud — The cloud (AWS) will be used for processing vast amounts of data as local computers are insufficient.
Reporting — A dashboard will be created to provide answers to previously defined questions.
Services Used
Amazon S3: An object storage service that provides manufacturing scalability, data availability, security, and performance.
AWS IAM: Identity and access management will be used to securely manage access to AWS services and resources.
QuickSight: A scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service designed for the cloud.
AWS Glue: A serverless data integration service that simplifies discovering, preparing, and combining data for analytics, machine learning, and application development.
AWS Lambda: A computing service that enables the execution of code without the need to create or manage servers.
AWS Athena: An interactive query service for S3 that allows querying data without needing to load it.
Dataset Used
The dataset from Kaggle contains statistics (CSV files) on daily trending YouTube videos over several months. There are up to 200 trending videos published every day for various locations. The data for each region is stored in separate files. The data includes video titles, channel titles, publication times, tags, views, likes, dislikes, descriptions, and comment counts. A category_id field, which varies by region, is also included in the JSON file linked to the respective region.

Dataset link: Kaggle YouTube Data

Architecture Diagram


This version follows the passive voice structure, emphasizing actions and processes rather than who is performing them. Let me know if you need further changes!
