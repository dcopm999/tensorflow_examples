from tensorflow_examples.settings import logging
import tensorflow as tf

logger = logging.getLogger(__name__)


def example01():
    logger.info('Пример объявления константных тенсоров')
    logger.info("Вызов функции tf.compat.v1.disable_eager_execution() \
    необходим для обратной совместимости с 1й версией tf")
    tf.compat.v1.disable_eager_execution()
    logger.info("Определяем константный тенсор x1")
    x1 = tf.constant(1)
    logger.info("Определяем константный тенсор x2")
    x2 = tf.constant(2)
    logger.info("Вычисляем тенсоры x1 и x2")
    z = tf.add(x1, x2)

    logger.info("Открываем сессию для вычисления графов")
    with tf.compat.v1.Session() as session:
        result = session.run(z)
    return result


def example02():
    tf.compat.v1.disable_eager_execution()
    x1 = tf.Variable(1)
    x2 = tf.Variable(2)
    z = tf.add(x1, x2)
    """
    Даже после обявления тенсоров x1 и x2 днамеческая инициализация переменных непроисходит
    для инициализации всех тенсоров необходимо добавлять дополнительный граф
    init = tf.compat.v1.global_variables_initializer()
    который должен выполняться перед основными вычислениями
    """
    init = tf.compat.v1.global_variables_initializer()
    with tf.compat.v1.Session() as session:
        session.run(init)
        result = session.run(z)
    return result


if __name__ == '__main__':
    print(example01())
