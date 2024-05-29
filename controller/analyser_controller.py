from service import analyser_service

class Analyser_Controller():
    def __init__(self):
        self.__analyser_service = analyser_service.get_service()

    def analyse(self, text: str):
        svc = analyser_service.get_service()

        return svc.analyse(text)