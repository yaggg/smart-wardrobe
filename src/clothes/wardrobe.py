DATA_IMAGES_BASEDIR = '../data/images/'


class Wardrobe:

    def __init__(self):
        self.clothes = {
            'Shirts': ['2100.jpg', '2099.jpg'],
            'Tshirts': ['1163.jpg', '1529.jpg'],
            'Sweatshirts': ['13089.jpg', '23876.jpg'],
            'Sweaters': ['19540.jpg', '11529.jpg'],
            'Jeans': ['39386.jpg'],
            'Trousers': ['41629.jpg', '41625.jpg'],
            'Track Pants': ['21379.jpg', '17624.jpg'],
            'Shorts': ['18005.jpg', '54924.jpg'],
            'Rain Jacket': ['52029.jpg', '52027.jpg'],
            'Jackets': ['1.jpg', '2.jpg'],
            'Casual Shoes': ['9204.jpg', '22243.jpg'],
            'Formal Shoes': ['9036.jpg', '10268.jpg'],
            'Sports Shoes': ['3168.jpg', '6628.jpg'],
            'Flip Flops': ['18653.jpg', '21825.jpg'],
            'Sandals': ['12967.jpg'],
            'Sunglasses': ['16957.jpg'],
            'Scarves': ['25947.jpg'],
            'Lip Care': ['55202.jpg'],
            'Gloves': ['19541.jpg'],
            'Umbrellas': ['14875.jpg']
        }

    def retrieve_clothes_for_type(self, clothes_type):
        return [DATA_IMAGES_BASEDIR + item for item in self.clothes[clothes_type]]
