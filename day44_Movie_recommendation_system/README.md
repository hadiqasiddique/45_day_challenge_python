# 🎬 Movie Recommendation System (Python)

This is a **Movie Recommendation System** built in Python using **Collaborative Filtering**.  
It recommends movies similar to a given title based on user ratings.  

---

## Features
- Load and merge movie and ratings datasets
- Perform **Exploratory Data Analysis (EDA)** with visualizations:
  - Distribution of ratings
  - Distribution of number of ratings
  - Relationship between ratings and number of ratings
- Create a **User–Movie rating matrix**
- Implement **Collaborative Filtering** using correlation
- Generate top recommended movies for any given movie title

---

## Technologies Used
- **Python 3.8+**
- [pandas](https://pandas.pydata.org/) → data manipulation & cleaning  
- [numpy](https://numpy.org/) → numerical operations  
- [matplotlib](https://matplotlib.org/) & [seaborn](https://seaborn.pydata.org/) → visualizations  

---

## Dataset
You need two files in the same folder as the script:

1. **`movies.csv`** → contains movie IDs and titles  
   Example:
   ```csv
   item_id,title
   1. Toy Story (1995)
   2. GoldenEye (1995)
   3. Four Rooms (1995)
   ratings.csv → contains user ratings
Example:

user_id,item_id,rating,timestamp
1,1,5,874965758
1,2,3,876893171
1,3,4,878542960

## How to Run

1. Clone or download this repository.

2. Place movies.csv and ratings.csv in the same folder as movie_recommendation.py.

3. Install dependencies:

pip install pandas numpy matplotlib seaborn

**Run the script:**

1. python movie_recommendation.py

2. Example usage in the script:

3. print(get_recommendations("Star Wars (1977)"))

**Example Output**
Top Recommendations for 'Star Wars (1977)':

                               Correlation  num_of_ratings
Return of the Jedi (1983)         0.748353             507
Empire Strikes Back (1980)        0.707351             485
Raiders of the Lost Ark (1981)    0.673918             420
Indiana Jones and the Last ...    0.662944             379


