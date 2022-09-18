# test.py
import logging
import aux

# создаем регистратор с именем 'logger'
logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)
# создаем файловый обработчик, который
# регистрирует отладочные сообщения
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# создаем консольный обработчик
# с более высоким уровнем журнала
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# создаем форматтер и добавляем его в обработчики
fmtstr = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
fmtdate = '%H:%M:%S'
formatter = logging.Formatter(fmtstr, fmtdate)
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# добавляем настроенные обработчики в логгер
logger.addHandler(fh)
logger.addHandler(ch)


# вызов функций, регистрирующих
# события в коде
logger.info('создание объекта Auxiliary')
a = auxiliary.Auxiliary()
logger.info('объект Auxiliary создан')
logger.info('вызов метода .something')
a.something()
logger.info('вызов .something закончен')
logger.info('вызов some_func()')
auxiliary.some_func()
logger.info('работа с Auxiliary закончена')