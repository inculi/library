import os

import requests

EXTENSIONS = {
    'pdf' : 'application/pdf',
    'epub' : 'application/epub+zip',
    'mobi' : 'application/x-mobipocket-ebook',
    'djvu' : 'image/vnd.djvu'
}

def file_extract(fileName):
    # detect filetype
    extension = fileName.rsplit('.',1)
    if len(extension) is not 2:
        print('Could not detect file extension.')
        return None
    
    extension = extension[1]
    content_type = EXTENSIONS.get(extension.strip().lower())
    if not content_type:
        print('File type not supported.')
        return None
    
    url = 'http://localhost:9998/tika'
    headers = {
        'Content-type' : content_type,
        'fileUrl' : 'file://' + fileName
    }
    requests.put(url, headers=headers)