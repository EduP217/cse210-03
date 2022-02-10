"""
class Parachute
"""
class Parachute:
    """
    Class Parachute
    Attributes: __graph (array) = static list of words to guess
                __status (boolean) = the status of the parachute 'alive' or 'dead'
    """
    
    def __init__(self):
        """
        Init method : Construct a new instance of the class
        """
        self.__graph = [
            "  ___  ",
            " /___\ ",
            " \   / ",
            "  \ /  ",
        ]
        self.__status = True
        
    def print_parachute_graph(self):
        """
        Print parachute graph method : Print the parachute graph on console
        """
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
    
    def __remove_parachute_item(self):
        """
        Remove parachute item method : Remove the first item from the private parachute graph list
        """
        if len(self.__graph) > 0:
            self.__graph.pop(0)
        
    def update_parachute_info(self, validation):
        """
        Update parachute info method : Make the update of the private attributes in this class
        """
        if validation == False:
            self.__remove_parachute_item()
            if len(self.__graph) <= 0:
                self.__status = False
        self.print_parachute_graph()
    
    def get_parachute_status(self):
        """
        Get parachute status method : return the value of the private __status attribute
        """
        return self.__status
    
    def get_parachute_status_message(self):
        """
        Get parachute status message method : return the message of the private __status attribute
        """
        return "alive" if self.__status else "dead"