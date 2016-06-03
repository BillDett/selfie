import kivy
import picamera
import time
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from PIL import Image

class Widgets(FloatLayout):
	def generateFilename(self):
		return "/home/pi/js/web2/pix/picture_" + str(time.time()) + ".jpg"

	def overlay(self, camera, filename, delay):
		img = Image.open(filename)
		pad = Image.new('RGB', ( ((img.size[0] + 31) // 32) * 32, ((img.size[1] + 15) // 16) * 16,))
		pad.paste(img, (0, 0))
		o = camera.add_overlay(pad.tostring(), size=img.size)
		o.alpha = 128
		o.layer = 3
		o.rotation = 90
		time.sleep(delay)
		camera.remove_overlay(o)
	

	def takePicture(self):
		with picamera.PiCamera() as camera:
		    camera.resolution = (720, 960)
		    camera.framerate = 24
		    camera.start_preview()
		    camera.preview.window = 0,0,600,800
		    camera.preview.rotation = 90
		    time.sleep(2)
		    self.overlay( camera, 'Three.tiff', 0.5)
		    self.overlay( camera, 'Two.tiff', 0.5)
		    self.overlay( camera, 'One.tiff', 0.5)
		    self.overlay( camera, 'Flash.tiff', 0.10)
		    camera.stop_preview()
		    camera.capture(self.generateFilename())

class Selfie(App):
	def build(self):
		return Widgets()

if __name__ == '__main__':
	Selfie().run()


