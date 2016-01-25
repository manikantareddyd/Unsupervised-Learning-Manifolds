"""
HW1 - Robot motion and manifold Learning
	Code written for assignment for CS365A - Artificial Intelligence Programming
	Author - Archit Rathore (archit@iitk.ac.in)
"""
from __future__ import division
from PIL import Image
import sys, math, pygame, numpy
import geometry

# Initilize pygame modules
pygame.init()

# Define global variables
linecolor = [0, 200, 150]
linecolors = [(0,200,150),(250,100,50),(100,100,50),(0,0,150)]
room_coords = [(-200,-200),(200,-200),(200,200),(-200,200)]
BGCOLOR = 250,250,250				# background color for screen
HEIGHT = 700						# Height of screen
WIDTH = 900							# Width of screen
outimg_width = 10					# Width of output image

# Ceate a graphical window to work in :
screen = pygame.display.set_mode((WIDTH,HEIGHT))
# Import the robot image
robot_sprite = pygame.image.load("src/robot.png")

def rot_center(image, angle):
	"""rotate an image while keeping its center and size fixed"""
	orig_rect = image.get_rect()
	rot_image = pygame.transform.rotate(image, angle)
	rot_rect = orig_rect.copy()
	rot_rect.center = rot_image.get_rect().center
	rot_image = rot_image.subsurface(rot_rect).copy()
	return rot_image

def angle_to_twopoint(x_y,theta):
	"""Find line along angle theta from given point (x,y)

	Args:
	    x_y (list or tuple): start point
	    theta (float): value of angle

	Returns:
	    tuple: (x,y) of the point to construct the ray
	"""
	x2 = x_y[0] + math.cos(math.radians(theta))*1000
	y2 = x_y[1] + math.sin(math.radians(theta))*1000
	return x2,y2

def wall_ray_intersect_pt(ray_start, ray_end):
	"""Find intersection of given ray with walls

	Args:
	    ray_start (tuple): (x1,y1)
	    ray_end (tuple): (x2,y2)

	Returns:
	    Tuple: (x,y) coordinates of the intersection point,
	    none if ray doesn't intersect with any of the walls.
	"""
	for i in xrange(len(room_coords)):
		wall_start = room_coords[i]
		if i == len(room_coords)-1 :
			wall_end = room_coords[0]
		else:
			wall_end = room_coords[i+1]
		collision_pt = geometry.intersection_pt(wall_start,wall_end,ray_start,ray_end)
		if collision_pt != None:
			return collision_pt
	return None

class Robot(object):
	def __init__(self, x = 0, y = 0, theta = 0, FOV = 0):
		"""Constructor for robot class"""
		# Note the the image is assumed to be 32*32
		# If you intend to use some other sprite for the
		# robot you make appropriate in the draw() function
		self.image = pygame.image.load("src/robot.png")
		self.x = x
		self.y = y
		self.theta = theta
		self.FOV = FOV

	def draw_FOV(self,surface):
		"""Auxilary method - written for intermediate testing purpose

		Args:
		    surface (Pygame Surface object)

		Returns:
		    RGBA tuple
		"""
		x,y = self.x,self.y
		x2,y2 = angle_to_twopoint((self.x, self.y), self.theta)
		'''Uncomment the next line to visualize a ray emerging out from the robot
		and intersecting the walls: strictly for debugging and visualizing,
		remember to comment it while taking pixel values at point of intersection'''
		# pygame.draw.line(surface, linecolor, center_coord(x,y), center_coord(x2,y2))

		'''Find intersection with wall using method defined in geometry.py
		Due to precision issues it returns null for some values
		of theta near 0,90,180 and 270 degrees, so we keep only non null
		values
		'''
		int_point = wall_ray_intersect_pt((x,y),(x2,y2))
		if int_point:
			# print pygame.Surface.get_at(screen,[int(x) for x in center_coord(int_point[0],int_point[1])])
			return pygame.Surface.get_at(screen,[int(x) for x in center_coord(int_point[0],int_point[1])])

	def take_picture(self,surface):
		"""Take a picture from the viewpoint of the robot.
		The picture has the angular width of the FOV (field of view)
		of the robot.

		Args:
		    surface (pygame.Surface): surface to sample pixel values from

		Returns:
		    RGBA list: returns list of RGBA values that form the image that
		    the robot sees.
		"""
		image_array = []
		# Save initial theta to restore later
		theta_ini = self.theta
		self.theta = self.theta - int(self.FOV/2)

		# Captures pixel values at 0.2 degree increments -
		# you can use finer/coarser increments to get more
		# detailed/coarser pictures
		increment = 0.2
		flag=1
		for x in numpy.arange(0,self.FOV,increment):
			x,y = self.x, self.y
			x_dash,y_dash = angle_to_twopoint((self.x,self.y),self.theta)
			int_point = wall_ray_intersect_pt((x,y),(x_dash,y_dash))
			'''Find intersection with wall using method defined in geometry.py
			Due to precision issues it returns null for some values
			of theta near 0,90,180 and 270 degrees, so we keep only non null
			values
			'''
			if int_point:
				for i in range(flag):
					image_array.append(pygame.Surface.get_at(screen,[int(x) for x in center_coord(int_point[0],int_point[1])])[:3])
				flag = 1
			else:
				if image_array:
					image_array.append(image_array[-1])
				else:
					flag += 1
			self.theta += increment
		self.theta = theta_ini
		return image_array


	def draw(self, surface):
		"""Draw on the provided surface

		Args:
		    surface (pygame surface object): where to draw the robot

		Returns:
		    VOID
		"""
		x,y = center_coord(self.x,self.y)
		surface.blit(rot_center(self.image,self.theta), center_coord(self.x-16,self.y+16))


