import struct

from xasm.generator.schematic import Schematic

class ROM1024x16Generator:
    def __init__(self):
        pass

    def generate(self, name: str, binary: bytes) -> Schematic:
        schematic = Schematic(name)

        if len(binary) % 2 != 0:
            raise ValueError("binary length is odd")

        count = len(binary) // 2

        if count > 1024:
            raise ValueError("binary is too large")

        # assuming big endian
        words = list(struct.unpack(f">{count}H", binary)) if count else []

        if count < 1024:
            words.extend([0] * (1024 - count))

        for address in range(1024):
            row             = address & 0b1111
            backward        = address & 0b1000000000
            offset          = address >> 4 & 0b001111
            is_bottom_half  = address & 0b0100000000
            indent          = address & 0b0001

            x = row * 7 + (2 if backward else 0)
            z = indent + offset * 2

            if is_bottom_half:
                z += 3 if indent else 5
                z += 31

            data = words[address]

            for i in range(16):
                bit = data >> (15 - i) & 1
                y = -i * 2 - 1

                if i > 7:
                    y -= 2

                schematic.set_block(x,  y,  -z, "minecraft:red_stained_glass")

                if bit:
                    schematic.set_block(x,  y + 1,  -z, "minecraft:repeater", delay="1", facing="east" if backward else "west")
                else:
                    schematic.set_block(x,  y + 1,  -z, "minecraft:red_stained_glass")

        return schematic
        