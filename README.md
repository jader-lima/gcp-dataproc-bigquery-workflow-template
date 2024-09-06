# GCP Dataproc BigQuery Workflow Template

## Overview

This project is designed to facilitate the ingestion of data from Google Cloud Storage into BigQuery using Apache PySpark on Google Dataproc. Furthermore, it utilizes Google Cloud Scheduler for automated execution and GitHub Actions for seamless deployment. 

## Table of Contents

- [Technologies Used](#technologies-used)
- [Features](#features)
- [Architecture Diagram](#architecture-diagram)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
- [Deploying the project](#workflow-overview)
  - [Workflow File YAML Explanation](#workflow-yaml-explanation)
- [Resources Created After Deployment](#resources-created-after-deployment)
- [Conclusion](#Conclusion)

## Technologies Used

- **Google Dataproc**
Google Dataproc is a fully managed cloud service designed to simplify running Apache Spark and Hadoop clusters in the Google Cloud ecosystem. It provides a fast and scalable way to process large datasets while integrating seamlessly with other Google Cloud services, such as Cloud Storage, to minimize operational overhead and ensure efficient big data processing.

- **Cloud Storage**
Google Cloud Storage is a scalable and secure object storage service for storing large amounts of unstructured data. It offers high availability and strong global consistency, making it suitable for a wide range of scenarios, such as data backups, big data analytics, and content distribution.

- **Workflow Templates**
Workflow templates in Google Cloud simplify the definition and management of complex processes involving multiple cloud services. This feature helps in scheduling and executing intricate workflows, optimizing resource management, and automating multi-step tasks across different services.

- **Cloud Scheduler**
Google Cloud Scheduler is a fully managed service for running scheduled jobs with no infrastructure to manage. It can be used to automate workflows, run reports, or trigger specific cloud services at defined intervals.

- **CI/CD Process with GitHub Actions**
Implementing a CI/CD pipeline with GitHub Actions automates the build, test, and deployment stages of your project. In this workflow, GitHub Actions triggers deployment to Google Cloud every time code changes are pushed to the repository, ensuring a consistent and accurate deployment process with minimal manual intervention.

- **GitHub Secrets and Configuration**
GitHub Secrets is essential for maintaining the security of sensitive information like API keys, service account credentials, and other configuration data. By securely storing these details outside your source code, you mitigate the risk of unauthorized access and potential leaks.

- **Google BigQuery**
A fully managed, scalable data warehouse that enables lightning-fast SQL queries and supports large-scale analytics across terabytes of data.

## Features

- Ingest data from Google Cloud Storage into BigQuery using Dataproc with PySpark.
- Utilize Cloud Scheduler to automate the execution of data ingestion workflows.
- Implement CI/CD for automated deployment through GitHub Actions.
- Comprehensive error handling and logging for reliable data processing.

## Architecture Diagram

![Architecture Diagram](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8q2nw194pekf1nfkctbr.png)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites set up:

- Google Cloud account with billing enabled.
- GitHub account.

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/jader-lima/gcp-dataproc-bigquery-workflow-template.git
   cd gcp-dataproc-bigquery-workflow-template
```
## Set Up Google Cloud Environment

1. **Create a Google Cloud Storage bucket** to store your data.
2. **Set up a BigQuery dataset** where your data will be ingested.
3. **Create a Dataproc cluster** for processing.

## Configure Environment Variables

Ensure the following environment variables are set in your deployment configuration or within GitHub Secrets:

- `GCP_BUCKET_BIGDATA_FILES`: Secret used to store the name of the cloud storage
- `GCP_BUCKET_DATALAKE`: Secret used to store the name of the cloud storage
- `GCP_BUCKET_DATAPROC`: Secret used to store the name of the cloud storage
- `GCP_BUCKET_TEMP_BIGQUERY`: Secret used to store the name of the cloud storage
- `GCP_SA_KEY`: Secret used to store the value of the service account key. For this project, the default service key was used. 
- `GCP_SERVICE_ACCOUNT`: Secret used to store the value of the service account key. For this project, the default service key was used. 
- `PROJECT_ID`: Secret used to store the project id value


### Creating github secret

1. To create a new secret:
    1. In project repository, menu **Settings** 
    2. **Security**, 
    3. **Secrets and variables**,click in access **Action**
    4. **New repository secret**, type a **name** and **value** for secret.

![github secret creation](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/i45cicz0q89ije7j70yf.png)

For more details , access :
https://docs.github.com/pt/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions

## Deploying the project <a name="workflow-overview"></a>

Whenever a push to the main branch occurs, GitHub Actions will trigger and run the YAML script. The script contains four jobs, described in detail below. In essence, GitHub Actions uses the service account credentials to authenticate with Google Cloud and execute the necessary steps as described in the YAML file.

## Workflow File YAML Explanation<a name="workflow-yaml-explanation"></a>

Environments Needed
We have variations for basic usage for cluster characteristics, bucket paths, process names and steps 
make workflow. In case of new steps in the workflow or new scripts, new variables can be easily added as below :

```yaml
MY_VAR_NAME : my_var_value 
${{ env.MY_VAR_NAME}}
```

```yaml
env:
    REGION: us-east1
    ZONE: us-east1-b
    DATAPROC_CLUSTER_NAME: dataproc-bigdata-multi-node-cluster
    DATAPROC_WORKER_TYPE: n2-standard-2
    DATAPROC_MASTER_TYPE: n2-standard-2
    DATAPROC_NUM_WORKERS: 2
    DATAPROC_IMAGE_VERSION: 2.1-debian11
    DATAPROC_WORKER_NUM_LOCAL_SSD: 1
    DATAPROC_MASTER_NUM_LOCAL_SSD: 1
    DATAPROC_MASTER_BOOT_DISK_SIZE: 32   
    DATAPROC_WORKER_DISK_SIZE: 32
    DATAPROC_MASTER_BOOT_DISK_TYPE: pd-balanced
    DATAPROC_WORKER_BOOT_DISK_TYPE: pd-balanced
    DATAPROC_COMPONENTS: JUPYTER
    DATAPROC_WORKFLOW_NAME: report_olist_order_items
    BIGQUERY_DATASET: olist
    BIGQUERY_TABLE_ORDER_ITEMS: order_items_report
    BRONZE_DATALAKE_FILES: bronze
    TRANSIENT_DATALAKE_FILES: transient
    BUCKET_DATALAKE_FOLDER: transient
    BUCKET_BIGDATA_JAR_FOLDER: jars
    BUCKET_BIGDATA_SCRIPT_FOLDER: scripts
    BUCKET_BIGDATA_PYSPARK_FOLDER: pyspark
    BUCKET_BIGDATA_PYSPARK_INGESTION: ingestion
    BUCKET_BIGDATA_PYSPARK_ENRICHMENT: enrichment/
    DATAPROC_APP_NAME: ingestion_countries_csv_to_delta 
    JAR_LIB1: delta-core_2.12-2.3.0.jar
    JAR_LIB2: delta-storage-2.3.0.jar 
    APP_NAME: 'countries_ingestion_csv_to_delta'
    PYSPARK_INGESTION_SCRIPT: ingestion_csv_to_delta.py
    PYSPARK_ENRICHMENT_SCRIPT_ORDER_ITENS: order_order_items_to_bigquery.py
    TIME_PARTITION_FIELD: datePartition
    FILE1: orders
    FILE2: order_items
    SUBJECT : olist
    STEP1 : orders
    STEP2 : order_items
    STEP3 : order_items_report
    TIME_ZONE : America/Sao_Paulo
    SCHEDULE : "00 12 * * *"
    SCHEDULE_NAME : schedule_olist_etl
    SERVICE_ACCOUNT_NAME : account-dataproc-bq-workflow
    CUSTOM_ROLE : DataProcBigQueryWorkflowCustomRole
    STEP1_NAME : step_ingestion_orders
    STEP2_NAME : step_ingestion_order_items
    STEP3_NAME : step_ingestion_order_items_bigquery
```

## Workflow Job Steps <a name="workflow-job-steps"></a>


- **deploy-buckets**:
This step is responsible for creating the required Cloud Storage buckets. If the bucket name does not already exist, it will be created. Once the buckets are created, the necessary data files, JARs, and scripts are copied into the appropriate folders.

```yaml
jobs:
  deploy-buckets:
    runs-on: ubuntu-22.04
    timeout-minutes: 10

    steps:
    - name: Checkout
      uses: actions/checkout@v4
    
    - name: Authorize GCP
      uses: 'google-github-actions/auth@v2'
      with:
        credentials_json:  ${{ secrets.GCP_SA_KEY }}
    
    # Step to Authenticate with GCP
    - name: Set up Cloud SDK
      uses: google-github-actions/setup-gcloud@v2
      with:
        version: '>= 363.0.0'
        project_id: ${{ secrets.PROJECT_ID }}

    # Step to Configure Docker to use the gcloud command-line tool as a credential helper
    - name: Configure Docker
      run: |-
        gcloud auth configure-docker


    # Step to Create GCP Bucket 
    - name: Create Google Cloud Storage - files
      run: |-
        if ! gsutil ls -p ${{ secrets.PROJECT_ID }} gs://${{ secrets.GCP_BUCKET_BIGDATA_FILES }} &> /dev/null; \
          then \
            gcloud storage buckets create gs://${{ secrets.GCP_BUCKET_BIGDATA_FILES }} --default-storage-class=nearline --location=${{ env.REGION }}
          else
            echo "Cloud Storage : gs://${{ secrets.GCP_BUCKET_BIGDATA_FILES }}  already exists" ! 
          fi

    # Step to Create GCP Bucket 
    - name: Create Google Cloud Storage - dataproc
      run: |-
        if ! gsutil ls -p ${{ secrets.PROJECT_ID }} gs://${{ secrets.GCP_BUCKET_DATAPROC }} &> /dev/null; \
          then \
            gcloud storage buckets create gs://${{ secrets.GCP_BUCKET_DATAPROC }} --default-storage-class=nearline --location=${{ env.REGION }}
          else
            echo "Cloud Storage : gs://${{ secrets.GCP_BUCKET_DATAPROC }}  already exists" ! 
          fi

    # Step to Create GCP Bucket 
    - name: Create Google Cloud Storage - datalake
      run: |-
        if ! gsutil ls -p ${{ secrets.PROJECT_ID }} gs://${{ secrets.GCP_BUCKET_DATALAKE }} &> /dev/null; \
          then \
            gcloud storage buckets create gs://${{ secrets.GCP_BUCKET_DATALAKE }} --default-storage-class=nearline --location=${{ env.REGION }}
          else
            echo "Cloud Storage : gs://${{ secrets.GCP_BUCKET_DATALAKE }}  already exists" ! 
          fi

    # Step to Create GCP Bucket 
    - name: Create Google Cloud Storage - big query temp files
      run: |-
        if ! gsutil ls -p ${{ secrets.PROJECT_ID }} gs://${{ secrets.GCP_BUCKET_TEMP_BIGQUERY }} &> /dev/null; \
          then \
            gcloud storage buckets create gs://${{ secrets.GCP_BUCKET_TEMP_BIGQUERY }} --default-storage-class=nearline --location=${{ env.REGION }}
          else
            echo "Cloud Storage : gs://${{ secrets.GCP_BUCKET_TEMP_BIGQUERY }}  already exists" ! 
          fi

    # Step to Upload the file to GCP Bucket - transient files
    - name: Upload transient files to Google Cloud Storage
      run: |-
        TARGET=${{ env.TRANSIENT_DATALAKE_FILES }}
        BUCKET_PATH=${{ secrets.GCP_BUCKET_DATALAKE }}/${{ env.BUCKET_DATALAKE_FOLDER }}    
        gsutil cp -r $TARGET gs://${BUCKET_PATH}


    # Step to Upload the file to GCP Bucket - jar files
    - name: Upload jar files to Google Cloud Storage
      run: |-
        TARGET=${{ env.BUCKET_BIGDATA_JAR_FOLDER }}
        BUCKET_PATH=${{ secrets.GCP_BUCKET_BIGDATA_FILES }}/${{ env.BUCKET_BIGDATA_JAR_FOLDER }}
        gsutil cp -r $TARGET gs://${BUCKET_PATH}

    # Step to Upload the file to GCP Bucket - pyspark files
    - name: Upload pyspark files to Google Cloud Storage
      run: |-
        TARGET=${{ env.BUCKET_BIGDATA_SCRIPT_FOLDER}}/${{ env.BUCKET_BIGDATA_PYSPARK_FOLDER}}
        BUCKET_PATH=${{ secrets.GCP_BUCKET_BIGDATA_FILES}}/${{ env.BUCKET_BIGDATA_SCRIPT_FOLDER}}/${{ env.BUCKET_BIGDATA_PYSPARK_FOLDER}}
        gsutil cp -r $TARGET gs://${BUCKET_PATH}

```

- **deploy-bigquery-dataset-bigquery-tables**:
This step creates the BigQuery dataset and tables. It checks for the existence of a dataset and validates whether a table is present. The table schema is copied from a predefined JSON file located in the scripts/libs bucket.

```yaml
deploy-bigquery-dataset-bigquery-tables:
    needs: [deploy-buckets]
    runs-on: ubuntu-22.04
    timeout-minutes: 10

    steps:
    - name: Checkout
      uses: actions/checkout@v4
    
    - name: Authorize GCP
      uses: 'google-github-actions/auth@v2'
      with:
        credentials_json:  ${{ secrets.GCP_SA_KEY }}
    
    # Step to Authenticate with GCP
    - name: Set up Cloud SDK
      uses: google-github-actions/setup-gcloud@v2
      with:
        version: '>= 363.0.0'
        project_id: ${{ secrets.PROJECT_ID }}

    # Step to Configure Docker to use the gcloud command-line tool as a credential helper
    - name: Configure Docker
      run: |-
        gcloud auth configure-docker


    - name: Create Big Query Dataset
      run: |-  
        if ! bq ls --project_id ${{ secrets.PROJECT_ID}} -a | grep -w ${{ env.BIGQUERY_DATASET}} &> /dev/null; \
          then 

            bq --location=${{ env.REGION }} mk \
          --default_table_expiration 0 \
          --dataset ${{ env.BIGQUERY_DATASET }}

          else
            echo "Big Query Dataset : ${{ env.BIGQUERY_DATASET }} already exists" ! 
          fi

    - name: Create Big Query table
      run: |-
        TABLE_NAME_ORDER_ITEMS=${{ env.BIGQUERY_DATASET}}.${{ env.BIGQUERY_TABLE_ORDER_ITEMS}}
        c=0
        for table in $(bq ls --max_results 1000 "${{ secrets.PROJECT_ID}}:${{ env.BIGQUERY_DATASET}}" | tail -n +3 | awk '{print $1}'); do

            # Determine the table type and file extension
            if bq show --format=prettyjson $TABLE_NAME_ORDER_ITEMS | jq -r '.type' | grep -q -E "TABLE"; then
              echo "Dataset ${{ env.BIGQUERY_DATASET}} already has table named : $table " !
              if [ "$table" == "${{ env.BIGQUERY_TABLE_ORDER_ITEMS}}" ]; then
                echo "Dataset ${{ env.BIGQUERY_DATASET}} already has table named : $table " !
                ((c=c+1)) 		
              fi                  
            else
                echo "Ignoring $table"            
                continue
            fi
        done
        echo " contador $c "
        if [ $c == 0 ]; then
          echo "Creating table named : $table for Dataset ${{ env.BIGQUERY_DATASET}} " !
         
          bq mk --table \
          --time_partitioning_field ${{ env.TIME_PARTITION_FIELD}} \
          $TABLE_NAME_ORDER_ITEMS \
          ./scripts/bigquery_files/schemas/order_items_schema.json

          
        fi
```

- **deploy-dataproc-workflow-template**:

This step creates the workflow template. It sets up a Dataproc cluster and links it with the workflow. The three main steps of the workflow are then created, with validations ensuring that each component is only created once.

```yaml
 deploy-dataproc-workflow-template:
    needs: [deploy-buckets]
    runs-on: ubuntu-22.04
    timeout-minutes: 10

    steps:
    - name: Checkout
      uses: actions/checkout@v4
    
    - name: Authorize GCP
      uses: 'google-github-actions/auth@v2'
      with:
        credentials_json:  ${{ secrets.GCP_SA_KEY }}
    
    # Step to Authenticate with GCP
    - name: Set up Cloud SDK
      uses: google-github-actions/setup-gcloud@v2
      with:
        version: '>= 363.0.0'
        project_id: ${{ secrets.PROJECT_ID }}

    # Step to Configure Docker to use the gcloud command-line tool as a credential helper
    - name: Configure Docker
      run: |-
        gcloud auth configure-docker

    - name: Create Dataproc Workflow
      run: |-  
        if ! gcloud dataproc workflow-templates list --region=${{ env.REGION}} | grep -i ${{ env.DATAPROC_WORKFLOW_NAME}} &> /dev/null; \
          then \
            gcloud dataproc workflow-templates create ${{ env.DATAPROC_WORKFLOW_NAME }} --region ${{ env.REGION }}

          else
            echo "Workflow Template : ${{ env.DATAPROC_WORKFLOW_NAME }} already exists" ! 
          fi

    - name: Create Dataproc Managed Cluster
      run: >       
        gcloud dataproc workflow-templates set-managed-cluster ${{ env.DATAPROC_WORKFLOW_NAME }} 
        --region ${{ env.REGION }} 
        --zone ${{ env.ZONE }} 
        --image-version ${{ env.DATAPROC_IMAGE_VERSION }} 
        --master-machine-type=${{ env.DATAPROC_MASTER_TYPE }} 
        --master-boot-disk-type ${{ env.DATAPROC_MASTER_BOOT_DISK_TYPE }} 
        --master-boot-disk-size ${{ env.DATAPROC_MASTER_BOOT_DISK_SIZE }} 
        --worker-machine-type=${{ env.DATAPROC_WORKER_TYPE }} 
        --worker-boot-disk-type ${{ env.DATAPROC_WORKER_BOOT_DISK_TYPE }}
        --worker-boot-disk-size ${{ env.DATAPROC_WORKER_DISK_SIZE }} 
        --num-workers=${{ env.DATAPROC_NUM_WORKERS }} 
        --cluster-name=${{ env.DATAPROC_CLUSTER_NAME }} 
        --optional-components ${{ env.DATAPROC_COMPONENTS }} 
        --service-account=${{ env.GCP_SERVICE_ACCOUNT }}

    - name: Add Job Ingestion orders to Workflow
      run: |-
        if gcloud dataproc workflow-templates list --region=${{ env.REGION}} | grep -i ${{ env.DATAPROC_WORKFLOW_NAME}} &> /dev/null; \
          then \
            
            if gcloud dataproc workflow-templates describe ${{ env.DATAPROC_WORKFLOW_NAME}} --region=${{ env.REGION}} | grep -i ${{ env.STEP1_NAME  }} &> /dev/null; \
            then \
              echo "Workflow Template : ${{ env.DATAPROC_WORKFLOW_NAME }} already has step : ${{ env.STEP1_NAME  }} " ! 
            else
              PYSPARK_SCRIPT_PATH=${{ secrets.GCP_BUCKET_BIGDATA_FILES}}/${{ env.BUCKET_BIGDATA_SCRIPT_FOLDER}}/${{ env.BUCKET_BIGDATA_PYSPARK_FOLDER}}/${{ env.BUCKET_BIGDATA_PYSPARK_INGESTION}}/${{ env.PYSPARK_INGESTION_SCRIPT}}
              JARS_PATH=gs://${{ secrets.GCP_BUCKET_BIGDATA_FILES }}/${{ env.BUCKET_BIGDATA_JAR_FOLDER }}/${{ env.JAR_LIB1 }}
              JARS_PATH=${JARS_PATH},gs://${{ secrets.GCP_BUCKET_BIGDATA_FILES }}/${{ env.BUCKET_BIGDATA_JAR_FOLDER }}/${{ env.JAR_LIB2 }}
              TRANSIENT=${{ secrets.GCP_BUCKET_DATALAKE }}/${{ env.BUCKET_DATALAKE_FOLDER }}/${{ env.SUBJECT }}/${{ env.FILE1 }}
              BRONZE=${{ secrets.GCP_BUCKET_DATALAKE }}/${{ env.BRONZE_DATALAKE_FILES }}/${{ env.SUBJECT }}/${{ env.FILE1 }}

              gcloud dataproc workflow-templates add-job pyspark gs://${PYSPARK_SCRIPT_PATH} \
              --workflow-template ${{ env.DATAPROC_WORKFLOW_NAME }}  \
              --step-id ${{env.STEP1_NAME }} \
              --region ${{ env.REGION }} \
              --jars ${JARS_PATH} \
              -- --app_name=${{ env.APP_NAME }}${{ env.STEP1 }} --bucket_transient=gs://${TRANSIENT} \
              --bucket_bronze=gs://${BRONZE}
            fi
        else
          echo "Workflow Template : ${{ env.DATAPROC_WORKFLOW_NAME}} not exists" ! 
        fi        

    - name: Add Job Ingestion order items to Workflow
      run: |-
        if gcloud dataproc workflow-templates list --region=${{ env.REGION}} | grep -i ${{ env.DATAPROC_WORKFLOW_NAME}} &> /dev/null; \
          then \
            if gcloud dataproc workflow-templates describe ${{ env.DATAPROC_WORKFLOW_NAME}} --region=${{ env.REGION}} | grep -i ${{ env.STEP2_NAME }} &> /dev/null; \
            then \
              echo "Workflow Template : ${{ env.DATAPROC_WORKFLOW_NAME }} already has step : ${{ env.STEP2_NAME  }} " ! 
            else
              PYSPARK_SCRIPT_PATH=${{ secrets.GCP_BUCKET_BIGDATA_FILES}}/${{ env.BUCKET_BIGDATA_SCRIPT_FOLDER}}/${{ env.BUCKET_BIGDATA_PYSPARK_FOLDER}}/${{ env.BUCKET_BIGDATA_PYSPARK_INGESTION}}/${{ env.PYSPARK_INGESTION_SCRIPT}}
              JARS_PATH=gs://${{ secrets.GCP_BUCKET_BIGDATA_FILES }}/${{ env.BUCKET_BIGDATA_JAR_FOLDER }}/${{ env.JAR_LIB1 }}
              JARS_PATH=${JARS_PATH},gs://${{ secrets.GCP_BUCKET_BIGDATA_FILES }}/${{ env.BUCKET_BIGDATA_JAR_FOLDER }}/${{ env.JAR_LIB2 }}
              TRANSIENT=${{ secrets.GCP_BUCKET_DATALAKE }}/${{ env.BUCKET_DATALAKE_FOLDER }}/${{ env.SUBJECT }}/${{ env.FILE2 }}
              BRONZE=${{ secrets.GCP_BUCKET_DATALAKE }}/${{ env.BRONZE_DATALAKE_FILES }}/${{ env.SUBJECT }}/${{ env.FILE2 }}


              gcloud dataproc workflow-templates add-job pyspark gs://${PYSPARK_SCRIPT_PATH} \
              --workflow-template ${{ env.DATAPROC_WORKFLOW_NAME }}  \
              --step-id ${{ env.STEP2_NAME }} \
              --start-after ${{ env.STEP1_NAME }} \
              --region ${{ env.REGION }} \
              --jars ${JARS_PATH} \
              -- --app_name=${{ env.APP_NAME }}${{ env.STEP2 }} --bucket_transient=gs://${TRANSIENT} \
              --bucket_bronze=gs://${BRONZE}
            fi
        else
          echo "Workflow Template : ${{ env.DATAPROC_WORKFLOW_NAME}} not exists" ! 
        fi
       

    - name: Add Job order + order items ingestion into big query  to Workflow
      run: |-
        if gcloud dataproc workflow-templates list --region=${{ env.REGION}} | grep -i ${{ env.DATAPROC_WORKFLOW_NAME}} &> /dev/null; \
          then \
            if gcloud dataproc workflow-templates describe ${{ env.DATAPROC_WORKFLOW_NAME}} --region=${{ env.REGION}} | grep -i ${{ env.STEP3_NAME }} &> /dev/null; \
            then \
              echo "Workflow Template : ${{ env.DATAPROC_WORKFLOW_NAME }} already has step : ${{ env.STEP3_NAME }} " ! 
            else

              PYSPARK_SCRIPT_PATH=${{ secrets.GCP_BUCKET_BIGDATA_FILES}}/${{ env.BUCKET_BIGDATA_SCRIPT_FOLDER}}/${{ env.BUCKET_BIGDATA_PYSPARK_FOLDER}}/${{ env.BUCKET_BIGDATA_PYSPARK_ENRICHMENT}}/${{ env.PYSPARK_ENRICHMENT_SCRIPT_ORDER_ITENS}}
              JARS_PATH=gs://${{ secrets.GCP_BUCKET_BIGDATA_FILES }}/${{ env.BUCKET_BIGDATA_JAR_FOLDER }}/${{ env.JAR_LIB1 }}
              JARS_PATH=${JARS_PATH},gs://${{ secrets.GCP_BUCKET_BIGDATA_FILES }}/${{ env.BUCKET_BIGDATA_JAR_FOLDER }}/${{ env.JAR_LIB2 }}
              BRONZE_ORDERS=${{ secrets.GCP_BUCKET_DATALAKE}}/${{ env.BRONZE_DATALAKE_FILES}}/${{ env.SUBJECT}}/${{ env.FILE1}}
              BRONZE_ORDER_ITEMS=${{ secrets.GCP_BUCKET_DATALAKE}}/${{ env.BRONZE_DATALAKE_FILES}}/${{ env.SUBJECT}}/${{ env.FILE2}}
              TABLE_NAME_ORDER_ITEMS=${{ secrets.PROJECT_ID}}.${{ env.BIGQUERY_DATASET}}.${{ env.BIGQUERY_TABLE_ORDER_ITEMS}}
              BIG_QUERY_TEMP=${{ secrets.GCP_BUCKET_TEMP_BIGQUERY }}



              gcloud dataproc workflow-templates add-job pyspark gs://${PYSPARK_SCRIPT_PATH} \
              --workflow-template ${{ env.DATAPROC_WORKFLOW_NAME }}  \
              --step-id ${{ env.STEP3_NAME }} \
              --start-after ${{ env.STEP1_NAME }},${{ env.STEP2_NAME }} \
              --region ${{ env.REGION }} \
              --jars ${JARS_PATH} \
              -- --app_name=${{ env.APP_NAME }}${{ env.STEP3 }} --bronze_orders_zone=gs://${BRONZE_ORDERS} \
              --bronze_orders_items_zone=gs://${BRONZE_ORDER_ITEMS} \
              --bigquery_table=${TABLE_NAME_ORDER_ITEMS} \
              --temp_bucket=${BIG_QUERY_TEMP} 

            fi
        else
          echo "Workflow Template : ${{ env.DATAPROC_WORKFLOW_NAME}} not exists" ! 
        fi

```

- **deploy-cloud-schedule**:
In this final step, a service account, custom role, and Cloud Scheduler job are created. The Cloud Scheduler runs the workflows on a predefined schedule, and the service account used is granted the necessary permissions.

```yaml
deploy-cloud-schedule:
    needs: [deploy-buckets, deploy-dataproc-workflow-template]
    runs-on: ubuntu-22.04
    timeout-minutes: 10

    steps:
    - name: Checkout
      uses: actions/checkout@v4
    
    - name: Authorize GCP
      uses: 'google-github-actions/auth@v2'
      with:
        credentials_json:  ${{ secrets.GCP_SA_KEY }}
    
    # Step to Authenticate with GCP
    - name: Set up Cloud SDK
      uses: google-github-actions/setup-gcloud@v2
      with:
        version: '>= 363.0.0'
        project_id: ${{ secrets.PROJECT_ID }}

    # Step to Configure Docker to use the gcloud command-line tool as a credential helper
    - name: Configure Docker
      run: |-
        gcloud auth configure-docker


    - name: Create service account
      run: |-
      
        if ! gcloud iam service-accounts list | grep -i ${{ env.SERVICE_ACCOUNT_NAME}} &> /dev/null; \
          then \
            gcloud iam service-accounts create ${{ env.SERVICE_ACCOUNT_NAME }} \
            --display-name="scheduler dataproc workflow service account"
          fi
    - name: Create Custom role for service account
      run: |-
        if ! gcloud iam roles list --project ${{ secrets.PROJECT_ID }} | grep -i ${{ env.CUSTOM_ROLE }} &> /dev/null; \
          then \
            gcloud iam roles create ${{ env.CUSTOM_ROLE }} --project ${{ secrets.PROJECT_ID }} \
            --title "Dataproc Workflow template scheduler" --description "Dataproc Workflow template scheduler" \
            --permissions "dataproc.workflowTemplates.instantiate,iam.serviceAccounts.actAs" --stage ALPHA
          fi    

    - name: Add the custom role for service account
      run: |-
        gcloud projects add-iam-policy-binding ${{secrets.PROJECT_ID}} \
        --member=serviceAccount:${{env.SERVICE_ACCOUNT_NAME}}@${{secrets.PROJECT_ID}}.iam.gserviceaccount.com \
        --role=projects/${{secrets.PROJECT_ID}}/roles/${{env.CUSTOM_ROLE}}

    - name: Create cloud schedule for workflow execution
      run: |-
        if ! gcloud scheduler jobs list --location ${{env.REGION}} | grep -i ${{env.SCHEDULE_NAME}} &> /dev/null; \
          then \
            gcloud scheduler jobs create http ${{env.SCHEDULE_NAME}} \
            --schedule="30 12 * * *" \
            --description="Dataproc workflow " \
            --location=${{env.REGION}} \
            --uri=https://dataproc.googleapis.com/v1/projects/${{secrets.PROJECT_ID}}/regions/${{env.REGION}}/workflowTemplates/${{env.DATAPROC_WORKFLOW_NAME}}:instantiate?alt=json \
            --time-zone=${{env.TIME_ZONE}} \
            --oauth-service-account-email=${{env.SERVICE_ACCOUNT_NAME}}@${{secrets.PROJECT_ID}}.iam.gserviceaccount.com
          fi
```


## Resources Created After Deployment

Upon deployment, the following resources are created:

### Google Cloud Storage Bucket

At the end of the deployment process, several Cloud Storage buckets are created: one bucket for storing data related to the data lake, another for the Dataproc cluster, one for the PySpark scripts and libraries used in the project and one for BigQuery Temporary files generated in load process . The Dataproc service itself creates a cluster to manage temporary data generated during processing.


![cloud storage](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8egg4eg3jeonb1bwuu9q.JPG)

### Dataproc Cluster

Now Dataproc service shows a new Workflow template, the picture above shows 2 templates. At the the Workflow tab, is possible to explore some options, as monitoring workflow executions and analyzing their details.


![dataproc-workflow1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/smp4rsn1x7x5paazy75e.JPG)

Selecting the created workflow, is possible to see the cluster used for processing and workflow's steps, dependencies between the steps. 


![dataproc-workflow2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/e0vypblqtao6k13v8lfh.JPG)

With Dataproc Service, is possible monitoring the execution status of each job, with individual detail about each execution, its performance , a example is displayed below.


![dataproc-workflow3](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jj0payqwvuca6pq1vyq1.JPG)

### BigQuery Dataset

In the image below the bigQuery DataSet is displayed, in this case we have just one table, with several columns of different numeric types, but it is possible to have several other datasets in the same project, as well as countless other tables, procedures, views and functions.

![Big Query1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rtuezk6zshzxxgxbxd6g.JPG)

The result of a query is demonstrated, in this case the query returns all columns in the table, using the column partitioned in the clause where is always a good practice to avoid excessive costs, as Biq Query charges for data processed in the query and stored data, As the data used in the experiment is small and I used a Trial account, there was no cost for the consultation

![Big Query2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/htr8eqw0u0j3qn5kfiz9.JPG)


### Cloud Scheduler Job

The cloud scheduler shows that there are 2 dataproc Workflow schedules, which automate the entire data ingestion, transformation and enrichment process in an orchestrated manner and with scheduled execution.
It is possible to force the execution of any schedule manually, by selecting the desired Cloud Scheduler and clicking on the "FORCE RUN" button, so it is possible to modify the scheduling time in "EDIT"


![Cloud Schedule](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/x74p6oys3q5n66vx2ojf.JPG)

## Conclusion<a name="Conclusion"></a>

This project demonstrates how Google Cloud’s Dataproc, BigQuery, Cloud Storage, and Cloud Scheduler can be integrated to create a scalable, automated data ingestion pipeline. By leveraging GitHub Actions for CI/CD, the project ensures streamlined deployment, robust automation, and seamless workflows. This setup can be adapted to suit various use cases in big data processing, enabling organizations to process, store, and analyze large datasets efficiently.

Links and References
[GitHub Repo](https://github.com/jader-lima/gcp-dataproc-bigquery-workflow-template)
[Big Query](https://cloud.google.com/bigquery/docs)
[DataProc](https://cloud.google.com/dataproc/docs)
[Cloud Scheduler](https://cloud.google.com/scheduler/docs)
[Wrokflows](https://cloud.google.com/dataproc/docs/concepts/workflows/workflow-schedule-solutions)