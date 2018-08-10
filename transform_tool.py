import maya.cmds as cmds

def w_move():
    objectSelected=cmds.ls(sl=1)
    for i in objectSelected:
        Px=cmds.textField(a,q=1,tx=1)
        Py=cmds.textField(b,q=1,tx=1)
        Pz=cmds.textField(c,q=1,tx=1)
        cmds.move(Px,Py,Pz,i,rpr=1)

def Freeze():
    objectSelected=cmds.ls(sl=1)
    for i in objectSelected:
        cmds.makeIdentity( i, apply=True, translate=True , rotate=True , scale=True )

def Center():
    objectSelected=cmds.ls(sl=1)
    for i in objectSelected:
        cmds.xform(i,cp=1)

def floor():
    objectSelected=cmds.ls(sl=1)
    sVtx=cmds.polyListComponentConversion(objectSelected,tv=1)
    cmds.select(sVtx)
    vertexList=cmds.ls(sl=1,fl=1)
    yPosition=[]
    for i in vertexList:
        y=cmds.xform(i,q=1,t=1,ws=1)
        yPosition.append(y[1])
    yMin=reduce(min,(yPosition))
    cmds.xform(objectSelected,ws=1,r=1,t=(0,-yMin,0))
    cmds.select(objectSelected)

def x_min():
    objectSelected=cmds.ls(sl=1)
    for os in objectSelected:
        sVtx=cmds.polyListComponentConversion(os,tv=1)
        cmds.select(sVtx)
        vertexList=cmds.ls(sl=1,fl=1)
        xPosition=[]
        for i in vertexList:
            x=cmds.xform(i,q=1,t=1,ws=1)
            xPosition.append(x[0])
        xMin=reduce(min,(xPosition))
        rpivotPosition=cmds.xform(os,q=1,rp=1,ws=1)
        length=-rpivotPosition[0]+xMin
        cmds.xform(os,ws=1,r=1,rp=(length,0,0))
        rpivotPosition=cmds.xform(os,q=1,rp=1,ws=1)
        cmds.xform(os,ws=1,a=1,sp=rpivotPosition)
    cmds.select(objectSelected)

def x_max():
    objectSelected=cmds.ls(sl=1)
    for os in objectSelected:
        sVtx=cmds.polyListComponentConversion(os,tv=1)
        cmds.select(sVtx)
        vertexList=cmds.ls(sl=1,fl=1)
        xPosition=[]
        for i in vertexList:
            x=cmds.xform(i,q=1,t=1,ws=1)
            xPosition.append(x[0])
        xMin=reduce(max,(xPosition))
        rpivotPosition=cmds.xform(os,q=1,rp=1,ws=1)
        length=-rpivotPosition[0]+xMin
        cmds.xform(os,ws=1,r=1,rp=(length,0,0))
        rpivotPosition=cmds.xform(os,q=1,rp=1,ws=1)
        cmds.xform(os,ws=1,a=1,sp=rpivotPosition)
    cmds.select(objectSelected)

def y_min():
    objectSelected=cmds.ls(sl=1)
    for os in objectSelected:
        sVtx=cmds.polyListComponentConversion(os,tv=1)
        cmds.select(sVtx)
        vertexList=cmds.ls(sl=1,fl=1)
        yPosition=[]
        for i in vertexList:
            y=cmds.xform(i,q=1,t=1,ws=1)
            yPosition.append(y[1])
        yMin=reduce(min,(yPosition))
        rpivotPosition=cmds.xform(os,q=1,rp=1,ws=1)
        length=-rpivotPosition[1]+yMin
        cmds.xform(os,ws=1,r=1,rp=(0,length,0))
        rpivotPosition=cmds.xform(os,q=1,rp=1,ws=1)
        cmds.xform(os,ws=1,a=1,sp=rpivotPosition)
    cmds.select(objectSelected)

