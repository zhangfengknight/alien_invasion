#coding:utf-8

import sys
import pygame
from bullet import Bullet

def check_events(all_settings,screen,ship,bullets):
	"""Corresponding buttons and mouse"""
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
			
		elif event.type==pygame.KEYDOWN:#按下键时
			check_keydown_events(event,all_settings,screen,ship,bullets)
			check_keydown_events(event,all_settings,screen,ship,bullets)
		elif event.type==pygame.KEYUP:#松开键时
			check_keyup_events(event,ship)
			#check_keydown_events(event,all_settings,screen,ship,bullets)
def update_screen(all_settings,screen,ship,bullets):
	"""update screen turn new screen"""
	#每次循环时都重绘屏幕
	screen.fill(all_settings.bg_color)#填充屏幕 只接受一个参数
	ship.blitme()#绘制飞船
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	#让最近绘制的屏幕可见
	pygame.display.flip()
def check_keydown_events(event,all_settings,screen,ship,bullets):#按键
	if event.key==pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key==pygame.K_LEFT:
		ship.moving_left=True
	elif event.key==pygame.K_SPACE:
		#bullets.space=True
		if len(bullets) < all_settings.bullets_allowed:
			new_bullet=Bullet(all_settings,screen,ship)
			bullets.add(new_bullet)
def check_keyup_events(event,ship):#松键
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
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
			
