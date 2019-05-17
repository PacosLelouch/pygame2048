需要安装的包：
PyQt5
pygame
运行方式（暂定）：
从main.py打开。

使用pyinstaller（可能需要安装pywin32）生成exe：
pyinstaller --path=.../Python/Python36-32/Lib/site-packages/PyQt5/Qt/bin --add-data=".../Python/Python36-32/Lib/site-packages/PyQt5/Qt/plugins/styles/qwindowsvistastyle.dll;/PyQt5/Qt/plugins/styles/" --add-data="2048.ico;." -F -w -i 2048.ico main.py -n 2048

如：
pyinstaller --path=D:/Python/Python36-32/Lib/site-packages/PyQt5/Qt/bin --add-data="D:/Python/Python36-32/Lib/site-packages/PyQt5/Qt/plugins/styles/qwindowsvistastyle.dll;/PyQt5/Qt/plugins/styles/" --add-data="2048.ico;." -F -w -i 2048.ico main.py -n 2048