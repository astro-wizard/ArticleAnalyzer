import sys

from PyQt5.QtWidgets import QApplication

from controller.controller import AnalysisController
from models.models import AnalysisModel
from views.views import AnalysisView


def main():
    app = QApplication(sys.argv)
    model = AnalysisModel()
    view = AnalysisView()
    controller = AnalysisController(model, view)
    view.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
