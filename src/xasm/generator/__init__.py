from enum import Enum, auto

from xasm.generator.litematica import LitematicaGenerator
from xasm.generator.schema import SchemaVersion
from xasm.generator.schema.rom1024x16 import ROM1024x16Generator

class GeneratorType(Enum):
    litematica = auto

class Generator:
    def __init__(
        self, 
        schema: SchemaVersion = SchemaVersion.rom1024x16,
        generator_type: GeneratorType = GeneratorType.litematica
    ):
        self.schema = schema
        self.generator_type = generator_type

    def generate(self, name: str, binary: bytes) -> bytes:
        match self.generator_type:
            case GeneratorType.litematica:
                generator = LitematicaGenerator()

        match self.schema:
            case SchemaVersion.rom1024x16:
                schematic = ROM1024x16Generator().generate(name=name, binary=binary)

        return generator.generate(schematic)
