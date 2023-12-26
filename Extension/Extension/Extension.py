import random

from krita import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.Qt import *
class MyExtension(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("testAction", "テスト!", "tools/scripts")
        # action.triggered.connect(self.exportDocument)
        action.triggered.connect(self.paintTest)
        pass
    
    def exportDocument(self):
        # ドキュメントを取得します:
        doc =  Krita.instance().activeDocument()
        # 存在しないドキュメントを保存するとクラッシュします。ですからまずそれを確認します。
        if doc is not None:
            # これによって保存ダイアログを呼び出します。保存ダイアログはタプル値を返します
            fileName = QFileDialog.getSaveFileName()[0]
            # そしてドキュメントを fileName で指定した場所にエクスポートします。
            # InfoObject は特定のエクスポートオプションに関する辞書ですが、空の辞書を渡すと Krita はデフォルトのオプションを用います。
            doc.exportImage(fileName, InfoObject())

    def drawStrokes(self):
        doc =  Krita.instance().activeDocument()
        view = Krita.instance().activeWindow().activeView()
        # print(view.currentBrushPreset())

        # with open("C:/Users/73cat/Documents/preset1.xml", 'r') as f:
        #     data = f.read()

        view.setBrushSize(random.randint(1, 1000))
        # view.setCurrentBlendingMode() #色の重なり方というより、レイヤーのモード選択のブラシ版だった
        # pre = Preset(view.currentBrushPreset())
        # view.setCurrentBrushPreset(pre.fromXML(data))
        # view.setCurrentGradient()
        # view.setCurrentPattern()

        preset = Preset(view.currentBrushPreset())
        xml_content = preset.toXML()
        file_path = "C:/Users/73cat/Documents/preset-test.xml"
        with open(file_path, 'w') as xml_file:
            xml_file.write(xml_content)

        if doc is not None:
            
            QMessageBox.information(QWidget(), "Test", "Hello! This is Krita " + Application.version()+str(view.currentGradient()))

    def paintTest(self):
        # doc =  Krita.instance().activeDocument()
        doc=Krita.instance().createDocument(800, 600, "Testing animation", "RGBA", "U8", "", 300.0)
        Krita.instance().activeWindow().addView(doc)

        rootLayer = doc.rootNode()

        pixmap=QPixmap(doc.bounds().size())
        # set image as fully transparent
        pixmap.fill(QColor(Qt.transparent))
        painter = QPainter()
        painter.begin(pixmap)
        color=QColor(255, 128, 255, 255)
        painter.setPen(QPen(color))
        painter.setBrush(QBrush(color))
        painter.drawLine(100, 300,200, 400)
        painter.drawRect(QRect(200,150,400,300))
        painter.end()
        
        fileName = "C:/Users/73cat/Documents/strokeimg.png"
        pixmap.toImage().save(fileName)


        # Set the new layer as active
        doc.setActiveNode(rootLayer)

        QMessageBox.information(QWidget(), "Test", "END")

Krita.instance().addExtension(MyExtension(Krita.instance()))