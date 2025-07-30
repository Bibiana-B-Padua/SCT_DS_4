import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import os

# Create output folder
output_dir = "accident_visuals"
os.makedirs(output_dir, exist_ok=True)

# Load dataset
df = pd.read_csv("US_Accidents_March23.csv")  # Replace with your real CSV file name

# Show all column names (for debug, optional)
print("Available columns:", df.columns.tolist())

# Convert Start_Time to datetime
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df['Hour'] = df['Start_Time'].dt.hour
df['Weekday'] = df['Start_Time'].dt.day_name()

# ----------------------------------
# 1. Accidents by Hour of the Day
# ----------------------------------
plt.figure(figsize=(10,6))
sns.countplot(x='Hour', data=df, hue='Hour', palette='coolwarm', legend=False)
plt.title('Accidents by Hour of the Day')
plt.xlabel('Hour')
plt.ylabel('Number of Accidents')
plt.grid(True)
plt.tight_layout()
plt.savefig(f"{output_dir}/accidents_by_hour.png")
plt.close()

# ----------------------------------
# 2. Accidents by Weather Condition
# ----------------------------------
plt.figure(figsize=(12,6))
top_weather = df['Weather_Condition'].value_counts().nlargest(10).index
sns.countplot(
    y='Weather_Condition',
    data=df[df['Weather_Condition'].isin(top_weather)],
    hue='Weather_Condition',
    order=top_weather,
    palette='magma',
    legend=False
)
plt.title('Top 10 Weather Conditions During Accidents')
plt.xlabel('Number of Accidents')
plt.ylabel('Weather Condition')
plt.tight_layout()
plt.savefig(f"{output_dir}/accidents_by_weather.png")
plt.close()

# ----------------------------------
# 3. Accidents by Day of the Week
# ----------------------------------
plt.figure(figsize=(8,5))
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sns.countplot(
    x='Weekday',
    data=df,
    hue='Weekday',
    order=weekday_order,
    palette='Set2',
    legend=False
)
plt.title('Accidents by Day of the Week')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{output_dir}/accidents_by_weekday.png")
plt.close()

# ----------------------------------
# 4. Interactive Accident Hotspot Map
# ----------------------------------
# ✅ Use correct latitude/longitude column names
if 'Start_Lat' in df.columns and 'Start_Lng' in df.columns:
    sample = df[['Start_Lat', 'Start_Lng']].dropna().sample(n=500, random_state=42)

    accident_map = folium.Map(
        location=[sample['Start_Lat'].mean(), sample['Start_Lng'].mean()],
        zoom_start=5
    )

    for _, row in sample.iterrows():
        folium.CircleMarker(
            location=[row['Start_Lat'], row['Start_Lng']],
            radius=2,
            color='red',
            fill=True,
            fill_opacity=0.6
        ).add_to(accident_map)

    map_path = f"{output_dir}/accident_hotspots_map.html"
    accident_map.save(map_path)
    print(f"Map saved at: {map_path}")

else:
    print("❌ Latitude and Longitude columns not found. Skipping map.")

print(f"✅ Visuals saved in the folder: {output_dir}")
