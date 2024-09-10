[ULP] ULP coprocessor and touch sensors can not be used during Deep-sleep when RTC_PERIPH power domain is up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

FAST_CLK is the main working clock for ULP coprocessor and touch sensors. But if RTC_PERIH power domain is powered on, the ULP coprocessor and touch sensors will receive the startup signal earlier than the clock management module, which causes the ULP coprocessor and touch sensors working under SLOW_CLK for a period of time, resulting in inaccurate working clock.

Workarounds
^^^^^^^^^^^

There is no workaround for this issue.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
