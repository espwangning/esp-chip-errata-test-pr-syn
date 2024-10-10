[GPIO] For pads with both GPIO and RTC_GPIO functionality, the GPIO pull-up and pull-down configuration register fields are nonfunctional
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

GPIO pull-up and pull-down resistors for pads with both GPIO and RTC_GPIO functionality can only be controlled via RTC_GPIO registers.

Workarounds
^^^^^^^^^^^

Use RTC_GPIO registers for both GPIO and RTC_GPIO functions.

Solution
^^^^^^^^

This issue is automatically worked around when using GPIO drivers in ESP-IDF v2.1 or newer.
