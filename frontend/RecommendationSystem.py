from openai import OpenAI
from customer_data import product_catalog, customer_profiles

class RecommendationSystem:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        
    def get_recommendations(self, customer_profile, question):
        # Prepare catalog as a string for OpenAI context
        catalog_text = "\n".join(
            f"- {item['name']}: {item['features']} ({item['price']})" 
            for item in product_catalog
        )
        
        # Construct prompt for OpenAI
        prompt = f"""
        Customer Profile:
        Account Name: {customer_profile['acct_name']}
        Extenders: {customer_profile['extenders']}
        Wireless Clients Count: {customer_profile['wireless_clients_count']}
        Wired Clients Count: {customer_profile['wired_clients_count']}
        Network Speed: {customer_profile['network_speed']}
        Location: {customer_profile['city']}, {customer_profile['state']}
        Whole-Home Wi-Fi: {customer_profile['whole_home_wifi']}
        Wi-Fi Security: {customer_profile['wifi_security']}
        Wi-Fi Security Plus: {customer_profile['wifi_security_plus']}
        
        Product Catalog:
        {catalog_text}
        
        Question: {question}
        Based on the customer profile and product catalog, recommend the most relevant products for the customer's question.
        """
        
        # Call OpenAI API
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant recommending products."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
