import sys, os, gnureadline
from framework.objects.json_file_operation import write
from framework.path.construct import construct_path, verify_path
import errors
import import_

def shield(object):
    def warper():
        try:
            return object()
        except Exception as e:
            print(f"error: (InterpreterError@WARPER) {e}")
    try:
        return warper()
    except Exception as e:
        print(f"error: (InterpreterError@SHIELD) {e}")

class translate:
    def __init__(self, source: list): # SHAPE_CONG ABS
        self.operation_token = source[0]
        self.name = source[1]
        try:
            (int(source[2][1]),int(source[2][3]))
        except ValueError:
            try:
                (source[2][1],source[2][3],source[2][5])
            except IndexError:
                self.points = (source[2],source[3])
            else:
                self.points = (source[2][1],source[2][3],source[2][5])
        else:
            self.points = (int(source[2][1]),int(source[2][3]))

class io:
    def take():
        inputs = input("Geo Playground> ")
        return inputs.split()

class tokens:
    def __init__(self, source: any) -> None:
        splitted_stuff = translate(source=source)
        dicts = [ ]; warp = [ ]
        try:
            for x in splitted_stuff.points:
                warp.append(x)
            dicts.append(warp)
            to_be_write = import_.OPERATION_TOKEN[splitted_stuff.operation_token](
            splitted_stuff.name,
            splitted_stuff.points
            )
            write.write(dict([[to_be_write.name,to_be_write.points]]))
        except KeyError:
            raise errors.UndefinedInstructionError(f"error: instruction {splitted_stuff.operation_token} is not defined")
        except AttributeError:
            ...

def first_start_up():
    if not verify_path(construct_path("framework/setup/.setup_done")):
        print("Welcome to GEO PLAYGROUND \n \
             LOAD_POINT [NAME] (X,Y) \n  \
            LOAD_SHAPE [NAME] (PT1,PT2,PT3,...) \n  \
            SHAPE_AREA [NAME] (PT1,PT2,PT3,...) \n  \
            SHAPE_PRIM [NAME] (PT1,PT2,PT3,...) \n  \
            SEGM_SLOPE [NAME] (PT1,PT2,PT3,...) \n  \
            CONGRUENCE [NAME] SHAPE1 SHAPE2 \n  \
            LINE_EQUAT [NAME] (PT1,PT2,PT3,...) \n  \
            ")
    else:
        return

@shield
def main():
# ----------------CONFIG AREA--------------------

# Uncomment the line below will automatically overwrite global_defined_points.json
    #write.clean()
# Comment the line below will NOT show guide when first startup.
    first_start_up()

# ----------------END OF CONFIG------------------ 
    while __name__ == "__main__":
        try:
            sources = io.take()
            if sources == "exit":
                sys.exit()
            else:
                tokens(source=sources)
        except Exception as e:
            print(f"error: (InterpreterError@MAIN) {e}")
    else:
        print("fatal: Software crashed....")