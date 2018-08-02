import zipfile
from IPython import embed

with zipfile.ZipFile('data/sample.zip') as existing_zip:
    existing_zip.extract('sample.txt', 'temp/')
    embed()
