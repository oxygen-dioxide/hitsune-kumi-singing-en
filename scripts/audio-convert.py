#batch convert the format of audio files under wav folder. For example, from wav to flac.
#example usage: In the root folder of the repo, run `python scripts/audio-convert.py wav flac`
import click
import pathlib
import subprocess

@click.command()
@click.argument('inputformat')
@click.argument('outputformat')
def main(inputformat, outputformat):
    audioFolder = pathlib.Path('wav')
    inputFiles = audioFolder.glob(f'*.{inputformat}')
    for inputFile in inputFiles:
        outputFile = inputFile.with_suffix(f'.{outputformat}')
        print(f'Converting {inputFile} to {outputFile}...')
        subprocess.run(['ffmpeg', '-i', str(inputFile), str(outputFile), '-y'])

if __name__ == '__main__':
    main()