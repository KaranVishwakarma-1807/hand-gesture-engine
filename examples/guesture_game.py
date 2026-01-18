import pygame
import cv2
import random
from hand_gesture.engine import GestureEngine

# INIT  
pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gesture Dodge Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 64)

# GESTURE ENGINE 
engine = GestureEngine()

cap = cv2.VideoCapture(0)

# PLAYER 
player = pygame.Rect(375, 420, 50, 50)
PLAYER_SPEED = 7

# ENEMIES 
enemies = []
ENEMY_SIZE = 40
ENEMY_SPEED = 5
SPAWN_RATE = 30  # lower = more enemies
frame_count = 0

# SCORE 
score = 0

# GAME STATE 
game_over = False

# THIS WILL CONVERT OPENCV FRAMES INTO SURFACE FOR PYGAME 
def cvframe_to_pygame(frame, size=(140, 105)):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, size)
    frame = frame.swapaxes(0, 1)
    return pygame.surfarray.make_surface(frame)
  
# RESTART 
def reset_game():
    global player, enemies, score, game_over, frame_count

    player.x = 375
    player.y = 420

    enemies.clear()
    score = 0
    frame_count = 0
    game_over = False


# GAME LOOP 
running = True
while running:
    clock.tick(60)
    frame_count += 1

    # EVENTS 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # CAMERA  
        ret, frame = cap.read()
        if not ret:
            break

        frame, gesture = engine.process(frame)

        # PLAYER MOVE 
        if gesture == "THREE":
            player.x += PLAYER_SPEED
        elif gesture == "PEACE":
            player.x -= PLAYER_SPEED

        player.x = max(0, min(WIDTH - player.width, player.x))

        # SPAWN ENEMY 
        if frame_count % SPAWN_RATE == 0:
            x = random.randint(0, WIDTH - ENEMY_SIZE)
            enemy = pygame.Rect(x, 0, ENEMY_SIZE, ENEMY_SIZE)
            enemies.append(enemy)

        # MOVE ENEMIES  
        for enemy in enemies:
            enemy.y += ENEMY_SPEED

        # REMOVE OFF-SCREEN ENEMIES 
        enemies = [e for e in enemies if e.y < HEIGHT]

        # COLLISION DETECTION 
        for enemy in enemies:
            if player.colliderect(enemy):
                game_over = True

        # SCORE 
        score += 1
    else:
    # RESTART WITH PEACE SIGN 
      ret, frame = cap.read()
      if not ret:
          break

      frame, gesture = engine.process(frame)

      if gesture == "PEACE":
          reset_game()


    # DRAW 
    screen.fill((25, 25, 25))

    # Player
    pygame.draw.rect(screen, (0, 200, 255), player)

    # Enemies
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 50, 50), enemy)

    # Score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Webcam preview
    if 'frame' in locals():
        cam_surface = cvframe_to_pygame(frame)
        cam_x = WIDTH - cam_surface.get_width() - 10
        cam_y = 10
        screen.blit(cam_surface, (cam_x, cam_y))

        # Webcam border
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (cam_x, cam_y, cam_surface.get_width(), cam_surface.get_height()),
            2
        )

    # Game over text
    if game_over:
      hint = font.render("Show PEACE sign to restart", True, (255, 255, 255))
      screen.blit(hint, (WIDTH // 2 - 180, HEIGHT // 2 + 30))


    pygame.display.flip()


# CLEANUP
cap.release()
pygame.quit()
