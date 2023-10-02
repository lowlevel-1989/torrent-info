from torf import Torrent
t = Torrent(path='in',
            trackers=['https://tracker1.example.org:1234/announce',],
            comment='This is a comment')
t.private = False
t.generate()
t.write('out.torrent')
