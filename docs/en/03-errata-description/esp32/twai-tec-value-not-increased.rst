[TWAI] When a stuff error occurs during arbitration whilst being transmitter, any errors in the subsequent error/overload frame will not increase the TEC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32

   .. tags::

      v0.0, v1.0, v1.1, v3.0, v3.1

Description
^^^^^^^^^^^

When a stuff error occurs during arbitration whilst being transmitter, the CAN2.0B protocol stipulates that an error frame be transmitted but the TEC should not increase (Exception 2 of Rule 3). The TWAI controller is able to fulfill these requirements without issue.

However, errors within the subsequent error/overload frames themselves will fail to increase the TWAI controller's TEC. Therefore, when a stuff error occurs during arbitration whilst being transmitter, the TEC will fail to increase in the following cases:

- Bit error in an active error flag or overload flag (Rule 4).
- Detecting too many dominant bits after the transmission of active error, passive error flag, and overload flags (Rule 6).

Workarounds
^^^^^^^^^^^

There is no workaround for this issue.

Solution
^^^^^^^^

:bdg-warning:`No fix` scheduled.
