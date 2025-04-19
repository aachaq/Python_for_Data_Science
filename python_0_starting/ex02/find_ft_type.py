def all_thing_is_obj(object: any) -> int:
    if isinstance(object, (list, dict, set, tuple)):
        print(f"{type(object).__name__} : {type(object)}")
        return
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : {type(object)}")
        return
    elif isinstance(object, int):
        print("Type not found")
        return 42
    else:
        return
