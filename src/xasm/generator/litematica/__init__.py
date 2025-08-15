import io
import nbtlib
import gzip

from litemapy import Region, BlockState

from xasm.generator.schematic import Schematic

class LitematicaGenerator:
    def __init__(self):
        pass

    def generate(self, schematic: Schematic) -> bytes:
        box = schematic.get_bounding_box()
        region = Region(box.x, box.y, box.z, box.width, box.height, box.depth)
        litematic = region.as_schematic(name=schematic.name, author="xasm")

        for (x, y, z), block in schematic.blocks.items():
            block_state = BlockState(block.id, **block.properties)
            region[x - box.x, y - box.y, z - box.z] = block_state

        nbt = litematic.to_nbt()

        buffer = io.BytesIO()
        nbtlib.File(nbt).write(buffer)
        compressed = gzip.compress(buffer.getvalue())

        return compressed