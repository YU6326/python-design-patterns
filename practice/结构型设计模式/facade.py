# Facade设计模式（外观模式）是一种软件设计模式，它提供了一个统一的接口来访问子系统中的一组接口。Facade模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。当一个系统的内部实现非常复杂，或者需要与多个复杂的子系统交互时，Facade模式可以用来简化这些交互，使客户端代码更加简洁易懂。


# +-------------------+
# |      Client       |
# +-------------------+
# | - request()       |
# +-------------------+
#           |
#           | uses
#           v
# +-------------------+
# |     Facade        |
# +-------------------+
# | + operation1()    |
# | + operation2()    |
# +-------------------+
#           ◇
#           | delegates to
#           |
# +-------------------+         +-------------------+ 
# +-------------------+         +-------------------+ 
# | + methodA1()      |         | + methodB1()      | 
# | + methodA2()      |         | + methodB2()      |  
# +-------------------+         +-------------------+ 



class AudioPlayer:
    def play(self, file_name):
        print(f"Playing audio file {file_name}")

    def stop(self):
        print("Stopping audio player")

class VideoPlayer:
    def play(self, file_name):
        print(f"Playing video file {file_name}")

    def stop(self):
        print("Stopping video player")

class MultimediaFacade:
    def __init__(self):
        self.audio_player = AudioPlayer()
        self.video_player = VideoPlayer()

    def play_audio(self, file_name):
        self.audio_player.play(file_name)

    def stop_audio(self):
        self.audio_player.stop()

    def play_video(self, file_name):
        self.video_player.play(file_name)

    def stop_video(self):
        self.video_player.stop()

# 客户端代码
facade = MultimediaFacade()
facade.play_audio('song.mp3')
facade.play_video('movie.mp4')
