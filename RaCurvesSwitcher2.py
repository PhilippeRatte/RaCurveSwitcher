import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import re as re
from functools import partial
path = mc.internalVar(usd=1)
if mc.window("nurbs", exists=True):
    mc.deleteUI("nurbs")
mc.window("nurbs", t="Controls Switcher & attributes", w=399, h=50)
form = mc.formLayout()
tabs = mc.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
mc.formLayout(form, edit=True,
              attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))
#switch
child1 = mc.gridLayout(nc=1, cwh=[399, 50], w=399, h=50)
mc.text("Choose the controler with the wanted shape then the ctrl ", h=10)
mc.button(l="copy shape", c="copyShape()", h=10)
mc.text("Same thing but this one delete the original")
mc.button(l="transfer shape", c="transfer()")
mc.text("Same thing but this one delete the original and the original shape of the ctrl")
mc.button(l="switch shape", c="switch()")
mc.setParent("..")
#attributtes
child2 = mc.scrollLayout(cr=1)

#separator
mc.frameLayout(cll=1,cl=1,l="Separator")
pm.rowColumnLayout(nc=1,rs=[10,10])
mc.button(l="separator attribute", c="separatorAttr()", h=40,w=417)
mc.setParent("..")
mc.setParent("..")

#Visibility
mc.frameLayout(cll=1,cl=1,l="Visibility")
pm.rowColumnLayout(nc=1,rs=[10,10])
mc.button(l="get the ctrl", c="getVisCtrl()", h=40,w=417)
mc.button(l="get the hidden", c="getVisibleCtrl()", h=40,w=417)
mc.textFieldGrp('VisAttrName',l='Name the attribute')
mc.button(l="create the visibility switch", c="createVisSwitch()", h=40,w=417)
mc.setParent("..")
mc.setParent("..")

#ikFK
mc.frameLayout(cll=1,cl=1,l="Ik Fk")
mc.textFieldButtonGrp('ogJnt',l='get the original joint',bl='Get',bc='getOgJnt()')
mc.textFieldButtonGrp('fkJnt',l='get the fk joint',bl='Get',bc='getFkJnt()')
mc.textFieldButtonGrp('ikJnt',l='get the ik joint',bl='Get',bc='getIkJnt()')
mc.textFieldButtonGrp('ikFkCtrl',l='get the ctrl for the switch',bl='Get',bc='getIkFkCtrl()')
mc.textFieldButtonGrp('fkCtrl',l='get the fk ctrl',bl='Get',bc='getfkCtrl()')
mc.textFieldButtonGrp('ikCtrl',l='get the ik ctrl',bl='Get',bc='getikCtrl()')
mc.textFieldButtonGrp('ikPoleCtrl',l='get the poleVector ctrl',bl='Get',bc='getikPoleCtrl()')
mc.button(l="FKIK", c="FKIK()", h=40)
mc.setParent("..")
#space switch

SpaceSwitch = mc.frameLayout(cll=1,cl=1,l="Space Switch")
pm.rowColumnLayout(nc=1,rs=[10,10])
mc.frameLayout(cll=1,cl=1,l="Space Switch groups")
mc.button(l="select the wanted the recipient of the switch", c="getChosen()")
mc.button(l="create the switches(have the selected parts to create it)", c="createSwitch()")
pm.setParent("..")
mc.radioButtonGrp("consQ",l="Constraint",nrb=3,la3=["Parent","Point","Orient"],sl=1)
mc.radioButtonGrp("moQ",l="Maintain Offset",nrb=2,la2=["Off","On"],sl=2)
mc.frameLayout(cll=1,cl=1,l="Parent Constrain Options")
mc.radioButtonGrp("rotationQ",l="Rotation Constraint",nrb=2,la2=["off","on"],sl=2)
mc.radioButtonGrp("translationQ",l="Translation Constraint",nrb=2,la2=["off","on"],sl=2)
pm.setParent("..")
mc.separator()
mc.textFieldButtonGrp("spaceGroup",l="get the attachement group",bl="Get",bc="getSpaceGroup()")
pm.textFieldGrp('AttributeName',l="Atttribute Name",w=100)
mc.separator()
mc.button(l="add parent", c="create()", h=40,w=417)
pm.setParent("..")
row1 = pm.rowColumnLayout(nc=2,rs=[10,10])
pm.setParent("..")
pm.rowColumnLayout(nc=1,rs=[10,10])
mc.text("have the ctrl selected")
mc.button(l="create space switch", c="createSpace()", h=40,w=417)
pm.setParent("..")
pm.setParent("..")
mc.setParent("..")



#Shapes switch
child3 = mc.scrollLayout(cr=1)

grid1 = mc.gridLayout(nc=3, cwh=[133, 133], w=133, h=133)