def center_coord(x,y):
	"""Convert coordinate tuple to pygame's coordinates
	Pygame assumes origin at top-left corner. Calling this
	function allows you to assume the origin at center of
	screen.

	Args:
		coords (tuple): tuple of type (x1,y1)

	Returns:
		Tuple: Returns transformed coordinates
	"""
	return WIDTH/2+x, HEIGHT/2-y

def draw_poly(vertices):
	"""Function to draw a polygon with given vertices
	assuming that the vertices are given in clockwise
	order

	Args:
		vertices (list of tuples): Takes a list of tuples
		of the form (x_i,y_i)

	Returns:
		NONE: Doesn't return a value
	"""
	for i, linecolor in zip(xrange(len(vertices)),linecolors):
		x1,y1 = vertices[i]
		if i == len(vertices)-1 :
			x2,y2 = vertices[0]
		else :
			x2,y2 = vertices[i+1]
		pygame.draw.aaline(screen, linecolor, center_coord(x1,y1),center_coord(x2,y2))

def save_picture(pixel_value_list,filename):
	environment = Image.new("RGB",(len(image_data),outimg_width))
	environment.putdata(tuple(image_data)*outimg_width)
	environment.save(filename)

def move_robot(x,y,theta):
	"""TODO

	Args:
	    x (TYPE): Description
	    y (TYPE): Description
	    theta (TYPE): Description

	Returns:
	    TYPE: Description
	"""
	pass


from os import mkdir
import random
import sys
coord=[]
random.seed(900)
for i in range(0,100):
	X_cor = random.randint(-180,180)
	Y_cor = random.randint(-180,180)
	coord.append([X_cor,Y_cor])
	for j in range(0,100):
		robot = Robot(x=X_cor,y=Y_cor,theta=int((j*360/100)),FOV=120)
		screen.fill(BGCOLOR)
		draw_poly(room_coords)
		robot.draw(screen)
		pygame.display.flip()
		image_data = robot.take_picture(screen)
		filname = 'img/train/'+str(X_cor)+'_'+str(Y_cor)+'_'+str(j)+'.png'
		save_picture(image_data,filname)

coord = numpy.array(coord)
numpy.savetxt('train_Coords.csv',coord,delimiter=",")
coord=[]
random.seed(9000)
for i in range(0,100):
	X_cor = random.randint(-180,180)
	Y_cor = random.randint(-180,180)
	t     = random.randint(0,360)
	coord.append([X_cor,Y_cor,t])	
	robot = Robot(x=X_cor,y=Y_cor,theta=t,FOV=120)
	screen.fill(BGCOLOR)
	draw_poly(room_coords)
	robot.draw(screen)
	pygame.display.flip()
	image_data = robot.take_picture(screen)
	filname = 'img/test/'+str(X_cor)+'_'+str(Y_cor)+'_'+str(i)+'.png'
	save_picture(image_data,filname)

coord = numpy.array(coord)
numpy.savetxt('test_Coords.csv',coord,delimiter=",")
#144 points in square so 12x12, 12 points in (-180,180,30) 360/30