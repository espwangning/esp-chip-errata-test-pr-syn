[CPU] CPU 使用 cache 访问外部 SRAM 时，特定条件下会发生读写错误
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0

描述
^^^^

CPU 使用 cache 访问外部 SRAM 时，特定条件下会发生读写错误。

变通方法
^^^^^^^^

对于芯片版本 v0.0，CPU 使用 cache 访问外部 SRAM 时，只能够进行单向操作，即只能够单纯地进行写 SRAM 操作，或者单纯地进行读 SRAM 操作，不能交替操作。

使用 MEMW 指令：在读操作之后，加上 __asm__("MEMW") 指令，然后在 CPU 流水线被清空前再发起写操作。

解决方案
^^^^^^^^

已在芯片版本 :bdg-success:`v1.0` 中修复。
