
# 📊 Sales Data Analysis Project

## 📌 Overview
A Python solution for performing basic data analysis on sales records with visualization capabilities.

## ✨ Features
- Calculates total revenue
- Identifies best-selling products
- Finds peak sales days
- Generates visual sales trends
- Exports results to text and image files

## 🛠️ Technologies
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-1.0+-blue?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.0+-blue?logo=matplotlib)

## 📂 File Structure
```
project/
├── sales_analysis.py       # Main analysis script
├── sales_data.csv          # Sample input data
├── sales_summary.txt       # Generated text report
└── sales_trend.png         # Generated visualization
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip package manager

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sales-analysis.git
   cd sales-analysis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
Run the analysis:
```bash
python sales_analysis.py
```

## 📊 Sample Output

### Text Report (`sales_summary.txt`)
```
Total Revenue: $9,100
Best-Selling Product: Mouse (15 units sold) 
Highest Sales Day: 2025-03-01
```

### Visualization Example
![Sales Trend Chart](sales_trend.png)

##   Troubleshooting
**Issue**: Missing dependencies  
**Solution**:  
```bash
pip install pandas matplotlib
```

**Issue**: File not found  
**Solution**: Verify `sales_data.csv` exists in the same directory

## 📝 Customization
To modify the analysis:
1. Edit column names in `sales_analysis.py` if your CSV uses different headers
2. Adjust visualization parameters in the matplotlib section




## ✉️ Author
Ifeanyi Ekezie 
