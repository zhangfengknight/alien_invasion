#coding:utf-8

import sys
import pygame
from bullet import Bullet

def check_events(all_settings,screen,ship,bullets):
	"""Corresponding buttons and mouse"""
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
			
		elif event.type==pygame.KEYDOWN:#���¼�ʱ
			check_keydown_events(event,all_settings,screen,ship,bullets)
			check_keydown_events(event,all_settings,screen,ship,bullets)
		elif event.type==pygame.KEYUP:#�ɿ���ʱ
			check_keyup_events(event,ship)
			#check_keydown_events(event,all_settings,screen,ship,bullets)
def update_screen(all_settings,screen,ship,bullets):
	"""update screen turn new screen"""
	#ÿ��ѭ��ʱ���ػ���Ļ
	screen.fill(all_settings.bg_color)#�����Ļ ֻ����һ������
	ship.blitme()#���Ʒɴ�
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	#��������Ƶ���Ļ�ɼ�
	pygame.display.flip()
def check_keydown_events(event,all_settings,screen,ship,bullets):#����
	if event.key==pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key==pygame.K_LEFT:
		ship.moving_left=True
	elif event.key==pygame.K_SPACE:
		#bullets.space=True
		if len(bullets) < all_settings.bullets_allowed:
			new_bullet=Bullet(all_settings,screen,ship)
			bullets.add(new_bullet)
def check_keyup_events(event,ship):#�ɼ�
	if event.key==pygame.K_RIGHT:
		ship.moving_right=False
	elif event.key==pygame.K_LEFT:
		ship.moving_left=False
	#elif event.key==pygame.K_SPACE:
		#bullets.space=False	

def update_bullets(bullets):	
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
			
