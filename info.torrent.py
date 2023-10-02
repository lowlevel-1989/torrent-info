import hashlib
import bencodepy

with open('out.torrent', 'rb') as _torrent:
    data = _torrent.read()

torrent = bencodepy.decode(data)

print(torrent)
print()
print(torrent[b'info'])
print()
print(bencodepy.encode(torrent[b'info']))
print()

info_hash = hashlib.sha1(bencodepy.encode(torrent[b'info'])).hexdigest()

print("Info Hash:", info_hash)
