import logging


def log(info):
    FORMAT = '%(asctime)s|%(message)s'
    logging.basicConfig(filename='/Users/rustambekrukhilloev/PycharmProjects/PythonProgramming/learning_logging.log', format=FORMAT)
    logger = logging.getLogger('MyLogger')
    logger.setLevel(logging.INFO)
    logger.info(info)



'''
git status
git add * or /filename
git commit -m"MessageEnter"
git push
'''

