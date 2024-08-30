# GCP Dataproc BigQuery Workflow Template

## Overview

This project is designed to facilitate the ingestion of data from Google Cloud Storage into BigQuery using Apache PySpark on Google Dataproc. Furthermore, it utilizes Google Cloud Scheduler for automated execution and GitHub Actions for seamless deployment. 

## Table of Contents

- [Technologies Used](#technologies-used)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
- [Workflow Overview](#workflow-overview)
- [Resources Created After Deployment](#resources-created-after-deployment)
- [License](#license)

## Technologies Used

- **Google Cloud Platform**: A suite of cloud computing services.
- **Google Cloud Storage**: Object storage for storing and retrieving any amount of data.
- **Google Dataproc**: Managed Spark and Hadoop service to process data easily and cost-effectively.
- **Apache Spark (PySpark)**: Analytics engine for big data processing with built-in modules.
- **Google BigQuery**: Fully managed data warehouse that enables super-fast SQL queries.
- **Google Cloud Scheduler**: Fully managed cron job service to execute tasks automatically.
- **GitHub Actions**: CI/CD framework for automating workflows, including deployment on GCP.

## Features

- Ingest data from Google Cloud Storage into BigQuery using Dataproc with PySpark.
- Utilize Cloud Scheduler to automate the execution of data ingestion workflows.
- Implement CI/CD for automated deployment through GitHub Actions.
- Comprehensive error handling and logging for reliable data processing.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites set up:

- Google Cloud account with billing enabled.
- Google Cloud SDK installed and configured.
- GitHub account.

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/jader-lima/gcp-dataproc-bigquery-workflow-template.git
   cd gcp-dataproc-bigquery-workflow-template

## Set Up Google Cloud Environment

1. **Create a Google Cloud Storage bucket** to store your data.
2. **Set up a BigQuery dataset** where your data will be ingested.
3. **Create a Dataproc cluster** for processing.

## Configure Environment Variables

Ensure the following environment variables are set in your deployment configuration or within GitHub Secrets:

- `PROJECT_ID`: Your Google Cloud project ID
- `BUCKET_NAME`: The name of your Cloud Storage bucket
- `BQ_DATASET`: The BigQuery dataset name
- `DATAPROC_REGION`: The Dataproc region you want to deploy to
- `SERVICE_ACCOUNT_KEY`: The JSON key for your service account with the necessary permissions.

## Deploy the Workflow

Follow the deployment instructions in the GitHub Actions workflow file included in the repository. This file automates the creation of required resources and schedules the ingestion process using Cloud Scheduler.

## Workflow Overview

The workflow involves the following key steps:

- **Data Ingestion**: Data is ingested from Google Cloud Storage into Dataproc.
- **Processing with PySpark**: The data is processed using PySpark, transforming it into the desired format.
- **Load into BigQuery**: After processing, the data is loaded into the configured BigQuery dataset.
- **Automation**: Google Cloud Scheduler initiates the execution of the workflow at defined intervals.

## Resources Created After Deployment

Upon deployment, the following resources are created:

### Google Cloud Storage Bucket

A Cloud Storage bucket to hold the source data before it's ingested into BigQuery.

### Dataproc Cluster

A managed Dataproc cluster specified in the workflow, used to process the data with PySpark.

### BigQuery Dataset

The dataset in BigQuery receives the processed data, making it ready for analysis.

### Cloud Scheduler Job

A Cloud Scheduler job that manages the automated execution of the ingestion workflow.
