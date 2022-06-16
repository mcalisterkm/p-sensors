import board
import busio
import time
import digitalio
import adafruit_mcp230xx 
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
lcd_columns = 16
lcd_rows = 2
# import adafruit_character_lcd.character_lcd as characterlcd
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)
lcd.message = "Hello LCD1"
mcp = adafruit_mcp230xx.MCP23017(i2c)
# create buttons
up = mcp.get_pin(3)
down = mcp.get_pin(2)
left = mcp.get_pin(4)
right = mcp.get_pin(1)
select = mcp.get_pin(0)
#Define buttons as input
up.direction = digitalio.Direction.INPUT
down.direction = digitalio.Direction.INPUT
left.direction = digitalio.Direction.INPUT
right.direction = digitalio.Direction.INPUT
select.direction = digitalio.Direction.INPUT
#Create pull-ups for each button
up.pull = digitalio.Pull.UP
down.pull = digitalio.Pull.UP
left.pull = digitalio.Pull.UP
right.pull = digitalio.Pull.UP
select.pull = digitalio.Pull.UP
lcd.message = "Hello LCD2"
lcd.clear()
#while True:
	# create buttons
lcd.message = "Button Status /n"
lcd.message = "up %r" % up.value
#	lcd.message = "down %r" %  down.value
#	lcd.message = "left %r" % left.value
#	lcd.message = "right %r" % right.value
#	lcd.message = "select %r" % select.value
#	time.sleep(5)
