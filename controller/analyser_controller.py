class Analyser_Controller():
    def __init__(self, analyser_service) -> None:
        self.__analyser_service = analyser_service

    def analyse(self, text: str):
        # todo: add data validation
        
        return self.__analyser_service.analyse(text)