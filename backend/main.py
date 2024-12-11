def main():
    # Your API key
    api_key = "***"
    
    # Initialize recommendation system
    recommender = RecommendationSystem(api_key)
    
    print("Welcome to the Product Recommendation System!")
    print("Choose a customer profile:")
    
    for idx, profile in enumerate(customer_profiles):
        print(f"{idx + 1}: {profile['acct_name']} ({profile['city']}, {profile['state']})")
    
    selected_customer = int(input("\nEnter the number of the customer profile: ")) - 1
    customer_profile = customer_profiles[selected_customer]
    
    print("\nAsk a question related to your internet needs, or type 'exit' to quit.")
    
    while True:
        user_question = input("\nYour question: ")
        if user_question.lower() == "exit":
            print("Goodbye!")
            break
            
        try:
            recommendation = recommender.get_recommendations(customer_profile, user_question)
            print("\nRecommendations:")
            print(recommendation)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
