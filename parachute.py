"""
class Parachute
"""
class Parachute:
    
    def __init__(self):
        self.__graph = [
            "  ___  ",
            " /___\ ",
            " \   / ",
            "  \ /  ",
        ]
        self.__status = True
        
    def print_parachute_graph(self):
        print()
        for item in self.__graph:
            print(item)
        
        if self.__status == True:
            print("   o  ")
        else:
            print("   x  ")
        
        print("  /|\ ")
        print("  / \ ")
        print()
        print("^^^^^^^")
        print()
    
    def remove_parachute_item(self):
        if len(self.__graph) > 0:
            self.__graph.pop(0)
        
    def update_parachute_info(self, validation):
        if validation == False:
            self.remove_parachute_item()
            if len(self.__graph) <= 0:
                self.__status = False
        self.print_parachute_graph()
    
    def get_parachute_status(self):
        return self.__status
    
    def get_parachute_status_message(self):
        return "alive" if self.__status else "dead"