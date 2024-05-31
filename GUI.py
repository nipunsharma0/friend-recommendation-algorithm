import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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

class SocialNetworkGUI:
    def __init__(self, social_network):
        self.social_network = social_network
        self.root = tk.Tk()
        self.root.title("Social Network Visualization")
        self.root.geometry("800x600")
        self.root.config(bg="black")

        self.main_frame = tk.Frame(self.root, bg="#121212")
        self.main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.left_frame = tk.Frame(self.main_frame, bg="#121212")
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.right_frame = tk.Frame(self.main_frame, bg="#121212")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.canvas = FigureCanvasTkAgg(plt.figure(facecolor='#121212'), master=self.right_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.plot_social_network()

        self.user_label = tk.Label(self.left_frame, text="Select User:", bg="#121212", fg="white")
        self.user_label.pack(side=tk.TOP, padx=10, pady=10)

        self.user_var = tk.StringVar()
        self.user_dropdown = ttk.Combobox(self.left_frame, textvariable=self.user_var)
        self.user_dropdown['values'] = list(self.social_network.users.keys())
        self.user_dropdown.pack(side=tk.TOP, padx=10, pady=5)

        self.recommend_button = tk.Button(self.left_frame, text="Recommend Friends", command=self.recommend_friends, bg="darkblue", fg="white")
        self.recommend_button.pack(side=tk.TOP, padx=10, pady=5)

        self.recommend_label = tk.Label(self.left_frame, text="Recommended Friends:", bg="#121212", fg="white")
        self.recommend_label.pack(side=tk.TOP, padx=10, pady=10)

        self.recommend_text = tk.Text(self.left_frame, height=10, width=40, bg="#121212", fg="#CCCCCC")
        self.recommend_text.pack(side=tk.TOP, padx=10, pady=5)

        self.root.mainloop()

    def plot_social_network(self):
        # Clear the existing plot
        self.canvas.figure.clear()

        G = nx.Graph()
        for user in self.social_network.users.values():
            G.add_node(user.name)

        for user, connections in self.social_network.connections.items():
            for connection in connections:
                G.add_edge(user, connection.name)

        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, ax=self.canvas.figure.gca(), node_size=700, node_color="#85fb64")
        nx.draw_networkx_edges(G, pos, ax=self.canvas.figure.gca(), edge_color="gray")
        nx.draw_networkx_labels(G, pos, ax=self.canvas.figure.gca(), font_size=10, font_weight="bold", font_color="white")

        # Redraw canvas
        self.canvas.draw()

    def recommend_friends(self):
        user_name = self.user_var.get()
        start_user = self.social_network.users[user_name]
        recommendations = self.social_network.bfs_recommendation(start_user)
        
        self.recommend_text.delete('1.0', tk.END)
        for recommendation in recommendations:
            self.recommend_text.insert(tk.END, f"{recommendation.name}\n")
        
        # Update the tree visualization
        self.plot_social_network()

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

    gui = SocialNetworkGUI(social_network)
