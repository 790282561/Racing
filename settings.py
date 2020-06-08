'''本文件是关于游戏结束、得分等设置的文件'''
import time
import pygame
from enemy_car import Enemy
import lives

'''图像生成系统'''
def enemy_generate(locationgroup, enemycargroup, screen):
    for lo in locationgroup:
        enemycargroup.add(Enemy(screen, lo))

def life_generate(palyer_car_lives, screen, livesgroup):
    for life_num in range(palyer_car_lives):
        life = lives.Lives(screen)
        life.rect.x = 180 - 20 * life_num
        livesgroup.add(life)

'''结束结算系统'''
def enemy_reset(enemycargroup):
    #重置
    enemycargroup.empty()

def playercar_lives(palyer_car_lives, enemycargroup):
    #生命为零重置游戏
    palyer_car_lives -= 1
    if palyer_car_lives == 0:
        game_over(enemycargroup)
        time.time()


'''得分系统'''
def read_score():
    # 读取最高分数
    read_text = []
    with open('score.txt', 'r+') as highest_score_text:
        lines = highest_score_text.readlines()
        for line in lines:
            read_text.append(int(line))
    max_read_text = max(read_text)
    return max_read_text

def text_getscore(starttime):
    #获得分数
    endtime = time.time()
    text_x = str(round(endtime - starttime))
    return text_x

def print_text(screen, text_x):
    #显示字体在左上角
    score_font = pygame.font.SysFont("simhei", 24)
    imgText = score_font.render(str(text_x), False, (0, 0, 0))
    screen.blit(imgText, (0, 0))

def highesttext_getscore(text_x, highest_score, playerscorelists):
    #获得最高分
    if int(text_x) > int(highest_score):
        playerscorelists.append(text_x)
        with open('score.txt', 'r+') as highest_score_text:
            highest_score_text.write(str(text_x))

def print_highesttext(screen, highest_score):
    #显示字体在左上角
    score_font = pygame.font.SysFont("simhei", 24)
    imgText = score_font.render(str(highest_score), False, (0, 0, 0))
    screen.blit(imgText, (80, 0))


