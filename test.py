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



def show_letter(letter):
	for i in range(len(characters)):
		if characters[i][1] == letter:
			print(str(letter) + ' is ' + str(characters[i][0]))
			for j in range(8):
				MAX7219array.send_matrix_reg_byte(1, j+1, characters[i][0][j])


def scroll_letter(letter, matrix):
	for i in range(len(characters)):
		if characters[i][1] == letter:
			print(str(letter) + ' is ' + str(characters[i][0]))
			for n in range(8):
				for j in range(8):
					MAX7219array.send_matrix_reg_byte(matrix, j+1, characters[i][0][j]*2**n)
				time.sleep(0.1)
				MAX7219array.clear_all()


def scroll_letter_left(letter, matrix):
	for i in range(len(characters)):
		if characters[i][1] == letter:
			print(str(letter) + ' is ' + str(characters[i][0]))
			for n in range(8):
				for j in range(8):
					MAX7219array.send_matrix_reg_byte(matrix, j+1, characters[i][0][j]/2**n)
				time.sleep(0.1)
				MAX7219array.clear_all()


#n - step of movement
#j - row
def scroll_letter_LR(letter):
	for i in range(len(characters)):
		if characters[i][1] == letter:
			print(str(letter) + ' is ' + str(characters[i][0]))
			for n in range(16):
				for j in range(8):
					MAX7219array.send_matrix_reg_byte(1, j+1, characters[i][0][j]*2**n)
					if characters[i][0][j]*2**n >128:
						nextDisplay = characters[i][0][j]*2**n/256
						MAX7219array.send_matrix_reg_byte(0, j+1, nextDisplay)

				time.sleep(0.1)
				MAX7219array.clear_all()

def scroll_letter_RL(letter):
	for i in range(len(characters)):
		if characters[i][1] == letter:
			print(str(letter) + ' is ' + str(characters[i][0]))
			for n in range(16):
				for j in range(8):
					thing = characters[i][0][j]
					thingf = float(thing)
					valf = float(thingf/2**n)
					lower = valf - int(valf)
					MAX7219array.send_matrix_reg_byte(0, j+1, int(valf))
					MAX7219array.send_matrix_reg_byte(1, j+1, int(lower*256))

				time.sleep(0.1)
				MAX7219array.clear_all()

def scrollLR(thing):
	for i in range(16):
		val = thing*2**i
		print(val)
		MAX7219array.send_matrix_reg_byte(1, 1, val)
		if val > 128:
			MAX7219array.send_matrix_reg_byte(0, 1, val/256)
		time.sleep(0.2)

def scrollRL(thing):
	for i in range(16):
		thingf = float(thing)
		valf = float(thingf/2**i)
		lower = valf - int(valf)
		MAX7219array.send_matrix_reg_byte(0, 1, int(valf))
		MAX7219array.send_matrix_reg_byte(1,1, int(lower*256))
		time.sleep(0.5)
			


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
([94, 51, 62, 48, 30, 0, 0, 0],'a'),						#a
([59, 102, 102, 62, 6, 6, 7, 0],'b'),						#b
([30, 51, 3, 51, 30, 0, 0, 0],'c'),							#c
([110, 51, 51, 62, 48, 48, 56, 0],'d'),						#d
([30, 3, 63, 51, 30, 0 , 0, 0],'e'),						#e
([15, 6, 6, 15, 6, 54, 28, 0],'f'),							#f
([31, 48, 62, 51, 51, 110, 0, 0],'g'),						#g
([103, 102, 102, 110, 54, 6, 7, 0],'h'),					#h
([15, 6, 6, 6, 7, 0, 6, 0],'i'),							#i
([30, 51, 51, 48, 48, 48, 0, 48],'j'),						#j
([103, 54, 30, 54, 102, 7, 0, 0],'k'),						#k
([15, 6, 6, 6, 6, 6, 7, 0],'l'),							#l
([99, 107, 127, 127, 51, 0, 0, 0],'m'),						#m
([51, 51, 51, 51, 31, 0, 0, 0],'n'),						#n
([30, 51, 51, 51, 30, 0, 0, 0],'o'),						#o
([15, 6, 62, 102, 102, 59, 0, 0],'p'),						#p
([102, 48, 62, 51, 110, 0, 0, 0],'q'),						#q
([15, 6, 102, 110, 59, 0, 0, 0],'r'),						#r
([31, 48, 30, 3, 62, 0, 0, 0],'s'),							#s
([12, 22, 6, 6, 31, 6, 8, 0],'t'),							#t
([110, 51, 51, 51, 51, 0, 0, 0],'u'),						#u
([12, 30, 51, 51, 51, 0, 0, 0],'v'),						#v
([54, 127, 127, 107, 99, 0, 0, 0],'w'),						#w
([99,  54, 28, 54, 99, 0, 0, 0],'x'),						#x
([31, 48, 62, 51, 51, 51, 0, 0],'y'),						#y
([63, 38, 12, 25, 63, 0, 0, 0],'z')							#z
]


#255 is maximum per row


try:
	running_dot()
	#running_dot()

	# MAX7219array.send_matrix_reg_byte(0, 1, int('10101010', 2))
	time.sleep(1)
	MAX7219array.clear_all();
	
	test = 'hello'
	for i in range(len(test)):
		scroll_letter_RL(test[i])

	#-- Clock on repeat --
	#while True:
	#	show_time()
	#	time.sleep(5)
	MAX7219array.clear_all()

except KeyboardInterrupt:
	MAX7219array.clear_all()
