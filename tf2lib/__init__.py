import tensorflow as tf

from tf2lib.data import *
from tf2lib.image import *
from tf2lib.ops import *
from tf2lib.utils import *

<<<<<<< HEAD
#physical_devices = tf.config.experimental.list_physical_devices('GPU')
#tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)
=======
tf.config.gpu.set_per_process_memory_growth(enabled=True)
>>>>>>> e5fecb902ff884968da182a8482c430b57f7cdc8
