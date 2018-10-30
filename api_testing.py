# VolumIO API Testing File
# https://volumio.github.io/docs/API/WebSocket_APIs.html

from socketIO_client import SocketIO

class VolumioClient:
    """ Class for the websocket client to Volumio """

    def __init__(self):
        HOSTNAME='192.168.0.41'  # use volumio ip address here
        PORT=3000

        self._client = SocketIO(HOSTNAME, PORT, LoggingNamespace)

    def play(self):
        self._client.emit('play')

    def pause(self):
        self._client.emit('pause')

    def toggle_play(self):
        try:
            if self.state["status"] == "play":
                self._client.emit('pause')
            else:
                self._client.emit('play')
        except KeyError:
            self._client.emit('play')

    def volume_up(self):
        self._client.emit('volume', '+')

    def volume_down(self):
        self._client.emit('volume', '-')

    def previous(self):
        self._client.emit('prev')

    def next(self):
        self._client.emit('next')

    def seek(self, seconds):
        self._client.emit('seek', int(seconds))


my_client = VolumioClient
my_client.play()