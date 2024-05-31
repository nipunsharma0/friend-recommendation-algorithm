from collections import deque
import random

class UserProfile:
    def __init__(self, name, age, interests):
        self.name = name
        self.age = age
        self.interests = interests

class SocialNetwork:
    def __init__(self):
        self.users = {}
        self.connections = {}

    def add_user(self, user):
        self.users[user.name] = user

    def add_connection(self, user1, user2):
        if user1.name not in self.connections:
            self.connections[user1.name] = []
        if user2.name not in self.connections:
            self.connections[user2.name] = []
        self.connections[user1.name].append(user2)
        self.connections[user2.name].append(user1)

    def bfs_recommendation(self, start_user, num_recommendations=5):
        visited = set()
        queue = deque([(start_user, 0)])  # (user, distance)
        recommendations = []

        while queue:
            user, distance = queue.popleft()
            visited.add(user)

            for friend in self.connections.get(user.name, []):
                if friend not in visited:
                    visited.add(friend)
                    queue.append((friend, distance + 1))
                    common_interests = len(set(user.interests) & set(friend.interests))
                    recommendations.append((friend, common_interests))

        recommendations.sort(key=lambda x: x[1], reverse=True)
        return [rec[0] for rec in recommendations[:num_recommendations]]

# Example usage
if __name__ == "__main__":
    # Initialize social network
    social_network = SocialNetwork()

    # Create user profiles
    gotya = UserProfile("gotya", 25, ["Technology", "Art"])
    pintu = UserProfile("pintu", 30, ["Technology", "Music"])
    bandya = UserProfile("bandya", 28, ["Art", "Cooking"])
    athrya = UserProfile("athrya", 35, ["Music", "Sports"])
    eve = UserProfile("Eve", 22, ["Art", "Fashion"])
    atharva = UserProfile("Atharva", 69, ["Geo-politics", "Music"])
    ananya = UserProfile("Ananya", 26, ["Literature", "Dance"])
    arjun = UserProfile("Arjun", 33, ["History", "Adventure"])
    divya = UserProfile("Divya", 29, ["Photography", "Travel"])
    ishaan = UserProfile("Ishaan", 27, ["Food", "Nature"])
    rhea = UserProfile("rhea", 31, ["Movies", "Pets"])
    fatima = UserProfile("fatima", 28, ["Yoga", "Health", "Blasting"])
    nikhil = UserProfile("Nikhil", 34, ["Science", "Technology"])
    ashnuta = UserProfile("ashnuta", 20, ["Fashion", "Shopping"])
    
    # Add users to the social network
    social_network.add_user(gotya)
    social_network.add_user(pintu)
    social_network.add_user(bandya)
    social_network.add_user(athrya)
    social_network.add_user(eve)
    social_network.add_user(atharva)
    social_network.add_user(ananya)
    social_network.add_user(arjun)
    social_network.add_user(divya)
    social_network.add_user(ishaan)
    social_network.add_user(rhea)
    social_network.add_user(fatima)
    social_network.add_user(nikhil)
    social_network.add_user(ashnuta)

    # Add connections between users
    social_network.add_connection(gotya, pintu)
    social_network.add_connection(gotya, bandya)
    social_network.add_connection(pintu, athrya)
    social_network.add_connection(bandya, eve)
    social_network.add_connection(bandya, atharva)
    social_network.add_connection(atharva, ananya)
    social_network.add_connection(atharva, arjun)
    social_network.add_connection(ananya, divya)
    social_network.add_connection(ananya, ishaan)
    social_network.add_connection(arjun, rhea)
    social_network.add_connection(arjun, fatima)
    social_network.add_connection(rhea, nikhil)
    social_network.add_connection(rhea, ashnuta)

    # Perform BFS recommendation for a user
    start_user = random.choice(list(social_network.users.values()))
    recommendations = social_network.bfs_recommendation(start_user)
    
    print("User:", start_user.name)
    print("Age:", start_user.age)
    print("Interests:", start_user.interests)
    print("Recommendations based on mutual connections and interests:")
    for recommendation in recommendations:
        print("- Name:", recommendation.name, "| Age:", recommendation.age, "| Interests:", recommendation.interests)
