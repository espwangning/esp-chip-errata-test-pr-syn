[GPIO] When certain RTC peripherals are powered on, the inputs of GPIO36 and GPIO39 will be pulled down for approximately 80 ns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

Powering on the following RTC peripherals will trigger this issue:

- SAR ADC1
- SAR ADC2
- AMP

Workarounds
^^^^^^^^^^^

When enabling power for any of these peripherals, ignore input from GPIO36 and GPIO39.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
