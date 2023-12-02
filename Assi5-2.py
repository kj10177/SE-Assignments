class SocialMediaPlatform:
    def __init__(self):
        self.users = {}
        self.graph = {}

    def add_user(self, username):
        if username in self.users:
            print("User already exists. Please choose another username.")
        else:
            self.users[username] = True
            self.graph[username] = []

    def remove_user(self, username):
        if username not in self.users:
            print("User not found. Please make sure of the username.")
        else:
            # Remove the user from the graph and all connections
            del self.graph[username]
            for user, connections in self.graph.items():
                if username in connections:
                    connections.remove(username)

            del self.users[username]
            print(f"User '{username}' has been removed.")

    def send_friend_request(self, user1, user2):
        if user1 not in self.users or user2 not in self.users:
            print("One or both users not found. Please make sure of the usernames.")
        else:
            # Add edges between users to represent a friend connection
            self.graph[user1].append(user2)
            self.graph[user2].append(user1)
            print(f"Friend request sent from {user1} to {user2}.")

    def remove_friend(self, user1, user2):
        if user1 not in self.users or user2 not in self.users:
            print("One or both users not found. Please make sure of the usernames.")
        else:
            # Remove edges between users to end the friend connection
            self.graph[user1].remove(user2)
            self.graph[user2].remove(user1)
            print(f"{user1} and {user2} are no longer friends.")

    def view_friends(self, username):
        if username not in self.users:
            print("User not found. Please make sure of the username.")
        else:
            friends = self.graph[username]
            print(f"Friends of {username}: {', '.join(friends)}")

    def view_all_users(self):
        print("List of all users on the platform:")
        for username in self.users:
            print(username)

# Example usage:
social_media = SocialMediaPlatform()

while True:
    print("- - - - - - - - - - - - - - -")
    print("1. Add a user to the platform")
    print("2. Remove a user from the platform")
    print("3. Send a friend request")
    print("4. Remove a friend")
    print("5. View your list of friends")
    print("6. View the list of users on the platform")
    print("7. Exit")
    choice = int(input("Enter a choice: "))

    if choice == 1:
        username = input("Enter a new username: ")
        social_media.add_user(username)

    elif choice == 2:
        username = input("Enter the username to remove: ")
        social_media.remove_user(username)

    elif choice == 3:
        user1 = input("Enter your username: ")
        user2 = input("Enter the username of the friend you want to add: ")
        social_media.send_friend_request(user1, user2)

    elif choice == 4:
        user1 = input("Enter your username: ")
        user2 = input("Enter the username of the friend you want to remove: ")
        social_media.remove_friend(user1, user2)

    elif choice == 5:
        username = input("Enter your username: ")
        social_media.view_friends(username)

    elif choice == 6:
        social_media.view_all_users()

    elif choice == 7:
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
