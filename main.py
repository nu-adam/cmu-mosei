import scripts.loader
import scripts.downloader

DEFAULT_PATH = 'cmumosei/'

if __name__ == '__main__':
    scripts.downloader.download_dataset(DEFAULT_PATH)
    scripts.loader.load_dataset(DEFAULT_PATH)
