#movie recommendation system
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# -----------------------------
# 1. Load Datasets
# -----------------------------
ratings_cols = ["user_id", "item_id", "rating", "timestamp"]
ratings = pd.read_csv("ratings.csv", sep="\t", names=ratings_cols)

movies = pd.read_csv("movies.csv")   # Ensure movies.csv has columns: item_id, title

# Merge datasets
df = pd.merge(ratings, movies, on="item_id")
print("Merged Dataset:\n", df.head())

# -----------------------------
# 2. Exploratory Data Analysis
# -----------------------------
# Average rating for each movie
ratings_mean = df.groupby("title")["rating"].mean()

# Number of ratings for each movie
ratings_count = df.groupby("title")["rating"].count()

# Create ratings dataframe
ratings_df = pd.DataFrame({
    "rating": ratings_mean,
    "num_of_ratings": ratings_count
})

print("\nRatings DataFrame:\n", ratings_df.head())

# Visualizations
plt.figure(figsize=(10, 4))
ratings_df["num_of_ratings"].hist(bins=70)
plt.title("Distribution of Number of Ratings")
plt.show()

plt.figure(figsize=(10, 4))
ratings_df["rating"].hist(bins=70)
plt.title("Distribution of Average Ratings")
plt.show()

sns.jointplot(x="rating", y="num_of_ratings", data=ratings_df, alpha=0.5)
plt.show()

# -----------------------------
# 3. Create User-Movie Matrix
# -----------------------------
movie_matrix = df.pivot_table(index="user_id", columns="title", values="rating")
print("\nUser-Movie Matrix:\n", movie_matrix.head())

# -----------------------------
# 4. Collaborative Filtering
# -----------------------------
# Example: Find movies similar to "Star Wars (1977)" if it exists
def get_recommendations(movie_name, min_ratings=100):
    if movie_name not in movie_matrix.columns:
        return f"Movie '{movie_name}' not found in dataset."

    # Ratings of the target movie
    movie_ratings = movie_matrix[movie_name]

    # Correlation with other movies
    similar_to_movie = movie_matrix.corrwith(movie_ratings)

    # Build DataFrame
    corr_movie = pd.DataFrame(similar_to_movie, columns=["Correlation"])
    corr_movie.dropna(inplace=True)

    # Join with num_of_ratings
    corr_movie = corr_movie.join(ratings_df["num_of_ratings"])

    # Filter for movies with enough ratings
    recommendations = corr_movie[corr_movie["num_of_ratings"] > min_ratings] \
                        .sort_values("Correlation", ascending=False)

    return recommendations.head(10)


# -----------------------------
# 5. Example Usage
# -----------------------------
movie_input = "Star Wars (1977)"
print(f"\nTop Recommendations for '{movie_input}':\n")
print(get_recommendations(movie_input))



