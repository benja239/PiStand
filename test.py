import MAX7219array
import time
import datetime


def running_dot():
	print("running_dot")
	
	MAX7219array.send_all_reg_byte(1, 255)
	MAX7219array.send_all_reg_byte(8, 255)
	for i in range(6):
		MAX7219array.send_matrix_reg_byte(0, i+2, 128)
	for i in range(6):
		MAX7219array.send_matrix_reg_byte(1, i+2, 1)

	ring=[127, 191, 223, 239, 247, 251, 253, 254,255]
	ring2=[254, 253, 251, 247, 239, 223, 191, 127, 255]

	for i in range(2):
		for n in range(8):
			MAX7219array.send_matrix_reg_byte(i, 1, ring[n])
			time.sleep(0.04)
		MAX7219array.send_matrix_reg_byte(i, 1, ring[8])

	for i in range(6):
		MAX7219array.send_matrix_reg_byte(1, i+2, 0)
		time.sleep(0.04)
		MAX7219array.send_matrix_reg_byte(1, i+2, 1)

	for i in range(2):
		for n in range(8):
			MAX7219array.send_matrix_reg_byte(1-i, 8, ring2[n])
			time.sleep(0.04)
		MAX7219array.send_matrix_reg_byte(1-i, 8, ring2[8])

	for i in range(5):
		MAX7219array.send_matrix_reg_byte(0, 6-i, 0)
		time.sleep(0.04)
		MAX7219array.send_matrix_reg_byte(0, 6-i, 128)

def display(char, matrix):
	temp = int(char)

	for i in range(8):
		MAX7219array.send_matrix_reg_byte(matrix, i+1, numbers[temp][i])
		

def display_scroll_char(char, matrix):
	temp = int(char)

	for n in range(8):		
		for i in range(8):
			MAX7219array.send_matrix_reg_byte(matrix, i+1, numbers[temp][i]*2**n)
		time.sleep(0.1)
		MAX7219array.clear_all()

def show_time():
	print(time.strftime('%H:%M'))
	hour = time.strftime('%H')
	minu = time.strftime('%M')

	
	display(hour[0], 1)
	display(hour[1], 0)

	time.sleep(0.5)

	MAX7219array.clear_all()

	time.sleep(0.1)

	display_scroll_char(10, 1) #: is 10 in chars
	display_scroll_char(10, 0) #: is 10 in chars

	display(minu[0], 1)
	display(minu[1], 0)

	time.sleep(0.5)

	MAX7219array.clear_all()


	#REFERENCING LETTERS
	#test = [(a,0), (b,0)]
	#for i in range(len(test)):
	#if test[i][0] == 'a':
	#	print(test[i])

##############################################################################
#MAIN
##############################################################################
MAX7219array.init()

# d1 = [63, 12, 12, 12, 12, 14, 12, 0]
# d2 = [63, 51, 6, 28, 48, 51, 30, 0]
# d3 = [30, 51, 48, 28, 48, 51, 30, 0]
# d4 = [120, 48, 127, 51, 54, 60, 56, 0]
# d5 = [30, 51, 48, 48, 31, 3, 63, 0]
# d6 = [30, 51, 51, 31, 3, 6, 28, 0]
# d7 = [12, 12, 12, 24, 48, 51, 63, 0]
# d8 = [30, 51, 51, 30, 51, 51, 30, 0]
# d9 = [14, 24, 48, 62, 51, 51, 30, 0]
# d0 = [62, 103, 111, 123, 115, 99, 62, 0]

numbers = [
[62, 103, 111, 123, 115, 99, 62, 0], 				#0
[63, 12, 12, 12, 12, 14, 12, 0], 					#1
[63, 51, 6, 28, 48, 51, 30, 0], 					#2
[30, 51, 48, 28, 48, 51, 30, 0], 					#3
[120, 48, 127, 51, 54, 60, 56, 0], 					#4
[30, 51, 48, 48, 31, 3, 63, 0], 					#5
[30, 51, 51, 31, 3, 6, 28, 0], 						#6 
[12, 12, 12, 24, 48, 51, 63, 0], 					#7
[30, 51, 51, 30, 51, 51, 30, 0], 					#8
[14, 24, 48, 62, 51, 51, 30, 0],					#9
[0, 3, 3, 0, 0, 3, 3, 0]]							#:

colon = [0, 12, 12, 0, 0, 12, 12, 0]

characters = [
[94, 51, 62, 48, 30, 0, 0, 0],						#a
[59, 102, 102, 62, 6, 6, 7, 0],						#b
[30, 51, 3, 51, 30, 0, 0, 0],						#c
[110, 51, 51, 62, 48, 48, 56, 0],					#d
[30, 3, 63, 51, 30, 0 , 0],							#e
[15, 6, 6, 15, 6, 54, 28, 0],						#f
[31, 48, 62, 51, 51, 110, 0, 0],					#g
[103, 102, 102, 110, 54, 6, 7, 0],					#h
[15, 6, 6, 6, 7, 0, 6, 0],							#i
[30, 51, 51, 48, 48, 48, 0, 48],					#j
[103, 54, 30, 54, 102, 7, 0],						#k
[15, 6, 6, 6, 6, 6, 7, 0],							#l
[99, 107, 127, 127, 51, 0, 0, 0],					#m
[51, 51, 51, 51, 31, 0, 0, 0],						#n
[30, 51, 51, 51, 30, 0, 0, 0],						#o
[15, 6, 62, 102, 102, 59, 0, 0],					#p
[102, 48, 62, 51, 110, 0, 0 ],						#q
[15, 6, 102, 110, 59, 0, 0, 0],						#r
[31, 48, 30, 3, 62, 0, 0, 0],						#s
[12, 22, 6, 6, 31, 6, 8, 0],						#t
[110, 51, 51, 51, 51, 0, 0, 0],						#u
[12, 30, 51, 51, 51, 0, 0, 0],						#v
[54, 127, 127, 107, 99, 0, 0, 0],					#w
[99,  54, 28, 54, 99, 0, 0, 0],						#x
[31, 48, 62, 51, 51, 51, 0, 0],						#y
[63, 38, 12, 25, 63, 0, 0, 0]						#z
]





try:
	running_dot()
	running_dot()

	# MAX7219array.send_matrix_reg_byte(0, 1, int('10101010', 2))
	time.sleep(1)
	MAX7219array.clear_all();
	# display_scroll_char(numbers[1], 1)
	# display_scroll_char(numbers[7], 1)
	# display_scroll_char(colon, 1)
	# display_scroll_char(numbers[3], 1)
	# display_scroll_char(numbers[2], 1)
	########################
	#for i in range(8):
	#	MAX7219array.send_matrix_reg_byte(1, i, characters[0][i])
	#time.sleep(10)
	while True:
		show_time()
		time.sleep(5)
	MAX7219array.clear_all()

except KeyboardInterrupt:
	MAX7219array.clear_all()
