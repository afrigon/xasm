# xasm

Assembler for xpu, a Minecraft CPU built in redstone. It takes an assembly
source file and produces a Litematica schematic (`.litematic`) that lays the
program out as a 1024-word by 16-bit ROM of repeaters, ready to paste into a
world beside the CPU.

## Quick start

```sh
mise run install
mise run xasm -- build examples/helloworld.asm -o helloworld.litematic
```

## Usage

`xasm build` assembles a source file and writes the resulting schematic:

```sh
mise run xasm -- build <input> --output <output>
```

Without `--output`, the schematic is written next to the input file.
