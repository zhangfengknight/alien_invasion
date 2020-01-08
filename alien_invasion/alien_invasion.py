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
	
	#����һ�ҷɴ�
	ship=Ship(all_settings,screen)
	#����һ�����ڴ����ӵ��ı���
	bullets=Group()
	
	#��ʼ��Ϸ����ѭ��
	while True:
		
		#���������¼�
		gf.check_events(all_settings,screen,ship,bullets)
		gf.check_events(all_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(bullets)
		
		
		gf.update_screen(all_settings,screen,ship,bullets)
		#���¼��طɴ�ͼ��
		gf.update_screen(all_settings,screen,ship,bullets)	
		
run_game()
