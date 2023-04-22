import gtirb
import gtirb_capstone
import gtirb_functions
import gtirb_rewriting.driver
import gtirb_rewriting.utils
from gtirb_rewriting import *
import gtirb_rewriting
import uuid


class NopPass(Pass):
    """
    Inserts a nop at the start of every function.
    """

    def begin_module(self, module, functions, context):
        
        context.register_insert(
            AllFunctionsScope(FunctionPosition.ENTRY, BlockPosition.ENTRY),
            Patch.from_function(self.many_nop_patch),
        )

    @patch_constraints(x86_syntax=X86Syntax.INTEL)
    def many_nop_patch(self, context):
        return """
            nop
            nop
            nop
            nop
            nop
        """

    @patch_constraints()
    def nop_patch(self, context):
        return "nop"
    

    
if __name__ == "__main__":
    # Allow gtirb-rewriting to provide us a command line driver. See
    # docs/Drivers.md for details.
    gtirb_rewriting.driver.main(NopPass)