import maya.cmds as cmds
import shutil
import os

def rsnormal():
	content=[]
	newcontent=[]
	
	rsNode=cmds.ls(type='RedshiftNormalMap')
	workspace=cmds.workspace( q=True, rd=True )
	sourceimages=workspace+'sourceimages'
	normalContent=sourceimages+'/rsNormalMap'
	os.chdir(sourceimages)
	isExists=os.path.exists('rsNormalMap')


	#判断目录是否存在
	if not isExists:
		os.makedirs('rsNormalMap') 
	else:
		pass
	#复制文件到rsNormalMap
	for i in rsNode:
		fileTextureName = cmds.getAttr(i + '.tex0')
		content.append(fileTextureName)
	for oldfile in content:
		
		a=oldfile.split("/")
		b=a[-1]
		newpath=normalContent+'/'+b
		newcontent.append(newpath)
		if newpath != oldfile:
			shutil.copy(oldfile,normalContent)
		else:
			pass
	#重新链接rsNormalMap
	for i in range(len(content)):
		cmds.setAttr(rsNode[i] + '.tex0',newcontent[i],type = 'string')

def rsdomelight():
	content=[]
	newcontent=[]

	rsNode=cmds.ls(type='RedshiftDomeLight')
	workspace=cmds.workspace( q=True, rd=True )
	sourceimages=workspace+'sourceimages'
	hdriContent=sourceimages+'/rsHDRI'
	os.chdir(sourceimages)
	isExists=os.path.exists('rsHDRI')


	#判断目录是否存在
	if not isExists:
		os.makedirs('rsHDRI')
	else:
		pass
	#复制文件到rsHDRI
	for i in rsNode:
		fileTextureName = cmds.getAttr(i + '.tex0')
		content.append(fileTextureName)
	for oldfile in content:
		
		a=oldfile.split("/")
		b=a[-1]
		newpath=hdriContent+'/'+b
		newcontent.append(newpath)
		if newpath != oldfile:
			shutil.copy(oldfile,hdriContent)
		else:
			pass
	#重新链接rsHDRI
	for i in range(len(content)):
		cmds.setAttr(rsNode[i] + '.tex0',newcontent[i],type = 'string')

RSLINK=cmds.window(t='RSLINK',w=200)
cmds.rowColumnLayout('global')
cmds.separator(h=10)
cmds.button('move rsNormalMap',w=200,h=50,c='rsnormal()')
cmds.separator(h=10)
cmds.button('move rsHDRI',w=200,h=50,c='rsdomelight()')
cmds.separator(h=10)
cmds.showWindow(RSLINK)
