#!/usr/bin/env python3
# encoding: utf-8

import rospy
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

from typing import Final

# constants
ROS_NODE_NAME: Final[str] = "publisher"

ROS_PARAM_PUB_RATE: Final[int] = 30
ROS_IMAGE_TOPIC: Final[str] = "image"

def generate_image(width, heigt):
  image = np.random.randint(0, 255, (360, 240), dtype=np.uint8)

  return image

def main() -> None:
  rospy.init_node(ROS_NODE_NAME)

  pub_frequency: int = rospy.get_param("~rate", ROS_PARAM_PUB_RATE)

  # Q: Почему здесь не нужно писать rospy.resolve_name(ROS_IMAGE_TOPIC)?
  #
  #
  publisher = rospy.Publisher(ROS_IMAGE_TOPIC, Image, queue_size=10)
  bridge = CvBridge()
  # Обратите внимание: топик "image" может переименоваться при запуске ROS-узла.
  # rosrun project_template publisher.py image:=image_raw
  # Более подробно об этом можно узнать по ссылке: http://wiki.ros.org/Names
  rospy.loginfo(f"Publishing to '{rospy.resolve_name(ROS_IMAGE_TOPIC)}' at {pub_frequency} Hz ...")

  rate = rospy.Rate(pub_frequency)

  while not rospy.is_shutdown():
    # Задание 1: сгенерируйте случайное изображение.
    # Разрешение: 320 x 240 (ширина x высота).
    # Формат пикселей: монохром, 8-бит.
    # Создайте функцию для генерации изображения "generate_image(width = 320, height = 240)".
    image = generate_image(320, 240)
    ros_image = bridge.cv2_to_imgmsg(image, encoding="mono8")

    publisher.publish(ros_image)
    
    rate.sleep()


if __name__ == '__main__':
    main()