mc.iconTextButton(st='iconOnly', i=path + "/img/circlex.PNG", c="circleX()")
mc.iconTextButton(st='iconOnly', i=path + "/img/circley.PNG", c="circleY()")
mc.iconTextButton(st='iconOnly', i=path + "/img/circlez.PNG", c="circleZ()")
mc.setParent(child3)
grid2 = mc.gridLayout(nc=3, cwh=[133, 133], w=133, h=133)
mc.iconTextButton(st='iconOnly', i=path + "/img/squareX.PNG", c="squareX()")
mc.iconTextButton(st='iconOnly', i=path + "/img/squarey.PNG", c="squareY()")
mc.iconTextButton(st='iconOnly', i=path + "/img/squarez.PNG", c="squareZ()")
mc.setParent(child3)
grid3 = mc.gridLayout(nc=3, cwh=[133, 133], w=133, h=133)
mc.iconTextButton(st='iconOnly', i=path + "/img/spinX.PNG", c="spinX()")
mc.iconTextButton(st='iconOnly', i=path + "/img/spinY.PNG", c="spinY()")
mc.iconTextButton(st='iconOnly', i=path + "/img/spinZ.PNG", c="spinZ()")
mc.setParent(child3)
grid4 = mc.gridLayout(nc=3, cwh=[133, 133], w=133, h=133)
mc.iconTextButton(st='iconOnly', i=path + "/img/pinX.PNG", c="pinX()")
mc.iconTextButton(st='iconOnly', i=path + "/img/pinY.PNG", c="pinY()")
mc.iconTextButton(st='iconOnly', i=path + "/img/pinZ.PNG", c="pinZ()")
mc.setParent(child3)
grid5 = mc.gridLayout(nc=3, cwh=[133, 133], w=133, h=133)
mc.iconTextButton(st='iconOnly', i=path + "/img/pyramidX.PNG", c="pyramidX()")
mc.iconTextButton(st='iconOnly', i=path + "/img/pyramidY.PNG", c="pyramidY()")
mc.iconTextButton(st='iconOnly', i=path + "/img/pyramidZ.PNG", c="pyramidZ()")
mc.setParent(child3)
grid6 = mc.gridLayout(nc=3, cwh=[133, 133], w=133, h=133)
mc.iconTextButton(st='iconOnly', i=path + "/img/cube.PNG", c="cube()")
mc.iconTextButton(st='iconOnly', i=path + "/img/sphere.PNG", c="sphereC()")
mc.iconTextButton(st='iconOnly', i=path + "/img/4arrowX.PNG", c="fourArrowX()")
mc.setParent(child3)
grid7 = mc.gridLayout(nc=3, cwh=[133, 133], w=133, h=133)
mc.iconTextButton(st='iconOnly', i=path + "/img/4arrowY.PNG", c="fourArrowY()")
mc.iconTextButton(st='iconOnly', i=path + "/img/4arrowZ.PNG", c="fourArrowZ()")
mc.iconTextButton(st='iconOnly', i=path + "/img/doubleArrowX.PNG", c="doubleArrowX()")
mc.setParent(child3)
grid8 = mc.gridLayout(nc=3, cwh=[133, 133], w=133, h=133)
mc.iconTextButton(st='iconOnly', i=path + "/img/doubleArrowY.PNG", c="doubleArrowY()")
mc.iconTextButton(st='iconOnly', i=path + "/img/doubleArrowZ.PNG", c="doubleArrowZ()")
mc.iconTextButton(st='iconOnly', i=path + "/img/fourArrowX.PNG", c="doubleArrowX()")
mc.setParent(child3)


mc.tabLayout(tabs, edit=True, tabLabel=((child1, 'switch'), (child2, 'attributes'), (child3, 'Shapes')))

mc.showWindow()
#space switch class + command
def getSpaceGroup():
    sel=mc.ls(sl=True)
    mc.textFieldButtonGrp('spaceGroup',e=True,tx=(sel[0]))

chosen = []
def getChosen():
    chosen.clear()
    sel = mc.ls(sl=1) 
    chosen.append(sel[0])
    #print(chosen)
def createSwitch():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(cl=1)
        grp = mc.group(n=chosen[0]+"_"+node+"_spaceSwitch",em=1)
        mc.matchTransform(grp,node)
        mc.matchTransform(grp,chosen,rot=1,scl=0,pos=0)
        mc.parentConstraint(node,grp,mo=1)
        
class Elements(object):
    entry = {}

    def __init__(self, name, label):
        Elements.entry["entry"+str(len(Elements.entry))] = self
        pm.setParent(row1)
        self.label = pm.textField('text'+str(len(Elements.entry)),w=100)
        self.name = pm.textFieldButtonGrp('parent'+str(len(Elements.entry)),bl='Get',bc=partial(Elements.getPar,self),w=400)

        pm.setParent(row1)
        self.num = str(len(Elements.entry))
    def getPar(self):
            selOrg = mc.ls(sl=1)
            self.name.setText(selOrg[0])


def create():
    p1 = Elements('one',"d")

