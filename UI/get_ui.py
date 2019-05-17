import PyQt5.uic as uic
s = input("nameOfUIFile: ")
f = open("ui_" + s + ".py", "w")
uic.compileUi(s + ".ui", f)
f.close()
