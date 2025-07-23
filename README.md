# **Customer-Data-Analytics**

**Role:** GCP Data Engineer  
**Objective:** End-to-end data pipeline on Google Cloud Platform using Cloud Storage, BigQuery, and Cloud Composer (Airflow) for batch processing and customer analytics.

---

## 📝 **Project Description**

This project is focused on designing and implementing a GCP-based data analytics pipeline to handle structured customer data for a travel-related business. The system ingests and processes customer booking data to deliver actionable insights for business growth.

---

## **Key Goals**

- **Analyze** customer demographics (age, place, state, country)
- **Track** customer booking patterns by date and region
- **Identify** high-value customers based on activity and engagement
- **Enhance** business decisions through data-driven customer profiling
- **Monitor** trends across states and optimize campaigns accordingly

---

## **Dataset**

**customer_data.csv**  
This dataset includes customer information such as:

| Column         | Description                  |
|:---------------|:----------------------------|
| `customer_id`  | Unique ID for each customer |
| `customer_name`| Name of the customer        |
| `age`          | Age                         |
| `place`        | City/Town                   |
| `state`        | State                       |
| `country`      | Country                     |
| `mobile`       | Mobile Number               |
| `book_date`    | Booking Date                |

---

## **Technologies Used**

- **Cloud:** Google Cloud Platform (GCP)
- **Data Lake:** Google Cloud Storage (GCS)  
  Stores raw and processed customer data for scalable access.
- **CLI Tools:** `gsutil`, `gcloud`, `bq`  
  For managing buckets, services, and BigQuery datasets.
- **Orchestration:** Cloud Composer (Airflow)  
  Building and automating workflows — from data ingestion to transformation.
- **Data Warehouse:** Google BigQuery  
  Storing transformed customer data and running efficient analytical queries.
- **Transformation Engine:** PySpark  
  Cleansing, filtering, and transforming customer data before loading to BigQuery.
- **Visualization:** Looker Studio (Google Data Studio)  
  Dashboards for booking trends, age demographics, and customer engagement metrics.

---

## **Procedure**

1. **Data Acquisition:**  
   Downloaded `customer_data.csv` from the source system or received as daily batch files.

2. **Architecture Design:**  
   Designed a scalable GCP architecture for ingestion, transformation, and reporting.

3. **Data Pipeline Implementation:**  
   Developed an Airflow DAG in Cloud Composer to:
   - Upload raw data to a GCS bucket (Data Lake)
   - Trigger transformations using PySpark (or optionally Dataflow)
   - Load transformed data into BigQuery tables

4. **ETL Process & Analytics Preparation:**  
   Implemented ETL logic to clean and standardize fields (e.g., formatting mobile numbers, parsing booking dates), followed by loading into BigQuery for analysis.

5. **Reporting:**  
   Built dashboards in Looker Studio to provide insights into:
   - Customer activity by region and age group
   - Daily/monthly booking trends
   - Customer growth across states/countries

---

## **Workflow Diagram**

<img width="500" alt="workflow" src="" />

