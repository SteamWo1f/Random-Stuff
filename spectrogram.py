import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QMainWindow, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # create a button to open the file dialog
        btn = QPushButton('Select Audio File', self)
        btn.clicked.connect(self.openFileDialog)
        btn.move(20, 20)

        # create a label to display the file name
        self.label = QLabel(self)
        self.label.move(20, 60)

        # create a canvas to display the spectrogram
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.move(20, 100)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Audio Spectrogram')
        self.show()

    def openFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, 'Select Audio File', '', 'Audio Files (*.wav)', options=options)
        if fileName:
            self.label.setText(fileName)
            self.generateSpectrogram(fileName)

    def generateSpectrogram(self, fileName):
        # read the audio file
        rate, data = wav.read(fileName)
        data = np.mean(data, axis=1) # take the mean of the two channels
        # plot the spectrogram
        plt.figure(figsize=(5, 4))
        plt.specgram(data, NFFT=2048, Fs=rate, noverlap=128)
        plt.axis('tight')
        plt.colorbar(format='%+2.0f dB')
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    sys.exit(app.exec_())
