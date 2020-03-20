import filetype

def main():
    kind = filetype.guess('/Users/smvamsi/Downloads/nginx.html')
    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)

if __name__ == '__main__':
    main()
