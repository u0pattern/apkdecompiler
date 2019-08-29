import os
cwd = os.path.dirname(os.path.realpath(__file__))
class APKDecompile:
	def __init__( self, apkfile ):
		self.apkfile = apkfile
	def inFolder(self,folder):
		os.system(cwd+'/needs/jadx/bin/jadx -d '+str(folder)+' '+str(self.apkfile))