import os

f = open("/home/tannishpage/Nextcloud/Notes/Winter Research Notes/Video Links from ABC and 7News.txt", 'r')
urls = f.readlines()
for url in urls:
    os.system("./youtube-dl {}".format(url.rstrip()))
