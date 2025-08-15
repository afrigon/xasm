class Box:
    def __init__(
        self, 
        x: int,
        y: int,
        z: int,
        width: int,
        height: int,
        depth: int
    ):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.depth = depth

class BlockState:
    def __init__(self, id: str, **properties: str):
        self.id = id
        self.properties = properties

class Schematic:
    def __init__(self, name: str):
        self.name = name
        self.blocks = {}

    def set_block(self, x: int, y: int, z: int, block_id: str, **properties: str):
        self.blocks[(x, y, z)] = BlockState(block_id, **properties)

    def get_bounding_box(self) -> Box:
        iterator = iter(self.blocks.keys())

        try:
            x, y, z = next(iterator)
        except StopIteration:
            return Box(0, 0, 0, 0, 0, 0)

        minx = maxx = x
        miny = maxy = y
        minz = maxz = z

        for x, y, z in iterator:
            if x < minx: minx = x
            if y < miny: miny = y
            if z < minz: minz = z
            if x > maxx: maxx = x
            if y > maxy: maxy = y
            if z > maxz: maxz = z

        nx, fx = (maxx, minx) if abs(maxx) <= abs(minx) else (minx, maxx)
        ny, fy = (maxy, miny) if abs(maxy) <= abs(miny) else (miny, maxy)
        nz, fz = (maxz, minz) if abs(maxz) <= abs(minz) else (minz, maxz)

        def signed_inclusive_span(near: int, far: int) -> int:
            delta = far - near
            return delta + 1 if delta >= 0 else delta - 1

        width = signed_inclusive_span(nx, fx)
        height = signed_inclusive_span(ny, fy)
        depth = signed_inclusive_span(nz, fz)

        return Box(nx, ny, nz, width, height, depth)