import sys
import pygame
from pygame.locals import QUIT

# Pygameの初期化
pygame.init()

# 画面のサイズ設定
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# 色の定義
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# フレームレートの設定
clock = pygame.time.Clock()

# ボールの初期位置と速度
ball_pos = [width // 2, height // 2]
ball_speed = [2, 2]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # ボールの位置を更新
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # 画面の端に到達したら跳ね返る
    if ball_pos[0] <= 0 or ball_pos[0] >= width:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= 0 or ball_pos[1] >= height:
        ball_speed[1] = -ball_speed[1]

    # 画面をクリア
    screen.fill(WHITE)

    # ボールを描画
    pygame.draw.circle(screen, BLUE, ball_pos, 20)

    # 画面を更新
    pygame.display.flip()

    # フレームレートを設定
    clock.tick(60)
