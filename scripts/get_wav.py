import tqdm
import pathlib
import tarfile
import requests
import audio_convert

def download(url:str, out:pathlib.Path):
    #show progress bar while downloading
    print(f"Downloading {url} to {out}")
    out.parent.mkdir(parents=True, exist_ok=True)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total = int(r.headers.get('content-length', 0))
        with open(out, 'wb') as f:
            for chunk in tqdm.tqdm(r.iter_content(chunk_size=8192), total=total/8192, unit='KB', unit_scale=True):
                f.write(chunk)

def extract(tarFile:pathlib.Path, outDir:pathlib.Path):
    #extract tar file
    print(f"Extracting {tarFile} to {outDir}")
    outDir.mkdir(parents=True, exist_ok=True)
    with tarfile.open(tarFile) as tar:
        tar.extractall(outDir)

def main():
    url = "https://github.com/oxygen-dioxide/hitsune-kumi-singing-en/releases/download/0/kumi-singing-en-flac.tar"
    tarFile = pathlib.Path("temp/kumi-singing-en-flac.tar")
    if(tarFile.exists()):
        print(f"{tarFile} already exists, skipping download")
    else:
        download(url, tarFile)
    outDir = pathlib.Path("wav")
    extract(tarFile, outDir)
    print("Converting flac to wav")
    audio_convert.convert(outDir, "flac", "wav")
    print("Removing flac files")
    for f in outDir.glob("*.flac"):
        f.unlink(missing_ok=True)
    print("Done")

if __name__ == "__main__":
    main()