from krita import *
from PyQt5.QtWidgets import QFileDialog

class MyExtension(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("testAction", "テストスクリプト", "tools/scripts")
        # action.triggered.connect(self.exportDocument)
        action.triggered.connect(self.drawStrokes)
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
        if doc is not None:
            



Krita.instance().addExtension(MyExtension(Krita.instance()))