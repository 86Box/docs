DMA
===

86Box offers two mechanisms for **Direct Memory Access**: 8237 DMA for ISA devices and direct memory read/write for PCI devices.

8237 DMA
--------

``86box/dma.h`` provides the ``dma_channel_read`` and ``dma_channel_write`` functions to read or write (respectively) a value from or to an **8237 DMA channel**.

.. flat-table:: dma_channel_read
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - channel
    - DMA channel number: ``0``-``3`` for 8-bit channels or ``5``-``7`` for 16-bit channels.

  * - **Return value**
    - 8- (channels ``0``-``3``) or 16-bit (channels ``5``-``7``) value read from the given DMA channel, or ``DMA_NODATA`` if no data was read.

      May include a ``DMA_OVER`` bit flag (located above the most significant data bit so as to not interfere with the data) indicating that this was the last byte or word transferred, after which the channel is auto-initialized or masked depending on its configuration.

.. flat-table:: dma_channel_write
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - channel
    - DMA channel number: ``0``-``3`` for 8-bit channels or ``5``-``7`` for 16-bit channels.

  * - val
    - 8- (channels ``0``-``3``) or 16-bit (channels ``5``-``7``) value to write to the given DMA channel.

  * - **Return value**
    - * ``0`` on success;
      * ``DMA_NODATA`` if no data was actually written;
      * ``DMA_OVER`` if this was the last byte or word transferred, after which the channel is auto-initialized or masked depending on its configuration.

Direct memory read/write
------------------------

``86box/mem.h`` provides the ``mem_read*_phys`` and ``mem_write*_phys`` functions, which read or write physical memory directly. These are useful for **PCI devices**, which perform DMA on their own.

.. flat-table:: mem_readb_phys / mem_readw_phys / mem_readl_phys
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - addr
    - 32-bit memory address to read.

  * - **Return value**
    - 8- (``mem_readb_phys``), 16- (``mem_readw_phys``) or 32-bit (``mem_readl_phys``) value read from the given memory address.


.. flat-table:: mem_writeb_phys / mem_writew_phys / mem_writel_phys
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - addr
    - 32-bit memory address to write.

  * - val
    - 8- (``mem_readb_phys``), 16- (``mem_readw_phys``) or 32-bit (``mem_readl_phys``) value to write to the given memory address.
