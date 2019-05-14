def packer(name=None, **kwargs):
    print(kwargs)


def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print(f"Hi {first_name} {last_name}!")
    else:
        print("Hi no name!")


packer(name="Peter", num=46, spanish_inquisition=None)
unpacker(**{"last_name": "Pallen", "first_name": "Peter"})
