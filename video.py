import sys
from PyQt4 import Qt
import vlc
app = Qt.QApplication(sys.argv)
video = Qt.QWidget()
video.setMinimumSize(300, 300)
path="gol.mp4"
instance=vlc.Instance()
media=instance.media_new(path)
player=instance.media_player_new()
player.set_media(media)

#Is it correct? Without these 2 lines I get a separate video display otherwise I see nothing...
hwnd = video.winId().__hex__()
player.set_hwnd(hwnd);

player.play()
video.show()

app.exec_()

