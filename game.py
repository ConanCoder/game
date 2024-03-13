import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Màn hình game
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Game")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Nhân vật
player_size = 50
player_x = screen_width / 2 - player_size / 2
player_y = screen_height - 2 * player_size
player_speed = 5

# Đồng tiền
coin_size = 30
coin_speed = 5
coin_spawn_rate = 25
coins = []

# Vật cản
obstacle_size = 50
obstacle_speed = 5
obstacle_spawn_rate = 100
obstacles = []

# Điểm số
score = 0
font = pygame.font.Font(None, 36)

# Hàm vẽ nhân vật
def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, player_size, player_size])

# Hàm vẽ đồng tiền
def draw_coins(coins):
    for coin in coins:
        pygame.draw.rect(screen, WHITE, coin)

# Hàm vẽ vật cản
def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, WHITE, obstacle)

# Hàm kiểm tra va chạm
def collision(player_x, player_y, object_x, object_y, object_size):
    if player_x + player_size >= object_x and player_x <= object_x + object_size:
        if player_y + player_size >= object_y and player_y <= object_y + object_size:
            return True
    return False

# Vòng lặp game
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Xử lý di chuyển nhân vật
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed

    # Tạo và di chuyển đồng tiền
    if random.randint(1, coin_spawn_rate) == 1:
        coin_x = random.randint(0, screen_width - coin_size)
        coin_y = -coin_size
        coins.append(pygame.Rect(coin_x, coin_y, coin_size, coin_size))
    for coin in coins:
        coin.y += coin_speed
        if coin.y > screen_height:
            coins.remove(coin)
            score += 1

    # Tạo và di chuyển vật cản
    if random.randint(1, obstacle_spawn_rate) == 1:
        obstacle_x = random.randint(0, screen_width - obstacle_size)
        obstacle_y = -obstacle_size
        obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_size, obstacle_size))
    for obstacle in obstacles:
        obstacle.y += obstacle_speed
        if obstacle.y > screen_height:
            obstacles.remove(obstacle)
        if collision(player_x, player_y, obstacle.x, obstacle.y, obstacle_size):
            running = False

    # Vẽ đối tượng trên màn hình
    draw_player(player_x, player_y)
    draw_coins(coins)
    draw_obstacles(obstacles)

    # Hiển thị điểm số
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

    # Cập nhật màn hình
    pygame.display.flip()
    clock.tick(60)

# Kết thúc game
pygame.quit()
