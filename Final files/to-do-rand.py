import random, keyboard, time

# List of project ideas
project_ideas = [
    "Build a weather app",
    "Create a to-do list application",
    "Develop a chatbot",
    "Design a recipe finder",
    "Build a budget tracker",
    "Create a quiz game",
    "Develop a music player",
    "Design a calorie counter",
    "Build a URL shortener",
    "Create a password manager"
]
def wait():
    time.sleep(3)

# Function to suggest a random project
def suggest_project():
    project = random.choice(project_ideas)
    return project

# Main function
def main():
    # Get the suggested project
    suggested_project = suggest_project()

    # Print the suggested project
    print("Today's project idea:")
    print(suggested_project)
    if input("Press Enter to exit...") == 'keyboard.is_pressed("enter")': exit()
    else: wait()

# Run the main function
if __name__ == "__main__":
    main()