from Util import materialType


class MaterialManager:

    def __init__(self, params: list):
        self.params = params
        # other configurations

    def _announceMaterial(self, text: str) -> bool:
        returnValue = False
        try:
            returnValue = self.announcer(text)
        except:
            print("Announcement of material type is failed.")
            returnValue = False
        finally:
            return returnValue

    def _announceMaterial(self, text: str) -> bool:
        return self.announcer(text)
