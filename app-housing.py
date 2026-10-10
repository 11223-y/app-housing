import streamlit as st
import pandas as pd

# 读取数据
df = pd.read_csv("housing.csv")

# 1. 标题（把 [Your Name] 换成你的名字）
st.title("California Housing Data (1990) by Qiu")

# 2. 滑块：最小 median_house_value
min_value = st.slider(
    "Minimal Median House Value",
    min_value=0,
    max_value=500001,
    value=200000,
    step=1
)

# 3. 子标题
st.subheader("See more filters in the sidebar:")

# 4. 侧边栏：多选 ocean_proximity
all_locations = sorted(df["ocean_proximity"].dropna().unique().tolist())
selected_locations = st.sidebar.multiselect(
    "Choose the location type",
    options=all_locations,
    default=all_locations
)

# 5. 侧边栏：单选收入水平
income_level = st.sidebar.radio(
    "Choose income level",
    options=["Low", "Medium", "High"]
)

# 根据滑块过滤
filtered_df = df[df["median_house_value"] >= min_value]

# 根据多选过滤
filtered_df = filtered_df[filtered_df["ocean_proximity"].isin(selected_locations)]

# 根据单选过滤 median_income
if income_level == "Low":
    filtered_df = filtered_df[filtered_df["median_income"] <= 2.5]
elif income_level == "Medium":
    filtered_df = filtered_df[
        (filtered_df["median_income"] > 2.5) & (filtered_df["median_income"] < 4.5)
    ]
else:  # High
    filtered_df = filtered_df[filtered_df["median_income"] >= 4.5]

# 6. 地图
st.map(filtered_df, latitude="latitude", longitude="longitude")

# 7. 直方图
st.subheader("Histogram of Median House Value")
hist_values = filtered_df["median_house_value"]
st.histogram_chart(hist_values, bins=30)