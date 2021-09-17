from pygame import mixer
from pygame.mixer import music
from pygame import time as pytime
import threading
class MusicPlayer():
    def __init__(self, *songs, loop:bool or bool = False, tick:int = 3000, volume:float = 1) -> None:
        self.songs:list[str] = list(songs)
        self.songs_name:list[str] = [song.split('/')[-1].split('\\')[-1].split('.')[1] for song in self.songs]
        self.loop = loop
        self.clock = pytime.Clock()
        self.tick = tick
        self.paused = False
        self.pausepos = 0
        self.stop = False
        self.volume = volume
        self.now_file = None
        self.now_song_name = None
        self.play_t = threading.Thread()
        self.replay = False
        mixer.init()
        music.set_volume(volume)

    def play(self, index_number:int = 1, pos:float = 0):
        self.pos = pos
        if index_number > len(self.songs):
            index_number = len(self.songs)
        elif index_number < 1:
            index_number = 1
        if self.play_t.is_alive():
            self.stop = True
            self.replay = True
            self.indexn = index_number
            return
        def _play(indexn:int):
            music.load(self.songs[indexn - 1])
            music.play(start=self.pos)
            self.now_file = self.songs[indexn - 1]
            self.now_song_name = self.songs[indexn - 1].split('/')[-1].split('\\')[-1].split('.')[1]
            while True:
                if music.get_busy():
                    self.clock.tick(self.tick)
                else:
                    if not self.paused:
                        break
                if self.stop:
                    break
            music.unpause()
            self.pos = 0
            self.stop = False
            self.now_song_name = None
            if self.replay:
                self.replay = False
                _play(self.indexn)
                self.indexn = 1
            elif indexn < len(self.songs):
                _play(indexn + 1)
            else:
                if self.loop:
                    _play(1)
        
        self.play_t = threading.Thread(target=_play,args=(index_number,))
        self.play_t.daemon = True
        self.play_t.start()
    
    def tp(self, pos:float):
        music.set_pos(pos)

    def skip(self):
        self.stop = True
        
    def pause(self):
        self.paused = True
        music.pause()

    def unpuase(self):
        music.unpause()
        self.paused = False
            
    def set_volume(self, volume:float = 1):
        music.set_volume(volume)
        self.volume = music.get_volume()
        
    def add_queue(self, *songs):
        self.songs += list(songs)
        self.songs_name:list[str] = [song.split('/')[-1].split('\\')[-1].split('.')[1] for song in self.songs]

    def delete_song(self, index_number:int):
        try:
            if self.now_file == self.songs[index_number - 1]:
                self.stop = True
            del self.songs[index_number - 1]
            self.songs_name:list[str] = [song.split('/')[-1].split('\\')[-1].split('.')[1] for song in self.songs]
        except: pass