class CryptoAdvisor:
    def __init__(self, name="CryptoBuddy"):
        self.name = name
        self.crypto_db = {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3/10
            },
            "Ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6/10
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10
            }
        }
        self.welcome_message = f"Hey there! I'm {self.name}, your friendly crypto advisor. How can I help you today? 🚀"
        
    def get_rising_coins(self):
        # rising_coins = [coin for coin, data in self.crypto_db.items() 
        #                if data["price_trend"] == "rising"]
        # return rising_coins

        # same way of writting the loop
        rising_coins = []
        for coin, data in self.crypto_db.items():
            if data["price_trend"] == "rising":
                rising_coins.append(coin)
        return rising_coins
    
    def get_sustainable_coins(self, min_score=7/10):
        sustainable_coins = [coin for coin, data in self.crypto_db.items() 
                            if data["sustainability_score"] >= min_score]
        return sustainable_coins
    
    def get_most_sustainable_coin(self):
        return max(self.crypto_db, key=lambda x: self.crypto_db[x]["sustainability_score"])
    
    def get_best_investment(self):
        best_coin = None
        best_score = -1
        
        for coin, data in self.crypto_db.items():
            profitability_score = 0
            if data["price_trend"] == "rising":
                profitability_score += 5
            elif data["price_trend"] == "stable":
                profitability_score += 3
                
            if data["market_cap"] == "high":
                profitability_score += 3
            elif data["market_cap"] == "medium":
                profitability_score += 2
                
            sustainability = data["sustainability_score"] * 10 
            
            total_score = profitability_score + sustainability
            if total_score > best_score:
                best_score = total_score
                best_coin = coin
                
        return best_coin
    
    def respond(self, user_input):
        user_input = user_input.lower()
        
        
        disclaimer = "\n\n Disclaimer: Crypto investments are risky. Always do your own research!"
        
        if "trending" in user_input or "rising" in user_input:
            rising = self.get_rising_coins()
            if rising:
                return f"These coins are currently trending up: {', '.join(rising)}! " + disclaimer
            else:
                return "I don't see any trending coins in my database right now." + disclaimer
                
        elif "sustainable" in user_input or "green" in user_input or "eco" in user_input:
            coin = self.get_most_sustainable_coin()
            return f"{coin} is the most sustainable option with a score of {self.crypto_db[coin]['sustainability_score']*10}/10! " + disclaimer
            
        elif "invest" in user_input or "buy" in user_input or "growth" in user_input or "long-term" in user_input:
            best = self.get_best_investment()
            return f"Based on both profitability and sustainability, I'd recommend looking into {best}! " + disclaimer
            
        elif "help" in user_input or "can you do" in user_input:
            return (f"I'm {self.name}, your crypto advisor! You can ask me questions like:\n"
                    "- Which crypto is trending up?\n"
                    "- What's the most sustainable coin?\n"
                    "- What should I invest in for long-term growth?\n"
                    "- Tell me about Bitcoin/Ethereum/Cardano")
                    
        elif any(coin.lower() in user_input for coin in self.crypto_db.keys()):
            for coin in self.crypto_db:
                if coin.lower() in user_input:
                    data = self.crypto_db[coin]
                    return (f"Here's what I know about {coin}:\n"
                            f" Price Trend: {data['price_trend'].capitalize()}\n"
                            f" Market Cap: {data['market_cap'].capitalize()}\n"
                            f" Energy Use: {data['energy_use'].capitalize()}\n"
                            f" Sustainability Score: {data['sustainability_score']*10}/10" + disclaimer)
        
        else:
            return "I'm not sure how to answer that. Try asking about trending coins, sustainability, or specific cryptocurrencies!"

def main():
    bot = CryptoAdvisor("CryptoMaster")
    print(bot.welcome_message)
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print(f"\n{bot.name}: Thanks for chatting! Happy investing!")
            break
            
        response = bot.respond(user_input)                                                                                                                                                                                                              
        print(f"\n{bot.name}: {response}")

if __name__ == "__main__":
    main()

