[TWAI 控制器] 当错误界定符的第 8 bit 为显性时，TWAI 控制器不能进入被动错误状态
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

描述
^^^^

当 TWAI 控制器发送数据并且 TEC 的值为 120 ~ 127 时，发送错误帧会使 TEC 增加 8 并且 TWAI 控制器会进入被动错误状态（CAN 2.0B 协议规定 TEC >= 128 时，TWAI 节点应进入错误被动状态）。但是，如果错误界定符的第 8 bit 为显性时，TEC 仍会增加 8，而 TWAI 控制器不会进入被动错误状态。再次发送错误帧后 TWAI 控制器才会进入被动错误状态。注意，由于错误界定符的第 8 bit 为显性，TWAI 控制器仍会产生协议规定的过载帧。

变通方法
^^^^^^^^

无

解决方案
^^^^^^^^

:bdg-warning:`暂无` 修复计划。
