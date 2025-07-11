[Crystal-5948] 40 MHz 晶振无法工作
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32c2

   .. tags::

      v0.0, v1.0

描述
^^^^

{IDF_TARGET_NAME} 产品设计本应同时支持 26 MHz 和 40 MHz 晶振。 但是，对于 revision v1.0 及之前的版本，部分芯片在配备 40 MHz 晶振时无法正常工作。问题的具体表现包括时钟错误或在上电启动时打印乱码等。

变通方法
^^^^^^^^

使用芯片版本 v1.0 及之前版本的芯片时，避免搭配 40 MHz 晶振，仅搭配 26 MHz 晶振使用。

解决方案
^^^^^^^^

已在芯片版本 :bdg-success:`v1.1` 中修复，可以同时支持 26 MHz 和 40 MHz 晶振。
