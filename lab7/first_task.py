import pygame
import time
import os
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 600, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
BACKGROUND_COLOR = (255, 255, 255)

images_path = "images"
clock_face = pygame.image.load(os.path.join(images_path, "clock.png"))
clock_face = pygame.transform.scale(clock_face, (WIDTH, HEIGHT))
hand_minute = pygame.image.load(os.path.join(images_path, "rightarm.png"))
hand_second = pygame.image.load(os.path.join(images_path, "leftarm.png"))

hand_minute = pygame.transform.scale(hand_minute, (hand_minute.get_width() // 2, hand_minute.get_height() // 2))
hand_second = pygame.transform.scale(hand_second, (hand_second.get_width() // 2, hand_second.get_height() // 2))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

running = True
while running:
    screen.fill(BACKGROUND_COLOR)
    screen.blit(clock_face, (0, 0))
    
    current_time = datetime.now()
    minutes = current_time.minute
    seconds = current_time.second

    minute_angle = -(minutes%60)*6 - 50
    second_angle = -(seconds%60)*6 + 51
  
    rotated_minute = pygame.transform.rotate(hand_minute, minute_angle)
    rotated_second = pygame.transform.rotate(hand_second, second_angle)

    min_rect = rotated_minute.get_rect(center=CENTER)
    sec_rect = rotated_second.get_rect(center=CENTER)

    screen.blit(rotated_minute, min_rect.topleft)
    screen.blit(rotated_second, sec_rect.topleft)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1000) 

pygame.quit()
