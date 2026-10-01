# 🚲 Cyclistic Bike-Share Analysis

Analysis of **6,037,805 rides** (August 2025 – July 2026) to understand how **casual riders** and **annual members** use Cyclistic bikes differently, and how those differences could support a strategy to convert casual riders into members.

> Cyclistic is a fictional company from the Google Data Analytics case study. The data comes from Divvy (Chicago) and is used under its license.

**Tools:** Python, Pandas, NumPy, Matplotlib, Jupyter Notebook
**Full analysis:** [`notebooks/cyclistic_analysis.ipynb`](notebooks/cyclistic_analysis.ipynb)

---

## 📌 Business Question

How do casual riders and annual members use Cyclistic bikes differently, and how can these differences be used to design strategies to convert casual riders into annual members?

---

## 💡 Key Findings

| | Casual | Member |
|---|---:|---:|
| Share of rides | 35.6% | 64.4% |
| Median ride duration | 11.1 min | 8.6 min |
| Mean ride duration | 21.2 min | 12.4 min |
| Rides on Saturday + Sunday | 37.9% | 23.4% |
| Rides in May–July | 42.4% | 35.3% |
| Busiest month / quietest month (ratio) | 14.5× (Jul / Jan) | 4.5× (Jul / Dec) |
| Electric bikes | 71.5% | 67.1% |

1. **Members take more rides in every month**, but the casual share changes a lot with the season: from **18%** of rides in January to **41%** in July.
2. **Casual riders concentrate on weekends.** Saturday is their busiest day (457,395 rides) and casual riders account for **48%** of all Saturday rides. Members peak Tuesday to Thursday (Wednesday: 622,935 rides).
3. **Different hourly patterns.** Both groups peak at 5 p.m., but members also have a sharp morning peak: 7–8 a.m. plus 4–6 p.m. covers **41.5%** of member rides, against **32.3%** for casual riders. Casual activity builds gradually through the afternoon.
4. **Casual rides are longer and more variable.** Median 11.1 vs 8.6 minutes (about 29% higher), and an interquartile range of 14.1 vs 9.6 minutes.
5. **Casual starts are concentrated in a few lakefront and tourist locations.** Navy Pier alone has 54,838 casual rides (2.5% of all casual rides), 2.4× the top member station. Member starts are spread across downtown streets (Wells St, Clinton St, Canal St).
6. **Bike type does not separate the groups.** Electric bikes are the majority for both (71.5% vs 67.1%).

![Rides by user type](images/user_type_analysis.png)
![Temporal patterns](images/temporal_analysis.png)

---

## ✅ Recommendations

1. **Time membership communication around casual peaks:** Friday to Sunday and the warm months (May–August).
2. **Test membership offers at the top casual stations** (Navy Pier, DuSable Lake Shore Dr & Monroe St, Michigan Ave & Oak St), where casual ride volume is highest.
3. **Run it as an experiment, not a certainty.** Compare conversion between exposed and non-exposed casual riders before scaling. This analysis cannot show that any campaign works.

---

## 🧹 Data Cleaning & Validation

| Step | Result |
|---|---|
| 12 monthly files loaded, schema checked (same 13 columns) | 6,037,968 rows |
| Exact duplicate rides found after combining files and removed | 35 → 6,037,933 rows |
| Rides that started before Aug 1, 2025 (included in the August file) excluded from the study period | 128 → **6,037,805 rows** |
| Negative ride durations, all on Nov 2, 2025 (daylight-saving change) | 29 corrected (+60 min), not deleted |
| Rides of about 26 hours on Mar 7–8, 2026 (daylight-saving change) | 10 corrected (−60 min), not deleted |
| Rides shorter than 1 minute (valid timestamps, mostly e-bikes) | about 160,900 (≈2.7%), retained |
| Rides longer than 24 hours | about 5,300 (≈0.09%), retained |
| Missing start station / end station | 21.09% / 22.14%, retained |

Coordinates and categories (`member_casual`, `rideable_type`) were validated with no invalid values.

---

## ⚠️ Limitations

- **The data counts rides, not riders.** There are no user IDs, so unique users, repeat usage, and actual conversion cannot be measured.
- **Motivations are unknown.** Weekend and lakefront patterns are consistent with leisure use, but the data cannot confirm why people ride.
- **Station analysis covers 78.9% of rides** (those with a start station). Whether missing stations are spread evenly across user types has not been checked yet.
- **Timestamps have no time zone.** Daylight-saving problems were corrected only where they were detectable.
- **Very long and very short rides were kept.** The mean is sensitive to them, so medians are the main duration measure.
- **One year of data**, so year-to-year seasonality cannot be assessed.

---

## 📂 Data

- **Source:** [Divvy trip data](https://divvy-tripdata.s3.amazonaws.com/index.html), monthly files 202508 to 202607
- **License:** [Divvy Data License Agreement](https://divvybikes.com/data-license-agreement)
- Raw files are not included in this repository because of their size. See `data/README.md`.

## 📁 Repository Structure

```text
├── README.md
├── notebooks/   # cyclistic_analysis.ipynb
├── images/      # charts used in this README
└── data/        # download instructions only
```
