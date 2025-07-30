# 🚧 SCT\_DS\_4

# Task 04: Traffic Accident Analysis – Visualization & Mapping

This project performs **exploratory data analysis and visualization** on a U.S. traffic accident dataset. It highlights trends in accidents by time, weather conditions, and location, and uses geospatial mapping for better insight.

---

## 🧾 Objective

To visualize and analyze **traffic accident patterns** in the United States using:

* Temporal data (hour of day, day of week)
* Environmental factors (weather)
* Geographic coordinates (latitude and longitude)

---

## 📁 Files Included

* `Task04.py` – Python script for full analysis and plotting
* `US_Accidents_Dataset.csv` – Dataset with traffic accident records
* `accident_visuals/` – Folder containing generated graphs:

  * `accidents_by_hour.png`
  * `accidents_by_weather.png`
  * `accidents_by_weekday.png`
  * `accident_hotspots_map.html`

---

## 📊 Data Source

* [US Accidents (2016–2021)](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents) – by Sobhan Moosavi on Kaggle

  > Over 2.8 million accident records from across the United States

---

## 🔍 Data Overview

Key columns used in the project:

| Column                  | Description                       |
| ----------------------- | --------------------------------- |
| `Start_Time`            | Timestamp when accident started   |
| `Weather_Condition`     | Weather condition during accident |
| `Latitude`, `Longitude` | Geolocation of the accident       |

---

## 📈 Visualizations

The following plots are generated:

### 🕒 Accidents by Hour

Shows peak accident times.

> Insight: Accidents spike during **rush hours** (7–9 AM and 4–6 PM)

### 🌧️ Accidents by Weather Condition

Highlights weather-related risks.

> Insight: Most accidents happen during **Clear**, **Overcast**, and **Rain** conditions.

### 📅 Accidents by Weekday

Compares accident counts by day of the week.

> Insight: Higher accident frequency on **weekdays**, especially **Fridays**.

### 🗺️ Interactive Accident Hotspots Map

Using `folium`, an interactive map plots 500 random accident locations.

> Insight: Major clusters in **California**, **Florida**, and **Texas**.

---

## 🛠️ Technologies Used

* Python
* Libraries:

  * `pandas` – Data manipulation
  * `matplotlib`, `seaborn` – Static plotting
  * `folium` – Geospatial mapping
  * `os` – Directory handling
  * `warnings` – Warning control

---

## ⚙️ How to Run

1. Install the required packages:

   ```bash
   pip install pandas matplotlib seaborn folium
   ```

2. Run the script:

   ```bash
   python Task04.py
   ```

3. Output files will be saved in the `accident_visuals/` folder.

---

## 📌 Key Learnings

* Visual trends help **identify risk patterns** in road safety.
* Geospatial plots enhance **location-based decision-making**.
* Data preprocessing and plotting must consider **missing values** and **categorical encoding**.

---

## 📄 License

This project is shared under the **MIT License**.
