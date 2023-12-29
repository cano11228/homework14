class Player:
    def __init__(self, name, video_link, duration):
        self.name = name
        self.video_link = video_link
        self.duration = duration
        self.last_time = 0
        self.quality = 'HD'

    def play(self, video_address):
        print(f"Playing video from {video_address}")
        return True

    def pause(self):
        print("Video paused")

    def save_last_time(self, time):
        self.last_time = time
        print(f"Last time saved: {self.last_time} seconds")

    def change_quality(self, new_quality):
        self.quality = new_quality
        print(f"Quality changed to {self.quality}")