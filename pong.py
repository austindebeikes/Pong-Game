import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Pong Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("Arial", 40)

paddle_width, paddle_height = 15, 100
player1_x, player2_x = 30, screen_width - 30 - paddle_width
player1_y, player2_y = screen_height // 2 - paddle_height // 2, screen_height // 2 - paddle_height // 2
paddle_speed = 5

ball_size = 15
ball_x = screen_width // 2 - ball_size // 2
ball_y = screen_height // 2 - ball_size // 2
ball_speed_x = 2
ball_speed_y = 2

player1_score = 0
player2_score = 0
fomt = pygame.font.SysFont("Arial", 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < screen_height - paddle_height:
        player1_y += paddle_speed

    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < screen_height - paddle_height:
        player2_y += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_speed_y *= -1

    if (player1_x + paddle_width >= ball_x >= player1_x) and (player1_y <= ball_y + ball_size <= player1_y + paddle_height):
        ball_speed_x *= -1
    if (player2_x <= ball_x + ball_size <= player2_x + paddle_width) and (player2_y <= ball_y + ball_size <= player2_y + paddle_height):
        ball_speed_x *= -1

    if ball_x <= 0:
        player2_score += 1
        ball_x = screen_width // 2 - ball_size // 2
        ball_y = screen_height // 2 - ball_size // 2
        ball_speed_x *= -1
    if ball_x >= screen_width - ball_size:
        player1_score += 1
        ball_x = screen_width // 2 - ball_size // 2
        ball_y = screen_height // 2 - ball_size // 2
        ball_speed_x *= -1

    if player1_score == 10 or player2_score == 10:
        winner = "Player 1" if player1_score == 10 else "Player 2"
        game_over_text = font.render(f"{winner} Wins!", True, WHITE)
        screen.fill(BLACK)
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2))
        pygame.display.flip()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()


    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y,paddle_width, paddle_height ))

    pygame.draw.rect(screen, WHITE, (ball_x, ball_y, ball_size, ball_size))

    player1_score_text = font.render(str(player1_score), True, WHITE)
    player2_score_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_score_text, (screen_width // 4 - player1_score_text.get_width() // 2, 20))
    screen.blit(player2_score_text, (3 * screen_width // 4 - player2_score_text.get_width() // 2, 20))

    pygame.display.flip()