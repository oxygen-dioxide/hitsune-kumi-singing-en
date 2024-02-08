# Use ffmpeg to unify the format of wav files under /wav folder to 48000hz, single, 16bit
# Usage: In the root folder of the repo, run `python scripts/audio-unify.py`
import shutil
from   py_linq import Enumerable
import pathlib
import subprocess

def main():
    wavFolder = pathlib.Path('wav')
    tempFile = pathlib.Path('temp/temp.wav')
    tempFile.parent.mkdir(parents=True, exist_ok=True)
    wavFiles = Enumerable(wavFolder.iterdir()).where(lambda x: x.suffix == '.wav').to_list()
    for wavFile in wavFiles:
        print(f'Processing {wavFile}')
        subprocess.run(['ffmpeg', '-i', str(wavFile), '-ar', '48000', '-ac', '1', '-sample_fmt', 's16', str(tempFile), '-y'])
        shutil.copy(tempFile, wavFile)

if __name__ == '__main__':
    main()