import random

def new_product():
    price = random.randint(5000, 1000000)
    #se muestra el punto para separar los miles
    price = "{:,}".format(price)
    price = price.replace(',', '.')
    price = "$" + str(price) + " CLP"
    name = random.choice(['iPhone', 'Samsung', 'Huawei','Motorola'])
    description = random.choice(['Nuevo', 'Usado', 'Reacondicionado'])
    if name == 'iPhone':
        image = 'https://tiendaempresas.entel.cl/media/catalog/product/cache/e83b319fe15d087a014efa16f11c0f36/l/o/logo_ok_2_1.png'
    elif name == 'Samsung':
        image = 'https://www.mobitronics.co.ke/wp-content/uploads/2022/03/Samsung-Galaxy-S22-Ultra-5G-c-1.jpg'
    elif name == 'Huawei':
        image = 'https://mobile2go.com.my/images/thumbs/0019279_huawei-p50-pro-8gb-ram-256gb-rom-original-huawei-malaysia.png'
    elif name == 'Motorola':
        image = 'https://i0.wp.com/diariolaregion.net/wp-content/uploads/2016/05/celular.png?w=450&ssl=1'
    return {
        'price': price,
        'name': name,
        'description': description,
        'image': image
    }