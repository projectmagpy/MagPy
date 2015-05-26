# -*- mode: python -*-
a = Analysis(['gui_interaction.py'],
             pathex=['C:\\Users\\SarathSarika\\Dropbox\\_ProjectMagPy\\MagPy\\bin\\core'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='gui_interaction.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
