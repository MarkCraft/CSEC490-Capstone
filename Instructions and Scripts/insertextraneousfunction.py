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
 
        dummy_sym = context.register_insert_function("Extraneous", gtirb_rewriting.Patch.from_function(self.fake_patch))

        print(str(dummy_sym))
        context.apply
       

    @gtirb_rewriting.patch_constraints()
    def fake_patch(self, context):
        return """
            mov $42, %eax 
            mov $35, %ebx 
            mov $15, %ecx 
            mov $12, %edx 
            XOR %eax, %ebx
            XOR %ecx, %edx
            xchg %eax, %edx
            mov $3, %edx 
            XOR %eax, %eax
            ret
        """    

    
if __name__ == "__main__":
    # Allow gtirb-rewriting to provide us a command line driver. See
    # docs/Drivers.md for details.
    gtirb_rewriting.driver.main(NopPass)