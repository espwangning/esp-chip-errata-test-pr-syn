[时钟] 以太网与 Wi-Fi 共用时，ESP32 不能用作 PHY 时钟源
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

描述
^^^^

RMII 工作模式下的以太网 MAC 和 PHY 需要一个公共的 50 MHz 同步时钟（即 RMII 时钟）。如果同时使用以太网与 Wi-Fi，则 RMII 时钟不能由内部的 ESP32 APLL 产生，因为会导致时钟不稳定。

变通方法
^^^^^^^^

#. 如果要使用内部 APLL 生成同步时钟，则需要关闭 Wi-Fi。
#. 如果要同时使用以太网和 Wi-Fi，则必须使用外部 PHY 或外部时钟源提供同步时钟。

解决方案
^^^^^^^^

:bdg-warning:`暂无` 修复计划。
