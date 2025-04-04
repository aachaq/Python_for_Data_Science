
def NULL_not_found(object: any) -> int:
    if  object == '':
        var = ""
        m = 0
        for var_name, var_value in globals().items():
            if var_value == object:
                var += var_name
        for i in range(len(var)):
            if var[(i+1)*-1] == '_':
                m = i*-1
                break
        print(f"{var[m:len(var)]}: {object} {type(object)}")
        return 0
    elif object is False:
        var = ""
        for var_name, var_value in globals().items():
            if var_value == object:
                var = var_name
        print(f"{var}: {object} {type(object)}")
        return 0
    elif object == None:
        var = ""
        m = 0
        for var_name, var_value in globals().items():
            if var_value == object:
                var += var_name
        for i in range(len(var)):
            if var[(i+1)*-1] == '_':
                m = i*-1
                break
        print(f"{var[m:len(var)]}: {object} {type(object)}")
        return 0
    elif object == 0:
        for var_name, var_value in globals().items():
            if var_value == object:
                print(f"{var_name}: {object} {type(object)}")
                break
        return 0
    elif isinstance(object, float) and str(object) == 'nan':
        print(f"Cheese: {object} {type(object)}")
        return 0
    else:
        print("Type not Found")
        return 1

Noting = None
Cheese = float("NaN")
Zero = 0
Empty = ''
Fake = False




