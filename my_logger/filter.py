class Filter(object):
    """Фильтр для обработчиков, для фильтрации высоких уровней логирования"""
    def __init__(self, level):
        self.__level = level

    def filter(self, logrecord):
        return logrecord.levelno <= self.__level
