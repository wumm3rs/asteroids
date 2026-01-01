import pygame
from constants import *

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        self.screen = screen
        pygame.draw.polygon(self.screen, "white", self.triangle(), LINE_WIDTH)

    def collides_with(self, other):
        distance = pygame.math.Vector2.distance_to(self.position, other.position)
        combined_radius = self.radius + other.radius
        return distance <= combined_radius
