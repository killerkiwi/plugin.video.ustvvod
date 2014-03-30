class MockAddon():
	def getAddonInfo(self, text):
		return text
	def getSetting(self, text):
		if text is "connectiontype":
			return 0
		return text
	def getLocalizedString(self, text):
		if text is "connectiontype":
			return 0
		return text
def Addon(text="", id=0):
	return MockAddon()
