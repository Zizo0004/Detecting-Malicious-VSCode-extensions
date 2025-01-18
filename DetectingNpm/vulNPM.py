import json
class DetectNpmVul:
    def __init__(self):
        self.vulNPM = []

    def readJsonFile(self, path):
        try:
            with open(path, 'r',encoding="utf8") as json_file:
                data = json.load(json_file)
                print(data['dependencies'])
                return data   
        except Exception as e:
            print(e)

attempt1 = DetectNpmVul()
attempt1.readJsonFile(r"C:/Users/Ziyad/.vscode/extensions/ms-python.vscode-pylance-2024.12.1/package.json")
