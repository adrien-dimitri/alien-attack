import sys
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt
from Game import Game


class AlienAttackGUI(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Alien Attack")

        self.game_layout = QtWidgets.QVBoxLayout()
        self.game_layout.setSpacing(0)
        self.game_layout.setMargin(0)

        self.header_layout = QtWidgets.QHBoxLayout()

        self.text = QtWidgets.QLabel("Save the world!")
        self.text.setFixedHeight(20)
        self.text.setStyleSheet("background: white; padding-left: 10px;")
        self.header_layout.addWidget(self.text)

        self.button = QtWidgets.QPushButton("Restart Game")
        self.button.setFixedWidth(200)
        self.button.setStyleSheet("background: white;")
        self.button.clicked.connect(self.restart_game)
        self.header_layout.addWidget(self.button)

        self.game_layout.addLayout(self.header_layout)
        self.setLayout(self.game_layout)

        self.game = Game(mode="Player")
        self.finished = False

        self.grid_css = "border: 1px solid gray;"
        self.setStyleSheet("background: black;")
        self.init_game_grid()
        self.update_game_grid()

    def restart_game(self):
        self.game = Game(mode="Player")
        self.finished = False
        self.update_game_grid()
        self.text.setText("Save the world!")
        self.text.setStyleSheet(f"background-color: white; padding-left: 10px")

    def init_game_grid(self):
        layout = QtWidgets.QGridLayout()
        layout.setSpacing(0)
        layout.setMargin(0)

        for r in range(self.game.rows):
            for c in range(self.game.columns):
                spacer = QtWidgets.QWidget()
                spacer.setStyleSheet(self.grid_css)
                layout.addWidget(spacer, r, c)

        self.game_layout.addLayout(layout)

    def update_game_status(self):
        if self.finished:
            if self.game.winner == "Humans":
                self.text.setText("Humans won!")
                self.text.setStyleSheet(f"background-color: green; padding-left: 10px")
            else:
                self.text.setText("Aliens won!")
                self.text.setStyleSheet(f"background-color: red; padding-left: 10px")

    def update_game_grid(self):
        layout = None
        for i, l in enumerate(self.layout().children()):
            if isinstance(l, QtWidgets.QGridLayout):
                layout = l

        if not layout:
            raise Exception("grid layout not found")

        for r in range(self.game.rows):
            for c in range(self.game.columns):
                if repr(self.game.sky[r][c]) == "'_'":
                    spacer = QtWidgets.QWidget()
                    spacer.setStyleSheet(self.grid_css)
                    layout.itemAtPosition(r, c).wid.deleteLater()
                    layout.addWidget(spacer, r, c)
                else:
                    picture = QtWidgets.QLabel()
                    if repr(self.game.sky[r][c]) == "SA2":
                        alien = QtGui.QPixmap("images/strong_alien.png")
                        picture.setPixmap(alien)

                    elif repr(self.game.sky[r][c]) == "SA1":
                        alien = QtGui.QPixmap("images/strong_alien_[hit].png")
                        picture.setPixmap(alien)

                    else:
                        alien = QtGui.QPixmap("images/weak_alien.png")
                        picture.setPixmap(alien)

                    picture.setStyleSheet(self.grid_css)
                    picture.setAlignment(Qt.AlignCenter)
                    layout.itemAtPosition(r, c).wid.deleteLater()
                    layout.addWidget(picture, r, c)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if not self.finished:
            if event.y() < 20:
                return
            column = event.x()//90
            column = column if column <= self.game.columns else self.game.columns
            self.finished = self.game.play_one_round(column)
            self.update_game_grid()
            self.update_game_status()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = AlienAttackGUI()
    widget.resize(900, 900)
    widget.show()

    sys.exit(app.exec_())
