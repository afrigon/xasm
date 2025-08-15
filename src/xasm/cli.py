import typer

from typing import Optional
from typing_extensions import Annotated
from enum import Enum
from pathlib import Path

from xasm.assembler import Assembler
from xasm.generator import Generator
from xasm.generator.schema import SchemaVersion
from xasm.generator import GeneratorType

app = typer.Typer(add_completion=False)

class Representation(str, Enum):
    assembly = "assembly"
    binary = "binary"
    litematica = "litematica"

    def extension(self) -> str:
        match self:
            case Representation.assembly:
                return "asm"
            case Representation.binary:
                return "bin"
            case Representation.litematica:
                return "litematic"

@app.command()
def build(
    input: Annotated[Path, typer.Argument(exists=True, dir_okay=False, readable=True)],
    output: Annotated[Optional[Path], typer.Option("--output", "-o", dir_okay=False)] = None,
    emit: Annotated[Representation, typer.Option()] = Representation.binary
):
    if output is None:
        output = input.with_suffix("." + emit.extension())

    # assuming input is asm. TODO: detect if input is asm or bin

    source = input.read_text(encoding="utf-8")
    binary = Assembler().assemble(source)
    data = Generator(
        schema=SchemaVersion.rom1024x16, 
        generator_type=GeneratorType.litematica
    ).generate(name=input.with_suffix('').name, binary=binary)

    # TODO: consider emit param

    output.write_bytes(data)

@app.command()
def run():
    print("hello world")

if __name__ == "__main__":
    app()