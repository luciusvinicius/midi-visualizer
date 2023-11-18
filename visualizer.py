import pygame
import math
import numpy as np
from array import array
from dataclasses import dataclass

@dataclass
class Visualizer():
    """Class responsible to show the colors from the MIDI file.
    TODO: Visualizer should be async to not block the MIDI file playing."""
    window_size: tuple[int, int] = (300, 200)
    window_title: str = "MIDI Visualizer"
    screen: pygame.Surface = None
    background_color: np.ndarray = np.array([255, 255, 255])
    color_fade_step_multiplier: float = 0.002
    
    def start(self):
        """Setups the window for the visualizer."""
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.window_title)
    
    def update(self):
        """Updates the window with the new color."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        pygame.display.flip()
        self.screen.fill(self.background_color)

    def change_to_color(self, color: np.ndarray, velocity: int = None):
        """Changes and updates the visualizer background color to the given one.
        TODO(?): Is there how simplify the smooth effect?
        TODO: Smooth effect IS NOT ASYNC.
        TODO(2?): Maybe use a non-linear function to smooth the color change."""
        
        # Defines the direction of the color change, and the clamp min-max values.
        mi = np.minimum(color, self.background_color)
        ma = np.maximum(color, self.background_color)
        direction = [None] * 3
        for i in range(3):
            direction[i] = 1 if color[i] > self.background_color[i] else -1 if color[i] < self.background_color[i] else 0
        direction = np.array(direction)
        
        # Calculate the increment for each color component
        increments = direction * self.color_fade_step_multiplier * velocity

        # Transiction from current color to the new one.
        while (self.background_color != color).any():
            # Clamp to guarantee that the color will not go over the destination color.
            new_color = self.clamp(self.background_color + increments, mi, ma)
            self.background_color = tuple(new_color.tolist())
            self.update()
        
    
    # -------------- Utils Functions
    def clamp(self, val : np.ndarray, mi : np.ndarray, ma : np.ndarray):
        """Given an np.ndarray, clamps the values between the min and max values."""
        return np.minimum(np.maximum(val, mi), ma)
    