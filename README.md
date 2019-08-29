**APKDecompiler** is a Python library that compiles [APK/DEX] file using [JADX](https://github.com/skylot/jadx) .

# Install :-
`pip install git+https://github.com/1337r00t/apkdecompiler#egg=apkdecompiler`

# Requirements

Only **JAVA!** and **needs** folder in \Lib\site-packages\apkdecompiler or just edit [Should be JADX in %PATH%] :-
```python
os.system(jadx -d '+str(folder)+' '+str(self.apkfile))
```

## Examples

```python
import apkdecompiler
Test = apkdecompiler.APKDecompile('test.apk').inFolder('C:/Users/1337r00t/null/apks/')
```
or
```python
import apkdecompiler
Test = apkdecompiler.APKDecompile('test.dex').inFolder('C:/Users/1337r00t/null/apks/')
```

`&> /dev/null` if you want to hide output .

## who am i ?

[1337r00t](https://1337r00t.me/) @ Blackfox's Team .
real n00b from Saudi Arabia
