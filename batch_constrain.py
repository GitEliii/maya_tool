import maya.cmds as cmds

#functions
Constrain_mode='parentConstraint'
check=0
targets=[]
objects=[]
def changeMode(mode):
    global Constrain_mode
    Constrain_mode=mode
    print 'Current Mode is '+Constrain_mode
def setTargets():
    global targets
    targets=cmds.ls(sl=1)
def setObjects():
    global objects
    objects=cmds.ls(sl=1)
def changeCheck():
    global check
    check=cmds.checkBox('maintainOffset',q=1,value=1)
def constrain():
    for i in objects:
        command='cmds.'+str(Constrain_mode)+'('+'%s'%targets+','+'\''+i+'\''+',mo=%s)'%check
        exec(command)

#GUI
window=cmds.window(t='constrain_tool',w=200)
cmds.rowColumnLayout('global')

cmds.text(label="Step1 : Set constrain mode",h=20,p='global',al='left')
cmds.optionMenu('mode',label='Mode:',changeCommand=changeMode)
cmds.menuItem( label='parentConstraint' )
cmds.menuItem( label='pointConstraint' )
cmds.menuItem( label='orientConstraint' )
cmds.menuItem( label='scaleConstraint' )
cmds.menuItem( label='aimConstraint' )
cmds.checkBox( 'maintainOffset',label='Maintain Offset',cc='changeCheck()' )
cmds.separator(h=10,p='global')

cmds.text(label="Step2 : Set targets and objects",h=20,p='global',al='left')
cmds.rowColumnLayout( numberOfRows=1,p='global' )
cmds.button('Set Targets',w=90,h=30,c='setTargets()')
cmds.separator(w=10)
cmds.button('Set Objects',w=90,h=30,c='setObjects()')
cmds.separator(h=10,p='global')

cmds.text(label="Step3 : Constrain",h=20,p='global',al='left')
cmds.button('Constrain',w=90,h=30,p='global',c='constrain()')


cmds.showWindow(window)



