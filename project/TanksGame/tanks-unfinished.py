import sys, pygame, time
from random import randint
from pygame.locals import *

class TankMain(object):
    width = 1000
    height = 750
    # 开始游戏
    def startGame(self):
        pygame.init() # 模块初始化
        # 创建屏幕，屏幕大小（宽，高），窗口特性（0,RESIZABLE,FULLSCREEM）
        screem = pygame.display.set_mode((TankMain.width, TankMain.height), 0, 32)
        pygame.display.set_caption("坦克大战")  # 设置标题
        my_tank = My_Tank(screem)
        enemy_list = []
        for i in range(1, 6):
            enemy_list.append(Enemy_Tank(screem))
        while True:
            time.sleep(0.05) # 显示间隔
            screem.fill((255, 255, 255))  # 设置背景颜色
            screem.blit(self.write_text(), (0, 5)) # 显示文字
            self.get_event(my_tank)

            my_tank.display() # 显示坦克
            my_tank.move()

            for enemy in enemy_list:
                enemy.display()
                enemy.random_move()

            pygame.display.update()

    # 关闭游戏
    def stopGame(self):
        sys.exit()
    # 打印文字内容
    def write_text(self):
        font = pygame.font.SysFont("simsunnsimsun", 15) #定义字体
        text_sf = font.render("敌方坦克数量为5", True,(255, 0, 0)) #创建图像
        return text_sf


    # 获取所有事件
    def get_event(self, my_tank):
        for event in pygame.event.get():
            if event.type == QUIT: # 退出
                self.stopGame()
            if event.type == KEYDOWN: # 键盘输入
                if event.key == K_LEFT or event.key == K_a: # 左
                    my_tank.direction = "L"
                    my_tank.stop = False
                    #my_tank.move()
                if event.key == K_RIGHT or event.key == K_d: # 右
                    my_tank.direction = "R"
                    my_tank.stop = False
                   # my_tank.move()
                if event.key == K_UP or event.key == K_w: # 上
                    my_tank.direction = "U"
                    my_tank.stop = False
                    #my_tank.move()
                if event.key == K_DOWN or event.key == K_s: # 下
                    my_tank.direction = "D"
                    my_tank.stop = False
                    #my_tank.move()
                if event.key == K_ESCAPE: # exc
                    self.stopGame()
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT or event.key == K_UP or event.key == K_DOWN or event.key == K_a or event.key == K_w or event.key == K_s or event.key == K_d:
                    my_tank.stop = True

# 坦克类
class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
class Tank(BaseItem):
    width = 50
    height = 51
    def __init__(self,screem,left,top):
        super().__init__()
        self.screem = screem # 显示坦克的移动
        self.direction = "U" # 默认方向
        self.speed = 5 # 坦克速度
        self.stop = False
        self.images = {}
        self.images["U"] = pygame.image.load("C:/Users/pc/Desktop/images/U.gif") # 上
        self.images["D"] = pygame.image.load("C:/Users/pc/Desktop/images/D.gif") # 下
        self.images["L"] = pygame.image.load("C:/Users/pc/Desktop/images/L.gif") # 左
        self.images["R"] = pygame.image.load("C:/Users/pc/Desktop/images/R.gif") # 右
        self.image = self.images[self.direction] # 根据方向取图片
        self.rect = self.image.get_rect() # 得到边界
        self.rect.left = left
        self.rect.top = top
        self.live = True # 坦克存活
    def display(self):
        self.image = self.images[self.direction]
        self.screem.blit(self.image, self.rect)
    def move(self):
        pass
    def fire(self):
        pass
# 我方坦克
class My_Tank(Tank):
    def __init__(self, screem):
        super().__init__(screem, 450, 700)
        self.stop=True
    def move(self):
        if not self.stop: # 判断坦克是否停止
            if self.direction == "L":
                if self.rect.left > 0:
                    self.rect.left -= self.speed
                else:
                    self.rect.left = 0
            elif self.direction == "R":
                if self.rect.right < TankMain.width:
                    self.rect.right += self.speed
                else:
                    self.rect.right = TankMain.width
            elif self.direction == "U":
                if self.rect.top > 0:
                    self.rect.top -= self.speed
                else:
                    self.rect.top = 0
            else:
                if self.rect.bottom < TankMain.height:
                    self.rect.bottom += self.speed
                else:
                    self.rect.bottom = TankMain.height

# 敌方坦克
class Enemy_Tank(Tank):

    def __init__(self, screem):
        super().__init__(screem, randint(1, 5)*150, 100)
        self.speed = 10
        self.step = 6
        self.get_random_direction()

    def get_random_direction(self):
        r = randint(0, 4)
        if r == 4:
            self.stop = True
        elif r == 1:
            self.direction = "L"
            self.stop = False
        elif r == 2:
            self.direction = "R"
            self.stop = False
        elif r == 3:
            self.direction = "D"
            self.stop = False
        elif r == 0:
            self.direction = "U"
            self.stop = False
    def random_move(self): #随机方向连续移动6步
        if self.live:
            if self.step == 0:
                self.get_random_direction()
                self.step = 6
            else:
                self.move()
                self.step -= 1



if __name__=="__main__":
    game = TankMain()
    game.startGame()