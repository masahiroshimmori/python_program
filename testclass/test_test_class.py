class test:
    int_a = None
    int_b = 0
    int_c = 1
    str_s = "default"
    
    def set_test(self, int_b):
        self.int_b = int_b
        
    def get_test(self):

        rtn_list = (
            self.int_a,
            self.int_b,
            self.int_c,
            self.str_s
        )
        
        return rtn_list