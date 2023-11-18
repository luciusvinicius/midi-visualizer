import pygame
from dataclasses import dataclass

@dataclass
class Visualizer():
    """Class responsible to show the colors from the MIDI file."""
    window_size: tuple[int, int] = (300, 200)
    window_title: str = "MIDI Visualizer"
    screen: pygame.Surface = None
    background_color: tuple[int, int, int] = (255, 255, 255)
    
    def start(self):
        self.screen = pygame.display.set_mode(self.window_size)
    
    def play(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        pygame.display.flip()
        self.screen.fill(self.background_color)
    
    def change_to_color(self, color: tuple[int, int, int]):
        self.background_color = color
        self.play()