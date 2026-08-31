# xasm

Assembler for xpu, a Minecraft CPU built in redstone. It takes an assembly
source file and produces a Litematica schematic (`.litematic`) that lays the
program out as a 1024-word by 16-bit ROM of repeaters, ready to paste into a
world beside the CPU.

## Quick start

```sh
uv sync
mise run run -- build examples/helloworld.asm -o helloworld.litematic
```

## Usage

`xasm build` assembles a source file and writes the resulting schematic:

```sh
mise run run -- build <input> --output <output>
```

Without `--output`, the schematic is written next to the input file.
