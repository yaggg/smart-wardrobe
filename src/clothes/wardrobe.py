DATA_IMAGES_BASEDIR = '../data/fashion-products/images/'


class Wardrobe:

    def __init__(self):
        self.clothes = {
            'Shirts': ['1163.jpg', '1529.jpg'],
            'Tshirts': ['1163.jpg', '1529.jpg'],
            'Sweatshirts': ['13089.jpg', '23876.jpg'],
            'Sweaters': ['19540.jpg', '11529.jpg'],
            'Jeans': ['39386.jpg', '26994.jpg'],
            'Track Pants': ['21379.jpg', '17624.jpg'],
            'Shorts': ['18005.jpg', '54924.jpg'],
            'Rain Jacket': ['52029.jpg', '52027.jpg'],
            'Jackets': ['6889.jpg', '6887.jpg'],
            'Casual Shoes': ['9204.jpg', '39988.jpg'],
            'Formal Shoes': ['9036.jpg', '10268.jpg'],
            'Sports Shoes': ['3168.jpg', '6628.jpg'],
            'Flip Flops': ['18653.jpg', '46885.jpg'],
            'Sandals': ['12967.jpg', '8574.jpg'],
            'Sunglasses': ['16957.jpg'],
            'Scarves': ['25947.jpg'],
            'Lip Care': ['55202.jpg'],
            'Gloves': ['19541.jpg'],
            'Umbrellas': ['14875.jpg']
        }

    def retrieve_clothes_for_type(self, clothes_type):
        return [DATA_IMAGES_BASEDIR + item for item in self.clothes[clothes_type]]
