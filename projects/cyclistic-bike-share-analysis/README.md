# Cyclistic Bike-Share Analysis

## Project Overview

This project analyzes bike-share usage data from Cyclistic to identify differences in riding behavior between **annual members** and **casual riders**.

The analysis follows a structured data analysis workflow, including data validation, data cleaning, transformation, exploratory data analysis, and visualization.

The main objective is to understand how different user groups use the bike-share service and identify patterns that can support data-driven business decisions.

---

## Business Question

**How do annual members and casual riders use Cyclistic bikes differently?**

Understanding differences in riding behavior between these two user groups can help identify patterns in bike usage and provide insights for customer engagement and membership strategies.

---

## Objectives

The main objectives of this project are to:

* Compare riding behavior between annual members and casual riders.
* Analyze differences in ride duration.
* Examine bike type usage by user type.
* Identify temporal patterns in bike usage.
* Assess the quality and consistency of the available data.
* Identify missing values and anomalous records.
* Transform the data into a format suitable for analysis.
* Generate data-driven insights from the available ride records.

---

## Dataset

The project uses historical Cyclistic bike-share trip data.

The analysis covers monthly datasets from:

**August 2025 through July 2026**

Each monthly dataset contains the following 13 columns:

| Column               | Description                         |
| -------------------- | ----------------------------------- |
| `ride_id`            | Unique identifier for each ride     |
| `rideable_type`      | Type of bike used                   |
| `started_at`         | Date and time when the ride started |
| `ended_at`           | Date and time when the ride ended   |
| `start_station_name` | Starting station name               |
| `start_station_id`   | Starting station identifier         |
| `end_station_name`   | Ending station name                 |
| `end_station_id`     | Ending station identifier           |
| `start_lat`          | Starting station latitude           |
| `start_lng`          | Starting station longitude          |
| `end_lat`            | Ending station latitude             |
| `end_lng`            | Ending station longitude            |
| `member_casual`      | User type: member or casual         |

The monthly datasets were checked to ensure that their schemas were consistent before being combined for analysis.

---

## Tools & Technologies

* **Python**
* **Pandas**
* **Matplotlib**
* **Jupyter Notebook**
* **GitHub**

---

## Project Workflow

The project follows these main stages:

```text
Data Collection
      ↓
Data Loading
      ↓
Schema Validation
      ↓
Data Quality Assessment
      ↓
Data Cleaning
      ↓
Data Transformation
      ↓
Exploratory Data Analysis
      ↓
Data Visualization
      ↓
Insights & Conclusions
```

---

## 1. Data Loading

The monthly datasets were loaded into Python using Pandas.

The files were initially kept separate to validate their structure before combining them into a single dataset.

---

## 2. Schema Validation

Before combining the monthly datasets, their structures were compared to verify that:

* Column names were consistent.
* The same 13 columns were present.
* Data types were appropriate.
* The monthly datasets could be safely combined.

This step was important to prevent structural inconsistencies from affecting the analysis.

---

## 3. Data Quality Assessment

The datasets were evaluated for several common data-quality issues:

* Missing values
* Duplicate records
* Invalid values
* Inconsistent data types
* Negative ride durations
* Potential outliers
* Date and time inconsistencies

Data quality was assessed before performing the main exploratory analysis.

---

## 4. Missing Value Analysis

Station-related columns contain a significant number of missing values.

For example, the analysis identified:

* **Total rides:** 6,037,805
* **Missing start station:** 1,273,163
* **Available start station:** 4,764,642
* **Missing start station:** 21.09%
* **Available start station:** 78.91%

Because station information is not available for every ride, station-level analyses need to account for missing values.

Missing station information was not automatically interpreted as an error because the absence of a station value does not necessarily mean that the ride record itself is invalid.

---

## 5. Date and Time Transformation

The `started_at` and `ended_at` columns were converted into datetime format to allow temporal analysis.

Additional variables were created from the original timestamps, including:

* Ride duration
* Month
* Year
* Day of week
* Hour

These variables were used to identify differences in riding patterns across time.

---

## 6. Ride Duration

Ride duration was calculated using the difference between the ride start and end timestamps.

This variable was used to compare the duration of rides made by:

* Annual members
* Casual riders

Ride duration was also investigated for potentially invalid values.

---

## 7. Anomaly Investigation

During the data-quality assessment, negative ride durations were identified in the November 2025 dataset.

A total of **29 negative ride-duration records** were identified.

These records occurred around **November 2, 2025**, during the daylight-saving time transition.

Rather than automatically deleting these records, they were investigated in context to determine whether they represented data errors or timestamp-related effects.

