[USB-OTG] 用户无法使用 USB-OTG Download 下载功能
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32s3

   .. tags::

      v0.0, v0.1, v0.2

描述
^^^^

在 Date Code（日期代码）为 2219 之前的 {IDF_TARGET_NAME} 系列芯片产品、生产工单为 PW-2022-06-XXXX 之前的 {IDF_TARGET_NAME} 系列模组和开发板产品的 eFuse 中，EFUSE_DIS_USB_OTG_DOWNLOAD_MODE (BLK0 B19[7]) 被默认置起且无法修改，因此，用户无法使用 USB-OTG Download 下载功能。

.. note::

  关于 Date Code 与生产工单的详细信息，请参考章节 :doc:`/01-chip-identification/index`。

变通方法
^^^^^^^^

也支持通过 USB-Serial-JTAG 下载固件，可参考 `USB Serial/JTAG 控制器 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32s3/api-guides/usb-serial-jtag-console.html>`__。

解决方案
^^^^^^^^

该问题已在芯片版本 :bdg-success:`v0.2` 的部分批次中修复。

在 Date Code 为 2219 及之后的 {IDF_TARGET_NAME} 系列芯片、生产工单为 PW-2022-06-XXXX 及之后的 {IDF_TARGET_NAME} 系列模组和开发板产品中，EFUSE_DIS_USB_OTG_DOWNLOAD_MODE (BLK0 B19[7]) 不再预烧写，而开放给用户烧写，这将使 USB-OTG Download 下载功能可用。

更多关于此问题的信息及使用建议，可参考 `关于 ESP32-S3 系列产品的 USB_OTG Download 和 USB_Serial_JTAG Download 功能的安全公告 <https://www.espressif.com/sites/default/files/advisory_downloads/AR2022-004%20%E5%85%B3%E4%BA%8E%20ESP32-S3%20%E7%B3%BB%E5%88%97%E4%BA%A7%E5%93%81%E7%9A%84%20USB_OTG%20Download%20%E5%92%8C%20USB_Serial_JTAG%20Download%20%E5%8A%9F%E8%83%BD%E7%9A%84%E5%AE%89%E5%85%A8%E5%85%AC%E5%91%8A%20CN.pdf>`__。
