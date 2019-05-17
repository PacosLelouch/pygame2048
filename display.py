import pygame
import random
import sys
import math
class Display:
    texts = [
            [
            '炼气',#2
            '筑基',#4
            '开光',#8
            '胎息',#16
            '辟谷',#32
            '金丹',#64
            '元婴',#128
            '出窍',#256
            '分神',#512
            '合体',#1024
            '大乘',#2048
            '渡劫' #4096
            ]
        ]
    colors = []
    bgcolor = (250, 248, 239, 255)
    canvas_color = (187, 173, 160, 255)#(250, 150, 100, 20)
    stroke_color = (205, 193, 180, 255)#(255, 250, 150, 255)
    text_color = (119, 110, 101, 255)
    score_canvas_color = (187, 173, 160, 255)
    score_pre_color = (231, 228, 218, 255)
    score_color = (255, 255, 255, 255)
    bt_color1 = (147, 137, 128, 255)
    bt_color2 = (249, 246, 242, 255)
    #shining_color = (255, 255, 35, 51)
    step = 4
    def __init__(self, name='null', width=400, height=600, size=4, init_map=[], converted=False):
        pygame.init()
        Display.makeColor()
        self.screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF, 32)
        self.block_font = pygame.font.SysFont('SimHei', math.floor(width/size*0.32))
        self.instruction_font = pygame.font.SysFont('SimHei', 24)
        self.title_font = pygame.font.SysFont('SimHei', 64)
        self.width = width
        self.height = height
        self.gap_width = width * 0.01625
        self.rect_width = (width - self.gap_width * (size + 1)) / size
        self.map_size = size
        if converted:
            self.rects = init_map
        else:
            self.rects = Display.convert_map(init_map)
        '''test
        print(self.rects)
        '''
        self.name = name
        self.tick = 30 # framerate 30
        self.delta_time = 0
        self.moving = False
        self.framerate = pygame.time.Clock()
        self.score = 0
        self.instruction = ''
        self.radii = 5
        self.speed = 1 / Display.step # 可改，但是效果不能保证
        if size >= 6:
            self.speed *= 2
        self.new_blocks = [] # 用于解决某个问题→_→
        pygame.display.set_caption('2048(' + name + '), ' + str(size) + 'x' + str(size))

    def update(self, state=0, direction=0, next_map=None):
        self.framerate.tick(self.tick)
        ticks = pygame.time.get_ticks()
        if ticks == self.delta_time:
            return
        if next_map == None:
            next_map = Display.to_integer(self.rects)
        else:
            next_map = Display.convert_map(next_map)
        self.event_control()
        self.draw_background()
        self.draw_blocks()
        pygame.display.update()
        if state == 1 and not self.moving:
            self.moving = True
        if self.moving:
            if not self.move(direction):
                self.moving = False
                self.new_blocks = []
                self.sync_map(next_map)
        self.delta_time = ticks

    def updateScore(self, score):
        self.score = score

    def makeColor():
        Display.colors = [
            (238, 228, 218, 255),#2
            (237, 224, 200, 255),#4
            (242, 177, 121, 255),#8
            (245, 149, 99, 255), #16
            (246, 124, 95, 255), #32
            (246, 94, 59, 255),  #64
            (237, 207, 114, 255),#128
            (237, 204, 97, 255), #256
            (237, 200, 80, 255), #512
            (228, 185, 60, 255), #1024
            (237, 197, 40, 255), #2048
            (230, 224, 20, 255), #4096
            ]
        '''
        for i in range(len(Display.texts[0])):
            Display.colors.append((150 - i * 11, 255 - i * 15, 35 + i * 15, 100 + 4 * i))
        '''

    def move(self, direction):
        '''移动方块，返回是否还需要继续移动'''
        have_to_move = False
        if direction == 0:
            return
        '''下面判断是否能移动的条件：自己不是新生成的方块，且移动无障碍'''
        if direction == 1:
            self.rects.sort(key=lambda r:r[1], reverse=False)
            for rect in self.rects:
                if self.up(rect) and rect not in self.new_blocks:
                    have_to_move = True
                    rect[1] -= self.speed
        elif direction == 2:
            self.rects.sort(key=lambda r:r[1], reverse=True)
            for rect in self.rects:
                if self.down(rect) and rect not in self.new_blocks:
                    have_to_move = True
                    rect[1] += self.speed
        elif direction == 3:
            self.rects.sort(key=lambda r:r[0], reverse=False)
            for rect in self.rects:
                if self.left(rect) and rect not in self.new_blocks:
                    have_to_move = True
                    rect[0] -= self.speed
        elif direction == 4:
            self.rects.sort(key=lambda r:r[0], reverse=True)
            for rect in self.rects:
                if self.right(rect) and rect not in self.new_blocks:
                    have_to_move = True
                    rect[0] += self.speed
        add_rects = []
        '''test
        print(self.rects)
        print(self.new_blocks)
        print()
        '''
        for rect in self.rects:
            if self.count_overlap(rect) == 2:
                add_rects.append([round(rect[0]), round(rect[1]), rect[2] + 1])
                self.new_blocks.append([round(rect[0]), round(rect[1]), rect[2] + 1])
                #self.rects.remove(rect)
                self.rects = [[round(r[0]), round(r[1]), r[2]] for r in self.rects if not self.overlap(r, rect)] # for test
        self.rects += add_rects
        return have_to_move

    def sync_map(self, next_map):
        '''与后端地图同步'''
        self.rects = next_map

    def set_gameover_display(self):
        '''显示游戏结束时的画面'''
        pygame.display.set_caption('2048(Game Over)(' + self.name + '), ' + str(self.map_size) + 'x' + str(self.map_size))
        # 还有画面上的显示也要改变

    def to_integer(next_rects):
        '''这个方法整合后就没有用了'''
        return [[round(r[0]), round(r[1]), r[2]] for r in next_rects]

    def count_overlap(self, rect):
        '''数重叠方块数，用于消除方块'''
        count = 0
        for r in self.rects:
            if self.overlap(r, rect):
                count += 1
        return count

    def overlap(self, r1, r2):
        '''判断方块是否重叠'''
        return abs(r1[0] - r2[0]) < self.speed and abs(r1[1] - r2[1]) < self.speed
    
    def event_control(self):
        '''事件处理'''
        pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()

    def draw_background(self):
        '''画背景'''
        self.screen.fill(Display.bgcolor)
        Display.draw_round_rect(self.screen, Display.canvas_color, 0, self.height - self.width - self.gap_width, self.width, self.width + self.gap_width, self.radii)
        for x in range(self.map_size):
            for y in range(self.map_size):
                (x1, y1) = self.blockToCoor(x, y)
                Display.draw_round_rect(self.screen, Display.stroke_color, x1, y1, self.rect_width, self.rect_width, self.radii)
        Display.draw_round_rect(self.screen, Display.score_canvas_color, self.width - self.instruction_font.get_height() * 6 - self.gap_width * 2, self.gap_width, self.instruction_font.get_height() * 6 + self.gap_width, self.instruction_font.get_height() + self.gap_width * 2, self.radii)
        score_pre_text = self.instruction_font.render('Score ', True, Display.score_pre_color)
        self.screen.blit(score_pre_text, (self.width - self.instruction_font.get_height() * 6, self.gap_width * 2))
        score_text = self.instruction_font.render(str(self.score), True, Display.score_color)
        self.screen.blit(score_text, (self.width - self.instruction_font.get_height() * 6 + score_pre_text.get_width(), self.gap_width * 2))
        text = self.title_font.render('2048', True, Display.text_color)
        self.screen.blit(text, (self.gap_width, self.gap_width))

    def draw_blocks(self):
        '''画方块'''
        for rect in self.rects:
            self.draw_a_block(rect, self.gap_width / 2)

    def draw_a_block(self, rect, z=5):
        (x1, y1) = self.blockToCoor(rect[0], rect[1])
        current_color = Display.colors[rect[2] - 1] if rect[2] <= len(Display.colors) else (255, 255, 255, 100)#Display.colors[-1]
        current_text = Display.texts[0][rect[2] - 1] if rect[2] <= len(Display.texts[0]) else str(1 << rect[2])
        Display.draw_round_rect(self.screen, Display.darker(current_color, 20), x1, y1, self.rect_width, self.rect_width, self.radii)
        Display.draw_round_rect(self.screen, current_color, x1, y1 - z, self.rect_width, self.rect_width, self.radii)
        #if rect[2] >= 8:
        #    Display.draw_round_rect(self.screen, Display.shining_color, x1 - self.gap_width, y1 - z - self.gap_width, self.rect_width + 2 * self.gap_width, self.rect_width + 2 * self.gap_width, self.radii)
        #text = self.block_font.render(current_text, True, Display.text_color)
        text = self.block_font.render(current_text, True, (rect[2] <= 2 or rect[2] > len(Display.colors)) and Display.bt_color1 or Display.bt_color2)
        self.screen.blit(text, (x1 + self.rect_width/2 - text.get_width()/2, y1 + self.rect_width/2 - text.get_height()/2 - z))


    def update_score(self, score):
        '''更新分数'''
        self.score = score

    def blockToCoor(self, x, y):
        '''格子坐标转像素坐标'''
        return (x * self.rect_width + (x + 1) * self.gap_width, y * self.rect_width + (y + 1) * self.gap_width + self.height - self.width)

    def up(self, rect):
        return rect[1] > 0 and self.no_obstacle(rect[0], rect[1] - 1, rect[2])

    def down(self, rect):
        return rect[1] < self.map_size - 1 and self.no_obstacle(rect[0], rect[1] + 1, rect[2])

    def left(self, rect):
        return rect[0] > 0 and self.no_obstacle(rect[0] - 1, rect[1], rect[2])

    def right(self, rect):
        return rect[0] < self.map_size - 1 and self.no_obstacle(rect[0] + 1, rect[1], rect[2])

    def no_obstacle(self, x, y, z):
        '''没有新生成的[x, y, z]，且没有[x, y, z2]（z != z2）返回真'''
        return [r for r in self.rects if self.overlap([x, y, z], r) and (r in self.new_blocks or z != r[2])] == []
        
    def exit(self):
        pygame.quit()
        #sys.exit()

    def draw_round_rect(surface, color, x, y, width, height, radii = 5):
        '''画圆角矩形'''
        pygame.draw.rect(surface, color, pygame.Rect(x + radii, y, width - 2 * radii, radii), 0)
        pygame.draw.rect(surface, color, pygame.Rect(x, y + radii, radii, height - 2 * radii), 0)
        pygame.draw.rect(surface, color, pygame.Rect(x + width - radii - 1, y + radii, radii + 1, height - 2 * radii), 0)
        pygame.draw.rect(surface, color, pygame.Rect(x + radii, y + height - radii - 1, width - 2 * radii, radii + 1), 0)

        pygame.draw.ellipse(surface, color, pygame.Rect(x, y, radii * 2, radii * 2), 0)
        pygame.draw.ellipse(surface, color, pygame.Rect(x, y + height - radii * 2, radii * 2, radii * 2), 0)
        pygame.draw.ellipse(surface, color, pygame.Rect(x + width - radii * 2, y, radii * 2, radii * 2), 0)
        pygame.draw.ellipse(surface, color, pygame.Rect(x + width - radii * 2, y + height - radii * 2, radii * 2, radii * 2), 0)
        
        pygame.draw.rect(surface, color, pygame.Rect(x + radii, y + radii, width - 2 * radii, height - 2 * radii), 0)

    def darker(color, value):
        return (max(color[0] - value, 0), max(color[1] - value, 0), max(color[2] - value, 0), min(color[3] + value, 255))

    def convert_map(init_map):
        ans = []
        for x in range(len(init_map)):
            for y in range(len(init_map[x])):
                if init_map[x][y] > 0:
                    ans.append([x, y, init_map[x][y]])
        return ans

if __name__ == "__main__":
    init_map = [[1, 1, 1], [0, 1, 2], [0, 2, 9], [1, 3, 6], [2, 2, 2]]
    init_map.extend([[0, 0, 1], [1, 0, 3], [2, 0, 11], [3, 0, 8], [3, 1, 12], [3, 2, 13]])
    print(init_map)
    display = Display('Test', 400, 600, 4, init_map, True)
    direction = 0
    while True:
        state = 1
        key = pygame.key.get_pressed()
        if not display.moving:
            if key[pygame.K_UP]:
                direction = 1
            elif key[pygame.K_DOWN]:
                direction = 2
            elif key[pygame.K_LEFT]:
                direction = 3
            elif key[pygame.K_RIGHT]:
                direction = 4
            else:
                direction = 0
                state = 0
        display.update(state, direction)
