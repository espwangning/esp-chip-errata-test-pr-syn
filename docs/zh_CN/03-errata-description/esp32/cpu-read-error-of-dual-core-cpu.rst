[CPU] 双核 CPU 在读不同地址空间时可能会发生错误
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1

描述
^^^^

双核情况下，一个 CPU 的总线在读 A (0x3FF0_0000 ~ 0x3FF1_EFFF) 地址空间，而另一个 CPU 的总线在读 B (0x3FF4_0000 ~ 0x3FF7_FFFF) 地址空间，读 B 地址空间的 CPU 可能会发生错误。

变通方法
^^^^^^^^

以下两种方法都可以使用：

- 一个 CPU 在读 A 地址空间时，通过加锁和中断的方式来避免另一个 CPU 发起对 B 地址空间的读操作。
- 一个 CPU 在读 A 地址空间之前，加一个此 CPU 读 B 地址空间（非 FIFO 地址空间，如 0x3FF40078）操作，并且要保证读 B 地址空间操作和读 A 地址空间操作是原子的。

解决方案
^^^^^^^^

已在芯片版本 :bdg-success:`v3.0` 中修复。
