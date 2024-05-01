import pandas as pd

# Sample data (user-item ratings)
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4],
    'item_id': ['A', 'B', 'C', 'A', 'B', 'A', 'B', 'C', 'B', 'C'],
    'rating': [5, 4, 2, 3, 5, 4, 2, 1, 3, 2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate mean rating for each item
item_ratings = df.groupby('item_id')['rating'].mean()

# Function to recommend items to a user
def recommend_items(user_id, num_recommendations=3):
    # Filter out items the user has already rated
    rated_items = set(df[df['user_id'] == user_id]['item_id'])
    
    # Calculate average rating for each item
    item_ratings = df.groupby('item_id')['rating'].mean()
    
    # Filter out items already rated by the user
    unrated_items = item_ratings.index.difference(rated_items)
    
    # Get top recommendations
    recommendations = item_ratings.loc[unrated_items].sort_values(ascending=False).head(num_recommendations)
    
    return recommendations

# Example usage
user_id = 1
recommendations = recommend_items(user_id)
print(f"Top recommendations for user {user_id}:")
print(recommendations)
