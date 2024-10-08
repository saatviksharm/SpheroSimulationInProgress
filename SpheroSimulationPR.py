#Imports

import pygame
import random

pygame.init

#Display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Polymer Formation Simulation")

#Colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

#Sphero Robot
class Sphero:
    def init(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vx = random.uniform(-2, 2)  # Velocity in the x direction
        self.vy = random.uniform(-2, 2)  # Velocity in the y direction

    def move(self):
        self.x += self.vx
        self.y += self.vy
        # Bounce off walls
        if self.x - self.radius <= 0 or self.x + self.radius >= 800:
            self.vx = -1
        if self.y - self.radius <= 0 or self.y + self.radius >= 600:
            self.vy= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


#Collision Detection
def detect_collision(sphero1, sphero2):
    dist = math.sqrt((sphero1.x - sphero2.x) ** 2 + (sphero1.y - sphero2.y)  ** 2)
    return dist <= sphero1.radius + sphero2.radius

#Merge Spheros
def merge_spheros(sphero1, sphero2):
    new_sphero_mass = sphero1.mass + sphero2.mass
    new_sphero_radius = sphero1.radius + sphero2.radius