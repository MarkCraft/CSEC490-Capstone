import gtirb
import gtirb_capstone
import gtirb_functions
import gtirb_rewriting.driver
import gtirb_rewriting.utils
from gtirb_rewriting import *
import gtirb_rewriting
import uuid


class NopPass(Pass):
    
    def begin_module(self, module, functions, context):

        listofblocks = []
        for function in reversed(functions):         
            for b in function.get_all_blocks():
                listofblocks.append(b)
            break

        for b in listofblocks:
            print(b)
            context.insert_at(b, 0, Patch.from_function(self.more_fake_patch))
            break

        context.apply




    @patch_constraints(x86_syntax=X86Syntax.INTEL)
    def dummy_patch(self, context):
        return """
            XCHG eax, ebx
            XOR edx, 0
            mov edx, edx
            xchg ebx, eax
        """

    

    
if __name__ == "__main__":
    # Allow gtirb-rewriting to provide us a command line driver. See
    # docs/Drivers.md for details.
    gtirb_rewriting.driver.main(NopPass)