# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
import uos, machine, os
# uos.dupterm(None, 1) # disable REPL on UART(0)

def reset():
    machine.reset()

from wipe import clear

from infra.setup import setup
setup()

if 'program' in os.listdir():
    from program.program import Program
    p = Program()
    p.run()
