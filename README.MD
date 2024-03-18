# Movie Recommendation Engine Using Schematic Search

## Overview
This movie recommendation engine utilizes schematic search to provide personalized recommendations based on user preferences and similarities between movies. The system incorporates a MongoDB database containing movie data and leverages a pre-trained sentence embeddings model for semantic analysis. Users interact with the engine through a Streamlit-based interface, where they input their preferences, and the engine responds with relevant movie recommendations.

## Components

### 1. Data Handling (Server-side)
- **MongoDB Database**: Stores structured movie data, including titles, plots, genres, and other relevant attributes.
- **API Integration**: Utilizes the Hugging Face API for generating sentence embeddings to represent movie plots semantically.

### 2. Schematic Analysis
- **Embedding Generation**: Converts textual movie plots into dense vector representations using the pre-trained sentence embeddings model.
- **Vector Search**: Performs vector similarity search to identify movies with plot embeddings similar to user input.

### 3. Recommendation Generation
- **Query Processing**: Parses user input to extract relevant preferences or keywords.
- **Database Querying**: Retrieves movies from the MongoDB database based on user preferences and similarity scores.
- **Ranking and Filtering**: Ranks and filters recommended movies based on relevance to user preferences.

### 4. User Interface (Client-side)
- **Streamlit Interface**: Provides a user-friendly interface for users to input preferences and view movie recommendations.
- **Message Display**: Displays user interactions and recommendations in a chat-like format for easy comprehension.

## Example Workflow

1. **User Input**: User enters preferences like "Action movies with space wars".
2. **Semantic Analysis**: Engine converts the input into a semantic embedding using the Hugging Face API.
3. **Vector Search**: Searches for movies with similar plot embeddings in the MongoDB database.
4. **Recommendation Generation**: Retrieves and ranks movies based on similarity scores and user preferences.
5. **Presentation**: Displays recommended movies to the user via the Streamlit interface.

## Advantages
- **Semantic Understanding**: Utilizes advanced semantic analysis to capture the essence of movie plots.
- **Personalization**: Tailors recommendations based on user preferences and similarity metrics.
- **Real-time Interaction**: Provides instant feedback and recommendations through the Streamlit interface.
- **Scalability**: Can handle large datasets and diverse user preferences effectively.

## Conclusion
The movie recommendation engine using schematic search and semantic analysis offers a sophisticated solution for personalized movie recommendations. By combining advanced algorithms with user-friendly interfaces, it enhances the movie discovery experience and assists users in finding relevant and enjoyable content effortlessly.