def createSpace():
    consQ =  mc.radioButtonGrp('consQ',q=1,sl=1)
    maintainOffset = mc.radioButtonGrp('moQ',q=1,sl=1)
    translationPar = mc.radioButtonGrp('translationQ',q=1,sl=1)
    rotationPar = mc.radioButtonGrp('rotationQ',q=1,sl=1)
    constraint =[]
    grp = mc.textFieldButtonGrp("spaceGroup",q=1,tx=1)
    attrName = pm.textFieldGrp('AttributeName',q=1,tx=1)
    mainOff = maintainOffset -1
    ctrl = mc.ls(sl=1)
    par = []
    label = []
    length =len(Elements.entry)
    print()
    for _ in range(length):
        gNum = str(_+1)
        sel = pm.textFieldButtonGrp('parent'+ gNum,q=1,tx=1)
        par.append(sel)
        tx = pm.textField('text'+ gNum,q=1,tx=1)
        label.append(tx)
    #add constraint
    mc.select(par,r=1)
    mc.select(grp,add=1)
    cons =[]
    consName =[]
    
    if consQ == 1:
        if translationPar == 1:
            if rotationPar == 1:
                print("it does not work with both off")
                return
            if rotationPar == 2:
                val = mc.parentConstraint(mo=mainOff,st=["x","y","z"])
                cons.append(val)
                consName.append("_parentConstraint1.")
        if translationPar == 2:
            if rotationPar == 1:
                val = mc.parentConstraint(mo=mainOff,sr=["x","y","z"])
                cons.append(val)
                consName.append("_parentConstraint1.")
            if rotationPar == 2:
                val = mc.parentConstraint(mo=mainOff)
                cons.append(val)
                consName.append("_parentConstraint1.")
    if consQ == 2:
        val =mc.pointConstraint(mo=mainOff)
        cons.append(val)
        consName.append("_pointConstraint1.")
    if consQ == 3:
        val =mc.orientConstraint(mo=mainOff)
        cons.append(val)
        consName.append("_orientConstraint1.")
    
   
    length = len(label)
    en = []
    for _ in range(length):
        string = str(label[_]+":")
        en.append(string)
    #add attribute
    enum = ''.join(en)
    attr =[]
    mc.select(ctrl,r=1)
    query = mc.attributeQuery(attrName,node=ctrl[0],ex=True)
    if query == False:
        if length == 2:
            val = mc.addAttr(ctrl,ln=attrName,at="double",min=0,max=1,k=1)
            attr.append(val)
        else:
            val = mc.addAttr(ctrl,ln=attrName,at="enum",en=enum,k=1)
            attr.append(val)
    if query == True:
        val = str((str(ctrl)) +"."+attrName)
        attr.append(val)
    for _ in range(length):
        num = str(_)
        mc.setAttr(ctrl[0]+"."+attrName,_)
        loopLen = (len(label)-1)
        print(num)
        if _ == 0:
            mc.setAttr(grp+str(consName[0])+par[_]+"W"+num,1)
            mc.setDrivenKeyframe(grp+str(consName[0])+par[_]+"W"+num,cd=ctrl[0]+"."+attrName)
            for _ in range(loopLen):
                gNum = _+1
                gNumStr = str(gNum)
                mc.setAttr(grp+str(consName[0])+par[gNum]+"W"+gNumStr,0)
                mc.setDrivenKeyframe(grp+str(consName[0])+par[gNum]+"W"+gNumStr,cd=ctrl[0]+"."+attrName)
                
            
                
        else:
            mc.setAttr(grp+str(consName[0])+par[_]+"W"+num,1)
            print(grp+str(consName[0])+par[_]+"W"+num)
            mc.setDrivenKeyframe(grp+str(consName[0])+par[_]+"W"+num,cd=ctrl[0]+"."+attrName)
            size = len(label)
            for x in range(size):
                if x == _:
                    print("")
                else:
                    gNumStr = str(x)
                    mc.setAttr(grp+str(consName[0])+par[x]+"W"+gNumStr,0)
                    print(grp+str(consName[0])+par[x]+"W"+gNumStr)
                    mc.setDrivenKeyframe(grp+str(consName[0])+par[x]+"W"+gNumStr,cd=ctrl[0]+"."+attrName)
                
                
        mc.setAttr(ctrl[0]+"."+attrName,0)
            
            
        
    
    
    

