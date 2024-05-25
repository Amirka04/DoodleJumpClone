import json

class Settings:
    def __init__(self):
        fileData = open("setting.json")
        self.dataSetting = json.load(fileData)

    def getWindowData(self, key : str):
        return self.dataSetting["Window"][key]
    
    def getSourceData(self, key : str):
        return self.dataSetting["source_dir"] + self.dataSetting["source"][key]
    
    def getUISetting(self, key : str):
        return self.dataSetting["ui"][key]