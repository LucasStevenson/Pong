from paddle import Paddle
from ball import Ball
import pygame
pygame.init()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# JUST SOME GIVENS
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# SETTING UP GAME VARS
leftPaddle = Paddle(WHITE, 10, 100)
leftPaddle.rect.x = 20
leftPaddle.rect.y = 200

rightPaddle = Paddle(WHITE, 10, 100)
rightPaddle.rect.x = 670
rightPaddle.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.reset()  # sets the position and velocity of the ball

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(leftPaddle, rightPaddle, ball)

run = True

clock = pygame.time.Clock()
FPS = 60

scoreA = 0
scoreB = 0

font = pygame.font.Font(None, 74)
font2 = pygame.font.Font(None, 65)


# CHECKING KEYS PRESSED
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and scoreA == 10 or scoreB == 10:
            if event.key == pygame.K_x:
                run = False
            elif event.key == pygame.K_SPACE:
                scoreA = 0
                scoreB = 0

    if scoreA == 10 or scoreB == 10:  # GAME OVER SCREEN
        screen.fill(BLACK)
        # LITERALLY ALL TEXT
        text = font.render(
            "Left Wins" if scoreA == 10 else "Right Wins", True, WHITE)
        text2 = font2.render("Restart - Spacebar", True, WHITE)
        text3 = font2.render("Quit - X", True, WHITE)
        finalScore = font.render(str(scoreA) + " | " + str(scoreB), 1, WHITE)

        # TEXT POSITIONING
        text_rect = text.get_rect()

        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2.4 - text_rect.height / 2

        text2_x = screen.get_width() / 2 - text2.get_rect().width / 2
        text2_y = text_y + 180

        text3_x = screen.get_width() / 2 - text3.get_rect().width / 2
        text3_y = text2_y + 60

        finalScore_x = screen.get_width() / 2 - finalScore.get_rect().width / 2
        finalScore_y = text_y + 70

        # DISPLAYING THE TEXT
        screen.blit(text, [text_x, text_y])
        screen.blit(text2, [text2_x, text2_y])
        screen.blit(text3, [text3_x, text3_y])
        screen.blit(finalScore, [finalScore_x, finalScore_y])
    else:  # the actual game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            leftPaddle.moveUp(5)
        if keys[pygame.K_s]:
            leftPaddle.moveDown(5)
        if keys[pygame.K_UP]:
            rightPaddle.moveUp(5)
        if keys[pygame.K_DOWN]:
            rightPaddle.moveDown(5)

        all_sprites_list.update()

        if ball.rect.x >= 690:
            scoreA += 1
            ball.reset()
        if ball.rect.x <= 0:
            scoreB += 1
            ball.reset()
        if ball.rect.y > 490 or ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

        if pygame.sprite.collide_mask(ball, leftPaddle) or pygame.sprite.collide_mask(ball, rightPaddle):
            ball.bounce()

        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

        all_sprites_list.draw(screen)

        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (250, 10))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text, (420, 10))

    pygame.display.flip()

    clock.tick(FPS)


pygame.quit()
