#make a farming game where there will be one block of land on top of the block a bot will be standing and 
#will harvest the land
#import the required libraries
import pygame
import random

# Define the screen width and height
screen_width = 800
screen_height = 600

# Define the colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
brown = (165, 42, 42)

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Farming Game")

# Define the block of land
land_width = 100
land_height = 100
land_x = (screen_width - land_width) // 2
land_y = (screen_height - land_height) // 2

# Define the bot
bot_width = 20
bot_height = 20
bot_x = land_x + land_width // 2 - bot_width // 2
bot_y = land_y - bot_height

# Define the crop
crop_width = 10
crop_height = 10
crop_x = random.randint(land_x, land_x + land_width - crop_width)
crop_y = random.randint(land_y, land_y + land_height - crop_height)

# Define the font
font = pygame.font.Font(None, 36)

# Define the score
score = 0