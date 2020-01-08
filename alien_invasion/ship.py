#coding:utf-8
import pygame
class Ship():
	def __init__(self,all_settings,screen):
		"""set init positiong"""
		self.screen=screen
		self.all_settings=all_settings
		#���طɴ�ͼ�񲢻�ȡ����Ӿ���
		self.image=pygame.image.load('images\ship.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		
		#��ÿ�ҷɴ�������Ļ�ײ�����
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		
		self.center=float(self.rect.centerx)
		
		self.moving_right=False
		self.moving_left=False
		
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center+=self.all_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center-=self.all_settings.ship_speed_factor#ע��˴��Ǽ��� ��Ϊ����x����
		
		self.rect.centerx=self.center
	def blitme(self):
		"""draw position"""
		self.screen.blit(self.image,self.rect)
