��Ҫ��װ�İ���
PyQt5
pygame
���з�ʽ���ݶ�����
��main.py�򿪡�

ʹ��pyinstaller��������Ҫ��װpywin32������exe��
pyinstaller --path=.../Python/Python36-32/Lib/site-packages/PyQt5/Qt/bin --add-data=".../Python/Python36-32/Lib/site-packages/PyQt5/Qt/plugins/styles/qwindowsvistastyle.dll;/PyQt5/Qt/plugins/styles/" --add-data="2048.ico;." -F -w -i 2048.ico main.py -n 2048

�磺
pyinstaller --path=D:/Python/Python36-32/Lib/site-packages/PyQt5/Qt/bin --add-data="D:/Python/Python36-32/Lib/site-packages/PyQt5/Qt/plugins/styles/qwindowsvistastyle.dll;/PyQt5/Qt/plugins/styles/" --add-data="2048.ico;." -F -w -i 2048.ico main.py -n 2048