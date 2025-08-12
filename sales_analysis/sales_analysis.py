import pandas as pd
from datetime import datetime

def load_sales_data(file_path):
    """Load sales data from CSV file"""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return None

def calculate_total_revenue(df):
    """Calculate total revenue from sales data"""
    return df['Revenue ($)'].sum()

def find_best_selling_product(df):
    """Find the product with highest quantity sold"""
    best_product = df.loc[df['Quantity Sold'].idxmax()]
    return best_product['Product'], best_product['Quantity Sold']

def find_highest_sales_day(df):
    """Find the day with highest total revenue"""
    daily_sales = df.groupby('Date')['Revenue ($)'].sum()
    highest_day = daily_sales.idxmax()
    highest_amount = daily_sales.max()
    return highest_day, highest_amount

def generate_summary(total_revenue, best_product, best_quantity, highest_day, highest_amount):
    """Generate summary text for output"""
    summary = f"""Sales Data Analysis Summary
{'='*30}
Total Revenue: ${total_revenue:,.2f}
Best-Selling Product: {best_product} ({best_quantity} units sold)
Highest Sales Day: {highest_day} (${highest_amount:,.2f})
"""
    return summary

def save_summary_to_file(summary_text, output_file):
    """Save summary to text file"""
    try:
        with open(output_file, 'w') as file:
            file.write(summary_text)
        print(f"Summary saved to {output_file}")
    except Exception as e:
        print(f"Error saving summary file: {e}")

def main():
    # File paths
    input_file = 'sales_data.csv'
    output_file = 'sales_summary.txt'
    
    # Load data
    print("Loading sales data...")
    sales_df = load_sales_data(input_file)
    
    if sales_df is None:
        return
    
    # Convert Date column to datetime if it's not already
    sales_df['Date'] = pd.to_datetime(sales_df['Date'])
    
    # Perform analysis
    print("Analyzing sales data...")
    total_revenue = calculate_total_revenue(sales_df)
    best_product, best_quantity = find_best_selling_product(sales_df)
    highest_day, highest_amount = find_highest_sales_day(sales_df)
    
    # Generate and display summary
    summary = generate_summary(total_revenue, best_product, best_quantity, 
                             highest_day, highest_amount)
    print("\n" + summary)
    
    # Save summary to file
    save_summary_to_file(summary, output_file)
    
    # Bonus: Visualization
    try:
        import matplotlib.pyplot as plt
        
        print("\nGenerating sales visualization...")
        
        # Daily sales trend
        daily_sales = sales_df.groupby('Date')['Revenue ($)'].sum()
        
        plt.figure(figsize=(10, 5))
        daily_sales.plot(kind='line', marker='o', color='b')
        plt.title('Daily Sales Trend')
        plt.xlabel('Date')
        plt.ylabel('Revenue ($)')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('daily_sales_trend.png')
        print("Saved visualization to 'daily_sales_trend.png'")
        
        # Product sales breakdown
        product_sales = sales_df.groupby('Product')['Quantity Sold'].sum()
        
        plt.figure(figsize=(8, 8))
        product_sales.plot(kind='pie', autopct='%1.1f%%')
        plt.title('Product Sales Distribution')
        plt.ylabel('')
        plt.tight_layout()
        plt.savefig('product_sales_distribution.png')
        print("Saved visualization to 'product_sales_distribution.png'")
        
    except ImportError:
        print("\nMatplotlib not available. Skipping visualization.")
    except Exception as e:
        print(f"\nError generating visualization: {e}")

if __name__ == "__main__":
    main()
