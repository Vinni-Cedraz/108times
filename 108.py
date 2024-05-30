import tkinter as tk
import pygame


class App:
    def __init__(self, root):
        self.root = root
        self.count = 0
        self.label = tk.Label(root, text="Bell will ring every 108 seconds")
        self.label.pack()
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound('bell.wav')
        self.sound.set_volume(0.3)
        self.ring_bell()

    def ring_bell(self):
        if self.count < 108:
            self.sound.play()
            self.count += 1
            self.root.after(
                108000, self.ring_bell
            )  # Schedule next bell ring after 108 seconds
        else:
            self.root.quit()


def main():
    """This is an extremely simple GUI application that should
    ring a bell once every 108 seconds. It does so 108 times and
    then it closes automatically after that"""
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
