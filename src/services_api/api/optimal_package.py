import operator

class BoxSize:
    """класс, определяющий размеры"""
    def __init__(self, height, length, width):
        self.height = height
        self.length = length
        self.width = width

    def volume(self):
        return self.height * self.width * self.length

    def fit_in(self, box):
        """метод определяет, влезет ли товар с заданными параметрами в текущий короб"""
        box_1_list_sizes = [self.width, self.height, self.length]
        box_2_list_sizes = [box.width, box.height, box.length]
        box_1_list_sizes.sort()
        box_2_list_sizes.sort()
        if box_1_list_sizes[0] >= box_2_list_sizes[0] and \
                box_1_list_sizes[1] >= box_2_list_sizes[1] and \
                box_1_list_sizes[2] >= box_2_list_sizes[2]:
            return True
        return False


class Package:
    def __init__(self, name, code, box):
        self.name = name
        self.code = code
        self.box = box
        self.volume = box.volume()


class OptimalPackage:
    def __init__(self, packages):
        self.packages = packages
        self.boxberry_package = self.boxberry_package()

    def boxberry_package(self):

        """метод получает из API список коробов и сортирует их по объему"""
        packages = [
            Package(package.name, package.code, BoxSize(package.depth, package.width, package.height))
            for package in self.packages]
        packages.sort(key=operator.attrgetter('volume'))
        return packages

    def _get_variants_boxes(self, products):
        """метод определяет 3 варианта опакоски товара (складывать по высоте, ширине или длинне)"""
        height = [i.height for i in products]
        length = [i.length for i in products]
        width = [i.width for i in products]
        return [
            BoxSize(max(height), max(length), sum(width)),
            BoxSize(max(height), sum(length), max(width)),
            BoxSize(sum(height), max(length), max(width))
        ]

    def _optimal_size(self, variants):
        """метод определяет то полежение товаров, при котором буде заниматься минимальный объем"""
        volumes = [box.width * box.height * box.length for box in variants]
        optimal_index = volumes.index(min(volumes))
        return variants[optimal_index]

    def get_package_code(self, *products):
        """метод определяет оптимальную упаковку ББ"""
        products = [BoxSize(*box) for box in products]
        variants = self._get_variants_boxes(products)
        optimal_size = self._optimal_size(variants)
        for pack in self.boxberry_package:
            if pack.box.fit_in(optimal_size):
                return pack.code
        return 803