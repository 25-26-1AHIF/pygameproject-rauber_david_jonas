import pygame

class Bilder:
    def __init__(self, filepath: str, image_count: int, image_rect: pygame.Rect, animation_speed: int):
        self.filepath = filepath
        self.image_count = image_count
        self.image_rect = image_rect
        self.images: list[pygame.Surface] = []
        self.animation_speed = animation_speed

    def load_spritesheet(self):
        spritesheet = pygame.image.load(self.filepath).convert_alpha()

        for image_index in range(self.image_count):
            # Neues Surface mit Transparenz
            image_surface = pygame.Surface(self.image_rect.size, pygame.SRCALPHA).convert_alpha()


            area = pygame.Rect(
                image_index * self.image_rect.width,
                0,
                self.image_rect.width,
                self.image_rect.height
            )

            image_surface.blit(spritesheet, (0, 0), area)
            self.images.append(image_surface)

    def draw(self, screen: pygame.Surface, xpos: float, ypos: float, frame_counter: int):
        index = (frame_counter // self.animation_speed) % self.image_count

        screen.blit(self.images[index], (int(xpos), int(ypos)), )
