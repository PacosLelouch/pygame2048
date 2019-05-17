# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['D:/Python/Python36-32/Lib/site-packages/PyQt5/Qt/bin', 'F:\\Database_uni\\Programming\\pythonEntertainment\\2048'],
             binaries=[],
             datas=[('D:/Python/Python36-32/Lib/site-packages/PyQt5/Qt/plugins/styles/qwindowsvistastyle.dll', '/PyQt5/Qt/plugins/styles/'), ('2048.ico', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='2048',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='2048.ico')
