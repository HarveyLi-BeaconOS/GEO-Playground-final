import area as area, obj_def as obj_def
import primeter as primeter
import congruent as congruent, slope as slope
import commands as commands, equation as equation

OPERATION_TOKEN = {
    "LOAD_POINT": obj_def.point_set,
    "LOAD_SHAPE": obj_def.polygon,
    "SHAPE_AREA": area.area,
    "SHAPE_PRIM": primeter.perimeter,
    "SEGM_SLOPE": slope.slope,
    "CONGRUENCE": congruent.congruent,
    "LINE_EQUAT": equation.equation,
    "COMMAND_HP": commands.help
}
