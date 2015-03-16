import pafy


class youtube():
    def downloadVideo(self, url, ptype='mp4', audio=False, silent=False):
        video = pafy.new(url)
        if audio:
            best = video.getbestaudio()
        else:
            best = video.getbest(preftype=ptype)
        best.download(quiet=silent, filepath="../../files")


    def downloadPlaylist(self, url, start=None, end=None, ptype='mp4', silent=False, audio=False):
        plist = pafy.get_playlist(url)
        videos = [item['pafy'] for item in plist['items']]
        if start is None:
            start = 0
        else:
            start = start - 1
        if end is None:
            end = len(videos)

        for video in videos[start:end]:
            try:
                if audio:
                    best = video.getbestaudio()
                else:
                    best = video.getbest(preftype=ptype)
                best.download(quiet=silent, filepath="../../files")
            except:
                print "Error:skipping"