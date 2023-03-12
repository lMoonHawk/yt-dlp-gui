from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLineEdit,
    QLabel,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QTextBrowser,
    QListWidget,
)
from PyQt6.QtGui import QIcon, QFont, QTextCursor, QImage, QPixmap
from PyQt6.QtCore import Qt
import sys
import yt_dlp
import urllib.request


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YT Downloader")
        self.setWindowIcon(QIcon("assets/yt-dlp-gui.png"))
        self.setFixedWidth(750)
        # self.setFixedHeight(100)

        # URL
        url_edit = QLineEdit()
        url_edit.setPlaceholderText("Video/Playlist URL...")
        btn = QPushButton("Process")
        btn.clicked.connect(lambda: self.clicked_process(url_edit))

        url_layout = QHBoxLayout()
        url_layout.addWidget(url_edit)
        url_layout.addWidget(btn)

        # Video Info
        video_info = QGroupBox("Video info")
        self.title = QLineEdit()
        self.title.setReadOnly(True)
        self.title.setStyleSheet("QLineEdit{background-color:#f0f0f0;}")
        self.uploader = QLineEdit()
        self.uploader.setStyleSheet("QLineEdit{background-color:#f0f0f0;}")
        self.uploader.setReadOnly(True)
        self.description = QTextBrowser()
        self.description.setFixedHeight(100)
        self.description.setStyleSheet("QTextBrowser{background-color:#f0f0f0;}")
        self.thumbnail = QLabel()
        self.thumbnail.setFixedWidth(300)

        text_desc_layout = QVBoxLayout()
        text_desc_layout.addWidget(self.title)
        text_desc_layout.addWidget(self.uploader)
        text_desc_layout.addWidget(self.description)

        info_layout = QHBoxLayout()
        info_layout.addLayout(text_desc_layout)
        info_layout.addWidget(self.thumbnail)
        video_info.setLayout(info_layout)

        # Main
        main_layout = QVBoxLayout()
        main_layout.addLayout(url_layout)
        main_layout.addWidget(video_info)

        self.setLayout(main_layout)

    def update_info(self, info):
        self.title.setText(info["title"])
        self.uploader.setText(info["uploader"])
        self.description.setText(info["description"])

        thumb_url = info["thumbnail"]
        thumb_content = urllib.request.urlopen(thumb_url).read()

        thumb_img = QImage()
        thumb_img.loadFromData(thumb_content)
        thumb_pixmap = QPixmap(thumb_img).scaledToWidth(300)
        self.thumbnail.setPixmap(thumb_pixmap)

        dl = QPushButton("Download")

    def clicked_process(self, url_edit):
        # TODO: validate url
        url = url_edit.text()
        with yt_dlp.YoutubeDL({}) as ydl:
            info = ydl.extract_info(url, download=False)

        self.update_info(info)
