#25-05-2024 6:44 PM 1845hours
import pygame
import random

# Initialize pygame
pygame.init()

# Define the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Define the screen size and title
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game_ TEST")

# Define the snake class
class Snake:
    def __init__(self):
        # Initialize the snake attributes
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 10
        self.dx = 5 # Horizontal velocity
        self.dy = 0 # Vertical velocity
        self.is_add = True # Flag to add an element

    def draw(self):
        # Draw the snake on the screen
        for element in self.elements:
            pygame.draw.circle(screen, green, element, self.radius)

    def move(self):
        # Move the snake by updating its elements
        if self.is_add:
            # Add an element at the end of the snake
            self.size += 1
            self.elements.append([0, 0])
            self.is_add = False

        # Shift the elements to the next position
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        # Update the head of the snake
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

    def eat(self):
        # Check if the snake eats the food
        if abs(self.elements[0][0] - food.x) < food.radius + self.radius and abs(self.elements[0][1] - food.y) < food.radius + self.radius:
            # Set the flag to add an element
            self.is_add = True

    def check_boundary(self):
        # Check if the snake hits the boundary of the screen
        if self.elements[0][0] > screen_width or self.elements[0][0] < 0 or self.elements[0][1] > screen_height or self.elements[0][1] < 0:
            # Game over
            pygame.quit()

    def check_collision(self):
        # Check if the snake collides with itself
        for i in range(1, self.size):
            if abs(self.elements[0][0] - self.elements[i][0]) < self.radius and abs(self.elements[0][1] - self.elements[i][1]) < self.radius:
                # Game over
                pygame.quit()

# Define the food class
class Food:
    def __init__(self):
        # Initialize the food attributes
        self.x = random.randint(50, screen_width - 50)
        self.y = random.randint(50, screen_height - 50)
        self.radius = 8

    def draw(self):
        # Draw the food on the screen
        pygame.draw.circle(screen, red, (self.x, self.y), self.radius)
# make a class named ball_p for a ball that will appear at random position and if the ball is eaten by snake it will make the snake bigger and the score will increase by 1
class ball_p:
    def __init__(self):
        self.x = random.randint(50, screen_width - 50)
        self.y = random.randint(50, screen_height - 50)
        self.radius = 8
    def draw(self):
        pygame.draw.circle(screen, red, (self.x, self.y), self.radius)
    

# Create an instance of snake and food
snake = Snake()
food = Food()

# Define the clock object to control the frame rate
clock = pygame.time.Clock()

# Define the game loop
running = True

while running:
    # Handle the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the game
            running = False

        if event.type == pygame.KEYDOWN:
            # Handle the key presses
            if event.key == pygame.K_RIGHT:
                # Move right
                snake.dx = 5
                snake.dy = 0

            if event.key == pygame.K_LEFT:
                # Move left
                snake.dx = -5
                snake.dy = 0

            if event.key == pygame.K_UP:
                # Move up
                snake.dx = 0
                snake.dy = -5

            if event.key == pygame.K_DOWN:
                # Move down
                snake.dx = 0
                snake.dy = 5

    # Fill the screen with black color
    screen.fill(black)

    # Draw the snake and the food on the screen
    snake.draw()
    food.draw()

    # Move the snake and check for eating and collisions

    snake.move()
    #new part edits