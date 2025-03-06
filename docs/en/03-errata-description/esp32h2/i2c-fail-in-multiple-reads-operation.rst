[I2C] I2C Slave Fails in Multiple-read Under non-FIFO Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: esp32h2

   .. tags::
      
      v0.0, v0.1

Description
^^^^^^^^^^^

If the I2C slave non-FIFO mode is enabled and the master performs multiple-read operation on the slave, the master can not correctly read the data from the slave.

Workarounds
^^^^^^^^^^^

Set I2C_FIFO_ADDR_CFG_EN and I2C_SLV_TX_AUTO_START_EN to 1 and I2C_FIFO_PRT_EN to 0 for the slave. The master uses the RSTART -> WRITE(slave addr, fifo addr) -> RSTART -> WRITE(slave addr) -> READ(NACK) -> STOP command sequence. When using this method, ensure that the slave TX FIFO is always in a non-empty state.

Solution
^^^^^^^^

Fixed in chip revision :bdg-success:`v1.2`.