This highlights the importance of investigating anomalies before removing records from a dataset.

---

## 8. Exploratory Data Analysis

The exploratory analysis focuses on several dimensions of bike usage.

### User Type

Ride activity is compared between:

* Annual members
* Casual riders

This comparison helps identify differences in overall usage patterns.

### Bike Type

The analysis examines how different bike types are used by each user group.

This allows potential differences in bike preferences between members and casual riders to be explored.

### Ride Duration

Ride duration is analyzed by user type to identify differences in how long members and casual riders use the service.

### Temporal Patterns

Ride activity is analyzed by:

* Month
* Day of week
* Hour of day

These comparisons help identify periods of higher and lower bike usage.

---

## 9. Visualizations

The project uses Matplotlib to create visualizations for the exploratory analysis.

The visualizations include analyses such as:

* Rides by user type
* Bike type usage
* Ride duration
* Monthly ride activity
* Weekly ride activity
* Hourly ride activity
* Comparisons between members and casual riders

Example visualizations will be included in the `images/` directory.

---

## 10. Key Questions

The analysis investigates questions such as:

1. Which user type accounts for more rides?
2. How does ride duration differ between members and casual riders?
3. Which bike types are most frequently used?
4. Does bike type usage differ between user groups?
5. How does ride activity change throughout the year?
6. Which days of the week have the highest ride activity?
7. Which hours have the highest ride activity?
8. What differences can be observed between members and casual riders?
9. How do missing values affect station-level analysis?
10. Which data-quality issues need to be considered before drawing conclusions?

---

## 11. Key Findings

This section will summarize the main findings obtained from the exploratory analysis.

The findings will focus on measurable differences between annual members and casual riders, including:

* Ride volume
* Ride duration
* Bike type usage
* Temporal behavior
* Other relevant patterns identified during the analysis

> **Note:** Final findings and numerical results will be added after completing the exploratory analysis.

---

## 12. Data Quality Considerations

Several data-quality considerations were identified during the project.

### Missing Values

A significant percentage of rides do not contain start station information.

This limits the ability to perform complete station-level analysis using the full dataset.

### Negative Ride Durations

Negative ride durations were identified in November 2025 and investigated as potential timestamp-related anomalies.

### Schema Consistency

The monthly datasets were validated before being combined to ensure that their structures were compatible.

### Data Validation

Data-quality checks were performed before using the data for exploratory analysis to reduce the risk of drawing conclusions from invalid or inconsistent records.

---

## 13. Skills Demonstrated

This project demonstrates practical skills in:

* Python
* Pandas
* Matplotlib
* Jupyter Notebook
* Data cleaning
* Data validation
* Data quality assessment
* Exploratory data analysis
* Data transformation
* Datetime manipulation
* Missing-value analysis
* Anomaly investigation
* Aggregation and grouping
* Data visualization
* Analytical problem solving
* Documentation of analytical decisions

---

## 14. Project Structure

```text
cyclistic-bike-share-analysis/
│
├── README.md
│
├── notebooks/
│   └── data-trip.ipynb
│
└── images/
    ├── user_type_ride_volume.png
    ├── monthly_ride_volume_by_user_type.png
    ├── rides_by_day_of_week_and_user_type.png
    ├── rides_by_hour_and_user_type.png
    ├── bike_type_usage_by_user_type.png
    ├── top10_starting_stations_casual.png
    └── top10_starting_stations_member.png

```

---

## 15. Future Improvements

Potential future improvements include:

* Completing the final comparative analysis between user groups.
* Performing additional temporal analysis.
* Expanding station-level analysis using records with available station information.
* Investigating geographic patterns using latitude and longitude.
* Performing statistical comparisons between members and casual riders.
* Reproducing selected analyses using SQL.
* Adding additional data-quality validation.
* Improving the final project documentation with additional visualizations.

---

## 16. Conclusion

This project demonstrates an end-to-end approach to analyzing a large bike-share dataset.

The analysis does not focus only on visualization. It also emphasizes **data quality, validation, transformation, anomaly investigation, and analytical reasoning** before drawing conclusions.

Working through these stages helps ensure that the final insights are based on data that has been properly examined and prepared for analysis.

---

## Project Status

**Status:** In Progress

The analysis is currently being refined as additional exploratory analysis, visualizations, and findings are completed.

---

## Author

**Citlalli**

Chemical Engineer transitioning into Data Analytics and Data Engineering.

Interested in:

* Data Analysis
* Data Quality
* SQL
* Python
* Data Engineering
* Problem Solving
