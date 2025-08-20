# 🏏 Cricsheet Match Data Analysis  

![Banner](./reports/screenshots/banner.png)

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)  
![MySQL](https://img.shields.io/badge/Database-MySQL-blue?logo=mysql)  
![Power BI](https://img.shields.io/badge/BI-Power%20BI-yellow?logo=powerbi)  
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)  

---

## 📌 Project Overview  
This project is a **sports analytics pipeline** built on cricket match data from [Cricsheet](https://cricsheet.org/matches/).  

It demonstrates an **end-to-end data workflow**:  
- **Data Collection** → Download JSON data (Tests, ODIs, T20s, IPL).  
- **Data Transformation** → Parse JSON into structured DataFrames & CSVs.  
- **Database Management** → Store matches in a relational MySQL database.  
- **SQL Analysis** → 20 analytical queries for insights.  
- **EDA (Python)** → Visualize patterns with Matplotlib, Seaborn, Plotly.  
- **Dashboard (Power BI)** → Interactive report with KPIs, team/player insights.  

---

## 🎯 Skills & Tools
- **Python** → Pandas, Requests, Matplotlib, Seaborn, Plotly  
- **SQL** → MySQL, SQLAlchemy, Analytical Queries  
- **Power BI** → Interactive Dashboards, KPIs, Data Storytelling  
- **Other Tools** → GitHub, JSON handling, Data Modeling (Star Schema)  


---

## 📊 Workflow  

1️⃣ **Data Collection**  
- Download full ZIPs from [Cricsheet](https://cricsheet.org/downloads/).  
- Extract JSONs into `data/raw/`.  

2️⃣ **Data Transformation**  
- Convert JSON → Pandas DataFrames.  
- Save structured CSVs into `data/cleaned/`.  

3️⃣ **Database Management**  
- Load cleaned CSVs into MySQL (`cricsheet_db`).  
- Tables: `test_matches`, `odi_matches`, `t20_matches`, `ipl_matches`.  
- Built **star schema**: Fact_Matches + Teams + Players + Calendar.  

4️⃣ **SQL Analysis**  
- Wrote 20 SQL queries (e.g., top players, win %, toss impact).  
- Stored in `src/database/queries.sql`.  

5️⃣ **Exploratory Data Analysis (EDA)**  
- 10+ Python visualizations: win distributions, toss decisions, runs over time, venue analysis.  

6️⃣ **Power BI Dashboard**  
- **4 Pages**: Overview | Teams | Players | Matches  
- KPIs: Total Matches, Win %, Toss Impact, Player Awards  
- Filters: Teams, Match Format, Year  

---

## 📈 Sample Visualizations  

📌 *EDA plots:*  
- **Wins by Team (Bar Chart)**  
- **Toss Decision Distribution (Pie)**  
- **Matches Over Time (Line)**  
- **Venue-wise Performance (Heatmap)**  

📌 *Power BI Dashboard screenshots:*  
- **Page 1: Overview**  
- **Page 2: Team Insights**  
- **Page 3: Player Insights**  
- **Page 4: Match Trends**  

---

## 🏆 Key Insights
- Certain teams dominate specific formats (e.g., Australia in Tests, India in T20s).  
- Toss has a measurable impact on results, especially in ODIs.  
- Some venues consistently favor batting or bowling.  
- A small set of players win most "Player of the Match" awards.  

---

## ⚡ Results
- Automated pipeline from **Cricsheet JSON → SQL → Power BI**.  
- 4 **MySQL tables** + star schema for analysis.  
- 20 SQL queries with meaningful insights.  
- 10+ Python EDA visualizations.  
- 4-page Power BI interactive dashboard.  

---


