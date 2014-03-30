class MockDialog():
	def create(self, text):
		return
	def update(self, percent, message):
		return
	def close(self):
		return

def DialogProgress():
	return MockDialog()


class MockListItem():
	def addContextMenuItems(self, text):
		return
	def setProperty(self, a, b):
		return
	def setInfo(self, type = '', infoLabels = ''):
		return
def ListItem(name, iconImage = "", thumbnailImage = ""):
	return MockListItem()





