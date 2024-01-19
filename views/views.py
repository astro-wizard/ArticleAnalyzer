from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel, QGraphicsView, \
    QGraphicsScene, QTableWidget, QTableWidgetItem, QAction, QMenuBar, QMainWindow


class AnalysisView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main layout is vertical
        main_layout = QVBoxLayout(self)

        # Create horizontal layout for text edit and graph
        h_layout = QHBoxLayout()

        # Style the QTextEdit
        self.textEdit = QTextEdit(self)
        self.textEdit.setStyleSheet("QTextEdit { background-color: #ffffff; border: 1px solid #ccc; padding: 5px; }")
        h_layout.addWidget(self.textEdit)

        # Placeholder for graph
        self.graphScene = QGraphicsScene(self)
        self.graphView = QGraphicsView(self.graphScene)
        h_layout.addWidget(self.graphView)

        # Hide graph view initially
        self.graphView.hide()

        # Add horizontal layout to the main layout
        main_layout.addLayout(h_layout)

        # Add other UI elements
        self.countButton = QPushButton('Analyse Article', self)
        self.countButton.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; padding: 8px; }")

        self.resultLabel = QLabel('Number of Words: 0', self)
        self.sentimentLabel = QLabel('Sentiment: Neutral (Polarity: 0, Subjectivity: 0)', self)

        main_layout.addWidget(self.countButton)
        main_layout.addWidget(self.resultLabel)
        main_layout.addWidget(self.sentimentLabel)


        # Readability Metrics Table
        self.readabilityTable = QTableWidget(self)
        self.readabilityTable.setStyleSheet("QTableWidget { border: 1px solid #ccc; }"
                                            "QHeaderView::section { background-color: #f2f2f2; }")
        self.readabilityTable.setColumnCount(2)
        self.readabilityTable.setHorizontalHeaderLabels(["Metric", "Value"])
        self.readabilityTable.setWordWrap(True)
        main_layout.addWidget(self.readabilityTable)

        # Create a menu bar
        menubar = QMenuBar(self)
        file_menu = menubar.addMenu('File')

        # Add Open action to File menu
        self.actionOpen = QAction('Open', self)
        file_menu.addAction(self.actionOpen)

        # Set up the actionOpen trigger
        # self.actionOpen.triggered.connect(self._open_file)

        # Add the menu bar to the main layout
        main_layout.addWidget(menubar)

        # Set main layout to the widget
        self.setLayout(main_layout)

    def updateReadabilityTable(self, metrics):
        # Clear previous content
        self.readabilityTable.setRowCount(0)

        # Add metrics to the table
        for metric, value in metrics.items():
            row_position = self.readabilityTable.rowCount()
            self.readabilityTable.insertRow(row_position)
            self.readabilityTable.setItem(row_position, 0, QTableWidgetItem(metric))
            self.readabilityTable.setItem(row_position, 1, QTableWidgetItem(str(value)))

        # Resize columns to fit content
        self.readabilityTable.resizeColumnsToContents()

    def displayWordCloud(self, pixmap):
        self.graphScene.clear()  # Clear previous scene
        self.graphScene.addPixmap(pixmap)
        self.graphView.show()  # Show the graph view
