# -*- mode: python ; coding: utf-8 -*-
a = Analysis(
    ['ImageCompressor.py'],
    pathex=[],
    binaries=[],
    datas=[('D:\\Programming\\PythonProjects\\HT\\Tools\\工具箱\\Code\\Tools\\Bin','Bin')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='图片压缩工具',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='D:\\Programming\\PythonProjects\\HT\\Tools\\工具箱\\Code\\Tools\\Icon\\压缩.ico'

)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Main',
)
