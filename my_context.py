class MyContext:
    # Constructor
    def __init__(self):
        self.context_data = []

    # Add method to add a key and value to my_context
    def add(self, name_in_context, value):
        self.context_data.append({"key": name_in_context, "value": value})

    # Get method to retrieve a specific context value on the base of its name
    def get(self, name_in_context):
        for i in range(len(self.context_data)):
            if self.context_data[i]["key"] == name_in_context:
                value = self.context_data[i]["value"]
                return value