#shapes switch def
def circleX():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mc.circle(nrx=1, nrz=0)
        mc.select(ctrl, r=1)
        mel.eval("DeleteHistory;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def circleY():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mc.circle(nry=1, nrz=0)
        mc.select(ctrl, r=1)
        mel.eval("DeleteHistory;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def circleZ():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mc.circle(nrz=1)
        mc.select(ctrl, r=1)
        mel.eval("DeleteHistory;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def squareX():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 1 -p 0 1 1 -p 0 1 -1 -p 0 -1 -1 -p 0 -1 1 -p 0 1 1 -k 0 -k 1 -k 2 -k 3 -k 4 ;")
        mc.select(ctrl, r=1)
        mel.eval("DeleteHistory;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def squareY():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -p 1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 ;")
        mc.select(ctrl, r=1)
        mel.eval("DeleteHistory;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)


def squareZ():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 1 -p -1 1 0 -p 1 1 0 -p 1 -1 0 -p -1 -1 0 -p -1 1 0 -k 0 -k 1 -k 2 -k 3 -k 4 ;")
        mc.select(ctrl, r=1)
        mel.eval("DeleteHistory;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def spinX():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 1 -p 0 0 0 -p 4 0 0 -p 4 1 0 -p 6 1 0 -p 6 -1 0 -p 4 -1 0 -p 4 0 0 -p 4 0 -1 -p 6 0 -1 -p 6 0 1 -p 4 0 1 -p 4 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 ;")
        mc.select(ctrl, r=1)
        mel.eval("DeleteHistory;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def spinY():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 1 -p 0 0 0 -p 0 4 0 -p -1 4 0 -p -1 6 0 -p 1 6 0 -p 1 4 0 -p 0 4 0 -p 0 4 -1 -p 0 6 -1 -p 0 6 1 -p 0 4 1 -p 0 4 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 ;")
        mc.select(ctrl, r=1)
        mel.eval("DeleteHistory;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def spinZ():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 1 -p 0 0 0 -p 0 0 4 -p 0 1 4 -p 0 1 6 -p 0 -1 6 -p 0 -1 4 -p 0 0 4 -p 1 0 4 -p 1 0 6 -p -1 0 6 -p -1 0 4 -p 0 0 4 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 ;")
        mc.select(ctrl, r=1)
        mel.eval("DeleteHistory;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def pinX():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 3 -p 0 0 0 -p 0 0 0 -p 0 3 0 -p 0 3 0 -p 0 3 0 -p -1 3 0 -p -1 4 0 -p -1 5 0 -p 0 5 0 -p 0 5 0 -p 0 5 0 -p 1 5 0 -p 1 4 0 -p 1 3 0 -p 0.00218946 3.000466 0 -p 0.00218946 3.000466 0 -k 0 -k 0 -k 0 -k 1 -k 1 -k 1 -k 2 -k 2 -k 2 -k 3 -k 3 -k 3 -k 4 -k 4 -k 4 -k 5 -k 5 -k 5 ;")
        mc.select(ctrl, r=1)
        mc.rotate(-90, y=1)
        mel.eval("DeleteHistory;")
        mel.eval("makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def pinY():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 3 -p 0 0 0 -p 0  0 0 -p 0 3 0 -p 0 3 0 -p 0 3 0 -p -1 3 0 -p -1 4 0 -p -1 5 0 -p 0 5 0 -p 0 5 0 -p 0 5 0 -p 1 5 0 -p 1 4 0 -p 1 3 0 -p 0.00218946 3.000466 0 -p 0.00218946 3.000466 0 -k 0 -k 0 -k 0 -k 1 -k 1 -k 1 -k 2 -k 2 -k 2 -k 3 -k 3 -k 3 -k 4 -k 4 -k 4 -k 5 -k 5 -k 5 ;")
        mc.select(ctrl, r=1)
        mc.rotate(90, x=1)
        mel.eval("DeleteHistory;")
        mel.eval("makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def pinZ():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 3 -p 0 0 0 -p 0 0 0 -p 0 3 0 -p 0 3 0 -p 0 3 0 -p -1 3 0 -p -1 4 0 -p -1 5 0 -p 0 5 0 -p 0 5 0 -p 0 5 0 -p 1 5 0 -p 1 4 0 -p 1 3 0 -p 0.00218946 3.000466 0 -p 0.00218946 3.000466 0 -k 0 -k 0 -k 0 -k 1 -k 1 -k 1 -k 2 -k 2 -k 2 -k 3 -k 3 -k 3 -k 4 -k 4 -k 4 -k 5 -k 5 -k 5 ;")
        mc.select(ctrl, r=1)
        mel.eval("DeleteHistory;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def pyramidX():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 1 -p 0 0 2 -p -2 0 0 -p 0 0 -2 -p 2 0 0 -p 0 0 2 -p 0 3 0 -p 0 0 -2 -p 2 0 0 -p 0 3 0 -p -2 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 ;")
        mc.select(ctrl, r=1)
        mc.rotate(-90, z=1)
        mel.eval("DeleteHistory;")
        mel.eval("makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def pyramidY():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 1 -p 0 0 2 -p -2 0 0 -p 0 0 -2 -p 2 0 0 -p 0 0 2 -p 0 3 0 -p 0 0 -2 -p 2 0 0 -p 0 3 0 -p -2 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 ;")
        mc.select(ctrl, r=1)
        mel.eval("DeleteHistory;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def pyramidZ():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 1 -p 0 0 2 -p -2 0 0 -p 0 0 -2 -p 2 0 0 -p 0 0 2 -p 0 3 0 -p 0 0 -2 -p 2 0 0 -p 0 3 0 -p -2 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 ;")
        mc.select(ctrl, r=1)
        mc.rotate(90, x=1)
        mel.eval("DeleteHistory;")
        mel.eval("makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def cube():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 1 -p -1 0 -1 -p -1 1 -1 -p 1 1 -1 -p 1 -1 -1 -p -1 -1 -1 -p -1 0 -1 -p -1 1 -1 -p -1 1 1 -p 1 1 1 -p 1 1 -1 -p 1 -1 -1 -p 1 -1 1 -p 1 1 1 -p -1 1 1 -p -1 -1 1 -p 1 -1 1 -p -1 -1 1 -p -1 -1 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 ;")
        mc.select(ctrl, r=1)
        mel.eval("DeleteHistory;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def cube():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 1 -p -1 0 -1 -p -1 1 -1 -p 1 1 -1 -p 1 -1 -1 -p -1 -1 -1 -p -1 0 -1 -p -1 1 -1 -p -1 1 1 -p 1 1 1 -p 1 1 -1 -p 1 -1 -1 -p 1 -1 1 -p 1 1 1 -p -1 1 1 -p -1 -1 1 -p 1 -1 1 -p -1 -1 1 -p -1 -1 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 ;")
        mc.select(ctrl, r=1)
        mel.eval("DeleteHistory;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def sphereC():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 3 -p 0 0 -1 -p 1 0 -1 -p 1 0 0 -p 1 0 0 -p 1 0 0 -p 1 0 1 -p 0 0 1 -p -1 0 1 -p -1 0 0 -p -1 0 0 -p -1 0 0 -p -1.000015 -0.00153565 -0.999984 -p -1.4884e-05 -0.00153565 -0.999984 -p 0.000146115 -0.00153565 -0.999501 -p 0 1 -1 -p 0 1 0 -p 0 1 1 -p 0 -0.000220475 0.987424 -p 0 -0.000220475 0.987424 -p 0 -0.000220475 0.987424 -p 0 -1 1 -p 0 -1 0 -p 0 -1 -1 -p 1.0936e-05 -0.00305433 -0.999997 -p 1.0936e-05 -0.00305433 -0.999997 -p 1.0936e-05 -0.00305433 -0.999997 -p -0.01185 1 -1 -p 0.00050745 0.999722 -0.00044319 -p 1.000493 0.973931 -0.00041398 -p 0.999744 -0.0127215 0 -p 0.999744 -0.0127215 0 -p 0.999744 -0.0127215 0 -p 0.993796 -0.98829 0 -p -0.00620429 -0.98829 0 -p -1.006204 -0.98829 0 -p -0.995801 -0.00576183 0 -p -0.995801 -0.00576183 0 -p -0.995801 -0.00576183 0 -p -0.998494 0.999722 -0.00058387 -p 0.00150595 0.999722 -0.00058387 -k 0 -k 0 -k 0 -k 1 -k 1 -k 1 -k 2 -k 2 -k 2 -k 3 -k 3 -k 3 -k 4 -k 4 -k 4 -k 5 -k 5 -k 5 -k 6 -k 6 -k 6 -k 7 -k 7 -k 7 -k 8 -k 8 -k 8 -k 9 -k 9 -k 9 -k 10 -k 10 -k 10 -k 11 -k 11 -k 11 -k 12 -k 12 -k 12 -k 13 -k 13 -k 13 ;")
        mc.select(ctrl, r=1)
        mel.eval("DeleteHistory;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def fourArrowX():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 3 -p -1 0 -3 -p -1 0 -3 -p -1 0 -5 -p -1 0 -5 -p -1 0 -5 -p -2 0 -5 -p -2 0 -5 -p -2 0 -5 -p 0 0 -7 -p 0 0 -7 -p 0 0 -7 -p 2 0 -5 -p 2 0 -5 -p 2 0 -5 -p 1 0 -5 -p 1 0 -5 -p 1 0 -5 -p 1 0 -3 -p 1 0 -3 -p 1 0 -3 -p 3 0 -1 -p 3 0 -1 -p 3 0 -1 -p 5 0 -1 -p 5 0 -1 -p 5 0 -1 -p 5 0 -2 -p 5 0 -2 -p 5 0 -2 -p 7 0 0 -p 7 0 0 -p 7 0 0 -p 5 0 2 -p 5 0 2 -p 5 0 2 -p 5 0 1 -p 5 0 1 -p 5 0 1 -p 3 0 1 -p 3 0 1 -p 3 0 1 -p 1 0 3 -p 1 0 3 -p 1 0 3 -p 1 0 5 -p 1 0 5 -p 1 0 5 -p 2 0 5 -p 2 0 5 -p 2 0 5 -p 0 0 7 -p 0 0 7 -p 0 0 7 -p -2 0 5 -p -2 0 5 -p -2 0 5 -p -1 0 5 -p -1 0 5 -p -1 0 5 -p -1 0 3 -p -1 0 3 -p -1 0 3 -p -3 0 1 -p -3 0 1 -p -3 0 1 -p -5 0 1 -p -5 0 1 -p -5 0 1 -p -5 0 2 -p -5 0 2 -p -5 0 2 -p -7 0 0 -p -7 0 0 -p -7 0 0 -p -5 0 -2 -p -5 0 -2 -p -5 0 -2 -p -5 0 -1 -p -5 0 -1 -p -5 0 -1 -p -3 0 -1 -p -3 0 -1 -p -3 0 -1 -p -1.015695 0 -2.994582 -p -1.015695 0 -2.994582 -k 0 -k 0 -k 0 -k 1 -k 1 -k 1 -k 2 -k 2 -k 2 -k 3 -k 3 -k 3 -k 4 -k 4 -k 4 -k 5 -k 5 -k 5 -k 6 -k 6 -k 6 -k 7 -k 7 -k 7 -k 8 -k 8 -k 8 -k 9 -k 9 -k 9 -k 10 -k 10 -k 10 -k 11 -k 11 -k 11 -k 12 -k 12 -k 12 -k 13 -k 13 -k 13 -k 14 -k 14 -k 14 -k 15 -k 15 -k 15 -k 16 -k 16 -k 16 -k 17 -k 17 -k 17 -k 18 -k 18 -k 18 -k 19 -k 19 -k 19 -k 20 -k 20 -k 20 -k 21 -k 21 -k 21 -k 22 -k 22 -k 22 -k 23 -k 23 -k 23 -k 24 -k 24 -k 24 -k 25 -k 25 -k 25 -k 26 -k 26 -k 26 -k 27 -k 27 -k 27 -k 28 -k 28 -k 28 ;")
        mc.select(ctrl, r=1)
        mc.rotate(90, z=1)
        mel.eval("DeleteHistory;")
        mel.eval("makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def fourArrowY():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 3 -p -1 0 -3 -p -1 0 -3 -p -1 0 -5 -p -1 0 -5 -p -1 0 -5 -p -2 0 -5 -p -2 0 -5 -p -2 0 -5 -p 0 0 -7 -p 0 0 -7 -p 0 0 -7 -p 2 0 -5 -p 2 0 -5 -p 2 0 -5 -p 1 0 -5 -p 1 0 -5 -p 1 0 -5 -p 1 0 -3 -p 1 0 -3 -p 1 0 -3 -p 3 0 -1 -p 3 0 -1 -p 3 0 -1 -p 5 0 -1 -p 5 0 -1 -p 5 0 -1 -p 5 0 -2 -p 5 0 -2 -p 5 0 -2 -p 7 0 0 -p 7 0 0 -p 7 0 0 -p 5 0 2 -p 5 0 2 -p 5 0 2 -p 5 0 1 -p 5 0 1 -p 5 0 1 -p 3 0 1 -p 3 0 1 -p 3 0 1 -p 1 0 3 -p 1 0 3 -p 1 0 3 -p 1 0 5 -p 1 0 5 -p 1 0 5 -p 2 0 5 -p 2 0 5 -p 2 0 5 -p 0 0 7 -p 0 0 7 -p 0 0 7 -p -2 0 5 -p -2 0 5 -p -2 0 5 -p -1 0 5 -p -1 0 5 -p -1 0 5 -p -1 0 3 -p -1 0 3 -p -1 0 3 -p -3 0 1 -p -3 0 1 -p -3 0 1 -p -5 0 1 -p -5 0 1 -p -5 0 1 -p -5 0 2 -p -5 0 2 -p -5 0 2 -p -7 0 0 -p -7 0 0 -p -7 0 0 -p -5 0 -2 -p -5 0 -2 -p -5 0 -2 -p -5 0 -1 -p -5 0 -1 -p -5 0 -1 -p -3 0 -1 -p -3 0 -1 -p -3 0 -1 -p -1.015695 0 -2.994582 -p -1.015695 0 -2.994582 -k 0 -k 0 -k 0 -k 1 -k 1 -k 1 -k 2 -k 2 -k 2 -k 3 -k 3 -k 3 -k 4 -k 4 -k 4 -k 5 -k 5 -k 5 -k 6 -k 6 -k 6 -k 7 -k 7 -k 7 -k 8 -k 8 -k 8 -k 9 -k 9 -k 9 -k 10 -k 10 -k 10 -k 11 -k 11 -k 11 -k 12 -k 12 -k 12 -k 13 -k 13 -k 13 -k 14 -k 14 -k 14 -k 15 -k 15 -k 15 -k 16 -k 16 -k 16 -k 17 -k 17 -k 17 -k 18 -k 18 -k 18 -k 19 -k 19 -k 19 -k 20 -k 20 -k 20 -k 21 -k 21 -k 21 -k 22 -k 22 -k 22 -k 23 -k 23 -k 23 -k 24 -k 24 -k 24 -k 25 -k 25 -k 25 -k 26 -k 26 -k 26 -k 27 -k 27 -k 27 -k 28 -k 28 -k 28 ;")
        mc.select(ctrl, r=1)
        mel.eval("DeleteHistory;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def fourArrowZ():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 3 -p -1 0 -3 -p -1 0 -3 -p -1 0 -5 -p -1 0 -5 -p -1 0 -5 -p -2 0 -5 -p -2 0 -5 -p -2 0 -5 -p 0 0 -7 -p 0 0 -7 -p 0 0 -7 -p 2 0 -5 -p 2 0 -5 -p 2 0 -5 -p 1 0 -5 -p 1 0 -5 -p 1 0 -5 -p 1 0 -3 -p 1 0 -3 -p 1 0 -3 -p 3 0 -1 -p 3 0 -1 -p 3 0 -1 -p 5 0 -1 -p 5 0 -1 -p 5 0 -1 -p 5 0 -2 -p 5 0 -2 -p 5 0 -2 -p 7 0 0 -p 7 0 0 -p 7 0 0 -p 5 0 2 -p 5 0 2 -p 5 0 2 -p 5 0 1 -p 5 0 1 -p 5 0 1 -p 3 0 1 -p 3 0 1 -p 3 0 1 -p 1 0 3 -p 1 0 3 -p 1 0 3 -p 1 0 5 -p 1 0 5 -p 1 0 5 -p 2 0 5 -p 2 0 5 -p 2 0 5 -p 0 0 7 -p 0 0 7 -p 0 0 7 -p -2 0 5 -p -2 0 5 -p -2 0 5 -p -1 0 5 -p -1 0 5 -p -1 0 5 -p -1 0 3 -p -1 0 3 -p -1 0 3 -p -3 0 1 -p -3 0 1 -p -3 0 1 -p -5 0 1 -p -5 0 1 -p -5 0 1 -p -5 0 2 -p -5 0 2 -p -5 0 2 -p -7 0 0 -p -7 0 0 -p -7 0 0 -p -5 0 -2 -p -5 0 -2 -p -5 0 -2 -p -5 0 -1 -p -5 0 -1 -p -5 0 -1 -p -3 0 -1 -p -3 0 -1 -p -3 0 -1 -p -1.015695 0 -2.994582 -p -1.015695 0 -2.994582 -k 0 -k 0 -k 0 -k 1 -k 1 -k 1 -k 2 -k 2 -k 2 -k 3 -k 3 -k 3 -k 4 -k 4 -k 4 -k 5 -k 5 -k 5 -k 6 -k 6 -k 6 -k 7 -k 7 -k 7 -k 8 -k 8 -k 8 -k 9 -k 9 -k 9 -k 10 -k 10 -k 10 -k 11 -k 11 -k 11 -k 12 -k 12 -k 12 -k 13 -k 13 -k 13 -k 14 -k 14 -k 14 -k 15 -k 15 -k 15 -k 16 -k 16 -k 16 -k 17 -k 17 -k 17 -k 18 -k 18 -k 18 -k 19 -k 19 -k 19 -k 20 -k 20 -k 20 -k 21 -k 21 -k 21 -k 22 -k 22 -k 22 -k 23 -k 23 -k 23 -k 24 -k 24 -k 24 -k 25 -k 25 -k 25 -k 26 -k 26 -k 26 -k 27 -k 27 -k 27 -k 28 -k 28 -k 28 ;")
        mc.select(ctrl, r=1)
        mc.rotate(90, x=1)
        mel.eval("DeleteHistory;")
        mel.eval("makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def doubleArrowX():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 3 -p -1 0 -2 -p -1 0 -2 -p -2 0 -2 -p -2 0 -2 -p -2 0 -2 -p 0 0 -4 -p 0 0 -4 -p 0 0 -4 -p 2 0 -2 -p 2 0 -2 -p 2 0 -2 -p 1 0 -2 -p 1 0 -2 -p 1 0 -2 -p 1 0 2 -p 1 0 2 -p 1 0 2 -p 2 0 2 -p 2 0 2 -p 2 0 2 -p 0 0 4 -p 0 0 4 -p 0 0 4 -p -2 0 2 -p -2 0 2 -p -2 0 2 -p -1 0 2 -p -1 0 2 -p -1 0 2 -p -0.991519 0 -1.990569 -p -0.991519 0 -1.990569 -k 0 -k 0 -k 0 -k 1 -k 1 -k 1 -k 2 -k 2 -k 2 -k 3 -k 3 -k 3 -k 4 -k 4 -k 4 -k 5 -k 5 -k 5 -k 6 -k 6 -k 6 -k 7 -k 7 -k 7 -k 8 -k 8 -k 8 -k 9 -k 9 -k 9 -k 10 -k 10 -k 10 ;")
        mc.select(ctrl, r=1)
        mc.rotate(90, z=1)
        mel.eval("DeleteHistory;")
        mel.eval("makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def doubleArrowY():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 3 -p -1 0 -2 -p -1 0 -2 -p -2 0 -2 -p -2 0 -2 -p -2 0 -2 -p 0 0 -4 -p 0 0 -4 -p 0 0 -4 -p 2 0 -2 -p 2 0 -2 -p 2 0 -2 -p 1 0 -2 -p 1 0 -2 -p 1 0 -2 -p 1 0 2 -p 1 0 2 -p 1 0 2 -p 2 0 2 -p 2 0 2 -p 2 0 2 -p 0 0 4 -p 0 0 4 -p 0 0 4 -p -2 0 2 -p -2 0 2 -p -2 0 2 -p -1 0 2 -p -1 0 2 -p -1 0 2 -p -0.991519 0 -1.990569 -p -0.991519 0 -1.990569 -k 0 -k 0 -k 0 -k 1 -k 1 -k 1 -k 2 -k 2 -k 2 -k 3 -k 3 -k 3 -k 4 -k 4 -k 4 -k 5 -k 5 -k 5 -k 6 -k 6 -k 6 -k 7 -k 7 -k 7 -k 8 -k 8 -k 8 -k 9 -k 9 -k 9 -k 10 -k 10 -k 10 ;")
        mc.select(ctrl, r=1)
        mel.eval("DeleteHistory;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def doubleArrowZ():
    selOrg = mc.ls(sl=1)
    for node in selOrg:
        mc.select(node,r=1)
        selOg = mc.ls(sl=1)
        ctrl = mel.eval("curve -d 3 -p -1 0 -2 -p -1 0 -2 -p -2 0 -2 -p -2 0 -2 -p -2 0 -2 -p 0 0 -4 -p 0 0 -4 -p 0 0 -4 -p 2 0 -2 -p 2 0 -2 -p 2 0 -2 -p 1 0 -2 -p 1 0 -2 -p 1 0 -2 -p 1 0 2 -p 1 0 2 -p 1 0 2 -p 2 0 2 -p 2 0 2 -p 2 0 2 -p 0 0 4 -p 0 0 4 -p 0 0 4 -p -2 0 2 -p -2 0 2 -p -2 0 2 -p -1 0 2 -p -1 0 2 -p -1 0 2 -p -0.991519 0 -1.990569 -p -0.991519 0 -1.990569 -k 0 -k 0 -k 0 -k 1 -k 1 -k 1 -k 2 -k 2 -k 2 -k 3 -k 3 -k 3 -k 4 -k 4 -k 4 -k 5 -k 5 -k 5 -k 6 -k 6 -k 6 -k 7 -k 7 -k 7 -k 8 -k 8 -k 8 -k 9 -k 9 -k 9 -k 10 -k 10 -k 10 ;")
        mc.select(ctrl, r=1)
        mc.rotate(90, x=1)
        mel.eval("DeleteHistory;")
        mel.eval("makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;")
        mc.select(selOg, add=1)
        switch()
        mc.select(selOg, r=1)
    mc.select(selOrg,r=1)

def copyShape():
    selOrg = mc.ls(sl=1)
    # print(selOrg)
    
    mc.select(selOrg[0], r=1)
    copy = mc.duplicate()
    mc.select(copy, r=1, hi=1)
    mc.select(copy, d=1)
    shape = mc.ls(sl=1)
    mc.parent(shape, selOrg[1], s=1, r=1)
    for node in shape:
        mc.select(node, r=1)
        mc.rename(selOrg[1] + 'Shape')
    mc.delete(copy)


def transfer():
    selOrg = mc.ls(sl=1)
    # print(selOrg)
    
    mc.select(selOrg[0], r=1)
    copy = mc.duplicate()
    mc.select(copy, r=1, hi=1)
    mc.select(copy, d=1)
    shape = mc.ls(sl=1)
    mc.parent(shape, selOrg[1], s=1, r=1)
    for node in shape:
        mc.select(node, r=1)
        mc.rename(selOrg[1] + 'Shape')
    mc.delete(copy)
    mc.delete(selOrg[0])


def switch():
    selOrg = mc.ls(sl=1)
    # print(selOrg)
    
    mc.select(selOrg[0], r=1)
    copy = mc.duplicate()
    mc.select(selOrg[1], hi=1)
    mc.select(selOrg[1], d=1)
    ogShape = mc.ls(sl=1)
    mc.select(copy, r=1, hi=1)
    mc.select(copy, d=1)
    shape = mc.ls(sl=1)
    mc.parent(shape, selOrg[1], s=1, r=1)
    for node in shape:
        mc.select(node, r=1)
        mc.rename(selOrg[1] + 'Shape')
    mc.delete(copy)
    mc.delete(selOrg[0])
    mc.delete(ogShape)

def separatorAttr():
    mc.addAttr(ln="_____________________",at="enum",en="____________",k=1)

def getOgJnt():
    sel=mc.ls(sl=True)
    mc.textFieldButtonGrp('ogJnt',e=True,tx=(sel[0]))

def getFkJnt():
    sel=mc.ls(sl=True)
    mc.textFieldButtonGrp('fkJnt',e=True,tx=(sel[0]))

def getIkJnt():
    sel=mc.ls(sl=True)
    mc.textFieldButtonGrp('ikJnt',e=True,tx=(sel[0]))

def getIkFkCtrl():
    sel=mc.ls(sl=True)
    mc.textFieldButtonGrp('ikFkCtrl',e=True,tx=(sel[0]))

def getfkCtrl():
    sel=mc.ls(sl=True)
    mc.textFieldButtonGrp('fkCtrl',e=True,tx=(sel[0]))

def getikCtrl():
    sel=mc.ls(sl=True)
    mc.textFieldButtonGrp('ikCtrl',e=True,tx=(sel[0]))

def getikPoleCtrl():
    sel=mc.ls(sl=True)
    mc.textFieldButtonGrp('ikPoleCtrl',e=True,tx=(sel[0]))


def FKIK():
    #variable declaration
    ogJnt = mc.textFieldButtonGrp('ogJnt',q=True,tx=True)
    fkJnt = mc.textFieldButtonGrp('fkJnt',q=True,tx=True)
    ikJnt = mc.textFieldButtonGrp('ikJnt',q=True,tx=True)
    ikFkCtrl = mc.textFieldButtonGrp('ikFkCtrl',q=True,tx=True)
    fkCtrl = mc.textFieldButtonGrp('fkCtrl',q=True,tx=True)
    ikCtrl = mc.textFieldButtonGrp('ikCtrl',q=True,tx=True)
    ikPoleCtrl = mc.textFieldButtonGrp('ikPoleCtrl',q=True,tx=True)
    mc.select(fkJnt,r=1)
    fkJnt2 =mc.pickWalk(d='down')
    fkJnt3 =mc.pickWalk(d='down')
    mc.select(ikJnt,r=1)
    ikJnt2 =mc.pickWalk(d='down')
    ikJnt3 =mc.pickWalk(d='down')
    mc.select(fkCtrl,r=1)
    mc.pickWalk(d='down')
    mc.pickWalk(d='right')
    fkCtrl2 =mc.pickWalk(d='down')
    mc.pickWalk(d='down')
    mc.pickWalk(d='right')
    fkCtrl3 =mc.pickWalk(d='down')
    #pole vector pos 
    loc = mc.spaceLocator(n=ikPoleCtrl+"Pos_locator")
    mc.hide(loc)
    mc.matchTransform(loc,ikPoleCtrl)
    mc.parent(loc,fkCtrl)
    #parenting
    mc.select(fkJnt,r=1)
    mc.select(ikJnt,add=1)
    mc.select(ogJnt,add=1)
    prnt1 = mc.parentConstraint(mo=1)
    mc.pickWalk(d='down')
    prnt2 = mc.parentConstraint(mo=1)
    mc.pickWalk(d='down')
    prnt3 = mc.parentConstraint(mo=1)
    mc.select(ikFkCtrl,r=1)
    #switch attr + connection
    mc.addAttr(ln="FKIK",at="double",min=0,max=1,dv=0,k=1)
    revNode = mc.shadingNode("reverse",au=1,n=ogJnt+"_FKIKReverse")
    mc.connectAttr(ikFkCtrl+".FKIK",revNode+".input.inputX")
    mc.connectAttr(revNode+".output.outputX",prnt1[0]+"."+fkJnt+"W0")
    mc.connectAttr(revNode+".output.outputX",prnt2[0]+"."+fkJnt2[0]+"W0")
    mc.connectAttr(revNode+".output.outputX",prnt3[0]+"."+fkJnt3[0]+"W0")
    mc.connectAttr(ikFkCtrl+".FKIK",prnt1[0]+"."+ikJnt+"W1")
    mc.connectAttr(ikFkCtrl+".FKIK",prnt2[0]+"."+ikJnt2[0]+"W1")
    mc.connectAttr(ikFkCtrl+".FKIK",prnt3[0]+"."+ikJnt3[0]+"W1")
    mc.connectAttr(revNode+".output.outputX",fkCtrl+".visibility")
    mc.connectAttr(ikFkCtrl+".FKIK",ikCtrl+".visibility")
    mc.connectAttr(ikFkCtrl+".FKIK",ikPoleCtrl+".visibility")
    #message mapping
    mc.addAttr(ikFkCtrl,ln= "ikJnt1", at="message")
    mc.connectAttr(ikJnt+".message",ikFkCtrl+".ikJnt1",f=1)
    mc.addAttr(ikFkCtrl,ln= "ikJnt2", at="message")
    mc.connectAttr(ikJnt2[0]+".message",ikFkCtrl+".ikJnt2",f=1)
    mc.addAttr(ikFkCtrl,ln= "ikJnt3", at="message")
    mc.connectAttr(ikJnt3[0]+".message",ikFkCtrl+".ikJnt3",f=1)
    mc.addAttr(ikFkCtrl,ln= "fkCtrl1", at="message")
    mc.connectAttr(fkCtrl+".message",ikFkCtrl+".fkCtrl1",f=1)
    mc.addAttr(ikFkCtrl,ln= "fkCtrl2", at="message")
    mc.connectAttr(fkCtrl2[0]+".message",ikFkCtrl+".fkCtrl2",f=1)
    mc.addAttr(ikFkCtrl,ln= "fkCtrl3", at="message")
    mc.connectAttr(fkCtrl3[0]+".message",ikFkCtrl+".fkCtrl3",f=1)
    mc.addAttr(ikFkCtrl,ln= "ikHandle", at="message")
    mc.connectAttr(ikCtrl+".message",ikFkCtrl+".ikHandle",f=1)
    mc.addAttr(ikFkCtrl,ln= "poleVector", at="message")
    mc.connectAttr(ikPoleCtrl+".message",ikFkCtrl+".poleVector",f=1)
    mc.addAttr(ikFkCtrl,ln= "poleVectorPos", at="message")
    mc.connectAttr(loc[0]+".message",ikFkCtrl+".poleVectorPos",f=1)
  
#visCtrl  
VisCtrl = []
def getVisCtrl():
    VisCtrl.clear()
    selOrg = mc.ls(sl=1)
    VisCtrl.extend(selOrg)
    
VisibleCtrl = []
def getVisibleCtrl():
    VisibleCtrl.clear()
    selOrg = mc.ls(sl=1)
    VisibleCtrl.extend(selOrg)

def createVisSwitch():
    attrName = mc.textFieldGrp('VisAttrName',q=1,tx=1)
    attr = mc.addAttr(VisCtrl,ln=attrName,at="double",min=0,max=1,k=1)
    for node in VisibleCtrl:
        strCtrl = str(VisCtrl[0])
        mc.connectAttr(strCtrl+"."+attrName,node+".visibility")
    
    