def y_max():
    objectSelected=cmds.ls(sl=1)
    for os in objectSelected:
        sVtx=cmds.polyListComponentConversion(os,tv=1)
        cmds.select(sVtx)
        vertexList=cmds.ls(sl=1,fl=1)
        yPosition=[]
        for i in vertexList:
            y=cmds.xform(i,q=1,t=1,ws=1)
            yPosition.append(y[1])
        yMin=reduce(max,(yPosition))
        rpivotPosition=cmds.xform(os,q=1,rp=1,ws=1)
        length=-rpivotPosition[1]+yMin
        cmds.xform(os,ws=1,r=1,rp=(0,length,0))
        rpivotPosition=cmds.xform(os,q=1,rp=1,ws=1)
        cmds.xform(os,ws=1,a=1,sp=rpivotPosition)
    cmds.select(objectSelected)

def z_min():
    objectSelected=cmds.ls(sl=1)
    for os in objectSelected:
        sVtx=cmds.polyListComponentConversion(os,tv=1)
        cmds.select(sVtx)
        vertexList=cmds.ls(sl=1,fl=1)
        zPosition=[]
        for i in vertexList:
            z=cmds.xform(i,q=1,t=1,ws=1)
            zPosition.append(z[2])
        zMin=reduce(min,(zPosition))
        rpivotPosition=cmds.xform(os,q=1,rp=1,ws=1)
        length=-rpivotPosition[2]+zMin
        cmds.xform(os,ws=1,r=1,rp=(0,0,length))
        rpivotPosition=cmds.xform(os,q=1,rp=1,ws=1)
        cmds.xform(os,ws=1,a=1,sp=rpivotPosition)
    cmds.select(objectSelected)

def z_max():
    objectSelected=cmds.ls(sl=1)
    for os in objectSelected:
        sVtx=cmds.polyListComponentConversion(os,tv=1)
        cmds.select(sVtx)
        vertexList=cmds.ls(sl=1,fl=1)
        zPosition=[]
        for i in vertexList:
            z=cmds.xform(i,q=1,t=1,ws=1)
            zPosition.append(z[2])
        zMin=reduce(max,(zPosition))
        rpivotPosition=cmds.xform(os,q=1,rp=1,ws=1)
        length=-rpivotPosition[2]+zMin
        cmds.xform(os,ws=1,r=1,rp=(0,0,length))
        rpivotPosition=cmds.xform(os,q=1,rp=1,ws=1)
        cmds.xform(os,ws=1,a=1,sp=rpivotPosition)
    cmds.select(objectSelected)

def sb():
	Center()
	w_move()
	floor()
	y_min()
	Freeze()


transformTOOL=cmds.window(t='transformTOOL',w=200)
cmds.rowColumnLayout('global')
cmds.separator(h=10)
cmds.button('Align To Floor',w=200,h=50,c='floor()')
cmds.separator(h=10)
cmds.rowColumnLayout( numberOfRows=3, rowHeight=[(1, 40), (2, 40),(3,40)] )
cmds.button('X-',w=100,c='x_min()')
cmds.button('Y-',w=100,c='y_min()')
cmds.button('Z-',w=100,c='z_min()')
cmds.button('X+',w=100,c='x_max()')
cmds.button('Y+',w=100,c='y_max()')
cmds.button('Z+',w=100,c='z_max()')
cmds.button('Center Pivots',w=200,h=50,p='global',c='Center()')
cmds.separator(h=10,p='global')

cmds.rowColumnLayout('world_space',numberOfRows=1,p='global' )

cmds.rowColumnLayout( numberOfColumns=1,p='world_space' )
cmds.text(label="  X:  ",h=20)
cmds.text(label="  Y:  ",h=20)
cmds.text(label="  Z:  ",h=20)

cmds.rowColumnLayout( numberOfColumns=1,p='world_space' )
a = cmds.textField(tx='0',h=20)
b = cmds.textField(tx='0',h=20)
c = cmds.textField(tx='0',h=20)

cmds.separator(w=5,p='world_space')
cmds.button('Set',w=65,h=60,p='world_space',c='w_move()')
cmds.separator(w=5,p='world_space')
cmds.separator(h=10,p='global')

cmds.button('Freeze All Transform',w=200,h=50,p='global',c='Freeze()')
cmds.separator(h=10,p='global')


cmds.showWindow(transformTOOL)