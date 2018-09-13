import maya.cmds as cmds

sl=cmds.ls(sl=1)
n=sl[0]
vertex=cmds.polyEvaluate(n,v=1)
#跳转到第一帧
cmds.currentTime(int(cmds.playbackOptions(q=1,min=1)))
#生成初始曲线
for i in range(vertex):
    pos=cmds.pointPosition(n+'.vtx[%s]'%(i))
    cmds.curve(name=n+'_'+str(i),p=pos)
#添加运动轨迹点
for t in range(int(cmds.playbackOptions(q=1,min=1)),int(cmds.playbackOptions(q=1,max=1))):
    #跳转到每一帧
    cmds.currentTime(t+1)
    for i in range(vertex):
        pos=pos=cmds.pointPosition(n+'.vtx[%s]'%(i))
        name=n+'_'+str(i)
        cmds.curve(name,a=1,p=pos)