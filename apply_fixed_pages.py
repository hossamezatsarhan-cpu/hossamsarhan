from pathlib import Path
import shutil, datetime
ROOT=Path.cwd()
files={'lms.html':ROOT/'apps'/'lms.html','quran.html':ROOT/'apps'/'quran.html','smart-exams.html':ROOT/'apps'/'smart-exams.html','style.css':ROOT/'assets'/'css'/'style.css'}
SRC=Path(__file__).resolve().parent
for name,target in files.items():
    if not target.exists() and name!='style.css':
        target=ROOT/name
    target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists():
        stamp=datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        shutil.copy2(target,target.with_suffix(target.suffix+'.bak_'+stamp))
    shutil.copy2(SRC/name,target)
    print('updated:',target)
print('Done. Refresh browser with Ctrl+F5.')
