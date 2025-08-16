# 🛍️ Customer Segmentation using K-Means Clustering

## 📌 Project Overview
This project applies **K-Means Clustering** to the **Mall Customers dataset** to identify distinct customer groups based on:
- Age
- Annual Income
- Spending Score

This technique is useful for **customer segmentation**, allowing businesses to design targeted marketing strategies.

---

## How It Works
1. Load the Mall Customers dataset.
2. Select key features (`Age`, `Annual Income`, `Spending Score`).
3. Standardize features using **StandardScaler**.
4. Apply the **Elbow Method** to find the optimal number of clusters.
5. Train the **K-Means algorithm**.
6. Visualize customer segments in 3D.
7. Analyze cluster centers to understand customer profiles.

---

## Files
- `Mall_Customers.csv` → dataset
- `kmeans_customer.py` → main script
- `README.md` → documentation

---

## Requirements
- Install dependencies before running the script:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn


 ##Running the Project

- Run the script in VS Code or terminal:

python kmeans_customer.py

## Example Output

1. Elbow curve showing optimal clusters.

2. 3D scatter plot of customer groups.

3. Cluster centers with average age, income, and spending score.

## Applications

- Personalized marketing

- Targeted promotions

- Customer behavior analysis

- Retail & e-commerce strategies
