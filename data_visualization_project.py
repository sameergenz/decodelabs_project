import os
import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = "Dataset for Data Analytics (3)(1).xlsx"
OUTPUT_DIR = "project_output"
CHART_DIR = os.path.join(OUTPUT_DIR, "charts")
os.makedirs(CHART_DIR, exist_ok=True)

df = pd.read_excel(INPUT_FILE)

# Data cleaning
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.drop_duplicates().copy()
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.to_period("M").astype(str)

print("Dataset shape:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# Save cleaned data
df.to_csv(os.path.join(OUTPUT_DIR, "cleaned_orders.csv"), index=False)

# 1. Revenue by Product
product = df.groupby("Product")["TotalPrice"].sum().sort_values()
ax = product.plot(kind="barh", figsize=(10,6), title="Revenue by Product")
ax.set_xlabel("Revenue")
ax.set_ylabel("Product")
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "01_revenue_by_product.png"), dpi=160)
plt.close()

# 2. Year-wise Revenue
year = df.groupby("Year")["TotalPrice"].sum()
ax = year.plot(kind="bar", figsize=(10,6), title="Year-wise Revenue")
ax.set_xlabel("Year")
ax.set_ylabel("Revenue")
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "02_year_wise_revenue.png"), dpi=160)
plt.close()

# 3. Monthly Revenue Trend
monthly = df.groupby("Month")["TotalPrice"].sum()
ax = monthly.plot(kind="line", marker="o", figsize=(10,6), title="Monthly Revenue Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
plt.xticks(rotation=60)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "03_monthly_revenue_trend.png"), dpi=160)
plt.close()

# 4. Order Status
status = df["OrderStatus"].value_counts()
status.plot(kind="pie", autopct="%1.1f%%", startangle=90, figsize=(8,8), title="Order Status Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "04_order_status_distribution.png"), dpi=160)
plt.close()

# 5. Payment Method
payment = df["PaymentMethod"].value_counts()
ax = payment.plot(kind="bar", figsize=(10,6), title="Orders by Payment Method")
ax.set_xlabel("Payment Method")
ax.set_ylabel("Number of Orders")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "05_payment_method.png"), dpi=160)
plt.close()

# 6. Referral Source Revenue
referral = df.groupby("ReferralSource")["TotalPrice"].sum().sort_values()
ax = referral.plot(kind="barh", figsize=(10,6), title="Revenue by Referral Source")
ax.set_xlabel("Revenue")
ax.set_ylabel("Referral Source")
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "06_referral_source_revenue.png"), dpi=160)
plt.close()

# 7. Quantity Distribution
ax = df["Quantity"].plot(kind="hist", bins=10, figsize=(10,6), title="Quantity Distribution per Order")
ax.set_xlabel("Quantity")
ax.set_ylabel("Frequency")
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "07_quantity_distribution.png"), dpi=160)
plt.close()

# 8. Coupon Usage
coupon = df["CouponCode"].value_counts()
ax = coupon.plot(kind="bar", figsize=(10,6), title="Coupon Usage")
ax.set_xlabel("Coupon")
ax.set_ylabel("Number of Orders")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "08_coupon_usage.png"), dpi=160)
plt.close()

print("\nProject completed. Check the project_output folder for charts and cleaned data.")
