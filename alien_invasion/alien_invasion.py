#coding:utf-8

import pygame
from ship import Ship
from settings import Settings
import game_functions as gf
from pygame.sprite import Group
#from bullet import Bullet
def run_game(): 
	pygame.init()
	all_settings=Settings()
	screen=pygame.display.set_mode(
		(all_settings.screen_width,all_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#创建一艘飞船
	ship=Ship(all_settings,screen)
	#创建一个用于储存子弹的编组
	bullets=Group()
	
	#开始游戏的主循环
	while True:
		
		#监听键鼠事件
		gf.check_events(all_settings,screen,ship,bullets)
		gf.check_events(all_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(bullets)
		
		
		gf.update_screen(all_settings,screen,ship,bullets)
		#重新加载飞船图像
		gf.update_screen(all_settings,screen,ship,bullets)	
		
run_game()
