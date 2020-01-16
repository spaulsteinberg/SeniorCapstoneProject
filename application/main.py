import sys
from sys import platform
from subprocess import Popen, PIPE, STDOUT, run

if __name__ == '__main__':
    if platform == "linux" or platform == "linux2":
        from PyQt5.QtWidgets import QApplication
        from gui.SNRgui import SNR

        # Instantiate instance of the SNR gui object
        app = QApplication(sys.argv)
        gui = SNR()

        app.aboutToQuit.connect(gui.mainWindowExitHandler)
        sys.exit(app.exec_())

    elif platform == "darwin":
        from PyQt5.QtWidgets import QApplication
        from gui.SNRgui import SNR

        # Instantiate instance of the SNR gui object
        app = QApplication(sys.argv)
        gui = SNR()

        app.aboutToQuit.connect(gui.mainWindowExitHandler)
        sys.exit(app.exec_())
    elif platform == "win32":
        p = Popen(['ipython', '--pylab=qt'], stdout=PIPE,  stdin=PIPE, stderr=STDOUT)
        grep_stdout = p.communicate(input=b'from PyQt5.QtWidgets import QApplication\nfrom gui.SNRgui import SNR\n'
                                          b'app = QApplication(sys.argv)\ngui = SNR()\n'
                                          b'app.aboutToQuit.connect(gui.mainWindowExitHandler)\nsys.exit(app.exec_())\n')[0]