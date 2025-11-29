import pygame
import random
import sys


pygame.init()


WIDTH = 600
HEIGHT = 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodger Game - Md Taju")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE  = (0, 150, 255)
RED   = (255, 50, 50)


player_size = 40
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 8


enemy_size = 40
enemy_speed_start = 4   
enemy_speed = enemy_speed_start
enemy_list = []

score = 0
font = pygame.font.SysFont("arial", 24, True)


def draw_player(x, y):
    pygame.draw.rect(WIN, BLUE, (x, y, player_size, player_size))


def drop_enemies(enemy_list):
   
    if len(enemy_list) < 7:
        if random.random() < 0.15:
            x_pos = random.randint(0, WIDTH - enemy_size)
            enemy_list.append([x_pos, 0])


def draw_enemies(enemy_list):
    for enemy in enemy_list:
        pygame.draw.rect(WIN, RED, (enemy[0], enemy[1], enemy_size, enemy_size))


def update_enemy_positions(enemy_list, speed):
    global score
    for idx, enemy in enumerate(enemy_list):
        enemy[1] += speed

        if enemy[1] > HEIGHT:
            enemy_list.pop(idx)
            score += 1


def check_collision(player_x, player_y, enemy_list):
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for enemy in enemy_list:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)
        if player_rect.colliderect(enemy_rect):
            return True
    return False


def show_text(text, x, y, color=WHITE):
    label = font.render(text, True, color)
    WIN.blit(label, (x, y))


def main():
    global player_x, player_y, enemy_speed, score, enemy_list

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed

        drop_enemies(enemy_list)
        update_enemy_positions(enemy_list, enemy_speed)

        enemy_speed = enemy_speed_start + score // 10

        
        if check_collision(player_x, player_y, enemy_list):
           
            WIN.fill(BLACK)
            show_text("GAME OVER!", WIDTH // 2 - 80, HEIGHT // 2 - 20, RED)
            show_text(f"Score: {score}", WIDTH // 2 - 50, HEIGHT // 2 + 20, WHITE)
            pygame.display.update()
            pygame.time.wait(2000)
            running = False
            continue

        # ----- Drawing -----
        WIN.fill(BLACK)
        draw_player(player_x, player_y)
        draw_enemies(enemy_list)
        show_text(f"Score: {score}", 10, 10)

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
