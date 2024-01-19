from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from wordcloud import WordCloud


class AnalysisController:
    """ Controller to connect the model and view """

    def __init__(self, model, view):
        self._view = view
        self._model = model
        self._view.countButton.clicked.connect(self._updateWordCount)
        self._view.actionOpen.triggered.connect(self._open_file)

    def _updateWordCount(self):

        text = self._view.textEdit.toPlainText()
        word_count = self._model.get_word_count(text)
        sentiment = self._model.analyze_sentiment(text)
        metrics = self._model.readability_analysis(text)

        self._view.resultLabel.setText(f'Word Count: {word_count}')
        self._view.sentimentLabel.setText(
            f'Sentiment: {"Positive" if sentiment.polarity > 0 else "Negative" if sentiment.polarity < 0 else "Neutral"} (Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity})')


        if word_count > 0:

            self._view.updateReadabilityTable(metrics)
            # Generate and display word cloud
            self.generateWordCloud(text)
        else:
            QMessageBox.warning(None, "Input Text",
                                "We need at least 1 word to plot a word cloud and calculate metrics.")

    def generateWordCloud(self, text):

        wordcloud = WordCloud(width=800, height=400).generate(text)

        # Convert word cloud to QPixmap
        image = wordcloud.to_image()
        image = image.convert("RGBA")
        data = image.tobytes("raw", "RGBA")
        qim = QImage(data, image.size[0], image.size[1], QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(qim)

        # Update view with the word cloud
        self._view.displayWordCloud(pixmap)

    def _open_file(self):
        file_dialog = QFileDialog(self._view)
        file_path, _ = file_dialog.getOpenFileName(self._view, "Open File", "", "All Files (*)")

        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_contents = file.read()
                self._view.textEdit.setPlainText(file_contents)
            except UnicodeDecodeError:
                QMessageBox.warning(None, "File Error",
                                    "Unable to decode the file. Please choose a valid text file.")